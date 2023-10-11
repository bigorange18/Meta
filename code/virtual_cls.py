import cv2
from code.finger_gesture_drag_block import *

class VirSys(object):
    '''
    _init
        0: 系统未开始工作
        1: 系统进入自检状态
        2: 系统状态无问题
        3: 系统进入工作状态
        4: 
    
    '''
    def __init__(self) -> None:
        self._init = 0

    def _SysCheck(self):
        # 1、检测相机是否存在
        # 2、相机的参数
        # 3、在输出图片上面显示检测已完成
        pass




class CameraParam():
    def __init__(self) -> None:
        self.img_width = 0
        self.img_higth = 0
        self.hz        = 0    
