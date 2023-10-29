import os, cv2

import math
import numpy as np
from threading import Thread
from multiprocessing.pool import ThreadPool, Pool
from pathlib import Path

class LoadStream():
    """可以处理多个摄像头"""
    def __init__(self, stream, 
                    img_size=640, 
                    stride=32, 
                    auto=True, 
                    transforms=None, 
                    vid_stride=1):
        self.img_size = img_size
        self.stride   = stride
        self.vid_stride = vid_stride
        sources = Path(stream).read_text().rsplit() if os.path.isfile(stream) else [stream]
        self.sources = sources
        n = len(sources)
        self.imgs, self.fps, self.frames, self.threads = [None] * n, [0] * n, [0] * n, [None] * n
        

        for idx, source in enumerate(sources):
            s = eval(source) if source.isnumeric() else source
            cap = cv2.VideoCapture(s)
            assert cap.isOpened(), f"{s} VideoCapture failed to open!"
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            self.frames[idx] = max(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), 0) or float("inf")
            self.fps[idx] = max((fps if math.isfinite(fps) else 0) % 100, 0) or 30
            ret, self.imgs[idx] = cap.read()
            self.threads[idx] = Thread(target=self.update_img, args=(idx, cap, s), daemon=True)
            self.threads[idx].start()
        # 下面需要将输入的图片尺寸转为yolo能识别的尺寸


    def update_img(self, idx, cap, s):
        n, f = 0, self.frames[idx]
        while cap.isOpened() and n < f:
            n += 1
            cap.grab()  # 用来指向下一帧
            if n % self.vid_stride == 0:
                ret, img = cap.retrieve()
                if ret:
                    self.imgs[idx] = img
                else:
                    self.imgs[idx] = np.zeros_like(self.imgs[idx])
                    cap.open(s)

    def __len__(self):
        return len(self.sources)

