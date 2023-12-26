import cv2, time
import yaml
import torch
import time
import threading
from lib.classes import *
from lib.log import logging
from lib.general import check_git_status
from src.finger_gesture_drag_block import HandControlVolume

class MetaSystem(object):
    '''
    1、读取cfg文件
    1、检查本地代码与git仓库代码相差几个commit
    2、初始化系统工作状态;
    2.1、检测相机;
    2.2、提取相机基本参数;
    '''
    def __init__(self, cfg="./cfg/init.yaml") -> None:
        """
        status
            0: 系统未开始工作
            1: 系统进入自检状态
            2: 系统状态无问题
            3: 系统进入工作状态
        """
        # 1.检测本地代码与git仓库代码
        self.MetaDic = dict()
        self.camera = Camera()
        self.sys_status = 0
        self._read_cfg(cfg)
        self._SysCheck()
        # 手势拖动方块

        # 后台加载模型
        self.thread = threading.Thread(target=self.init_model, args=())
        self.thread.start()
        # check_git_status(self.MetaDic["git-repo"]["repo"], self.MetaDic["git-repo"]["branch"])

    def init_model(self):
        self.model = torch.hub.load('./yolov5', 'custom', path='./weights/yolov5s.pt',source='local')  # local repo
        logging.info("load model success!")

    def _SysCheck(self, c=0):
        # 1、检测相机是否存在
        # 2、相机的参数
        # 3、在输出图片上面显示检测已完成
        cap = cv2.VideoCapture(c)
        if cap is None or not cap.isOpened():
            logging.error("camera is not available!")
        else:
            self.camera.is_active = True
            self.camera.width     = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.camera.height    = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.sys_status = 2 
            cap.release()
        logging.info("Meta system status:{}".format(self.sys_status))


    def _SysWork(self):
        pass

    def _read_cfg(self, cfg):
        with open(cfg, 'r') as f:
            dic = yaml.safe_load(f)
            return self.MetaDic.update(dic)


