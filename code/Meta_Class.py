import cv2, time
from code.finger_gesture_drag_block import finger_gesture_drag_block

class MetaSystem(object):
    '''
    status
        0: 系统未开始工作
        1: 系统进入自检状态
        2: 系统状态无问题
        3: 系统进入工作状态
        4: 
    
    '''
    def __init__(self) -> None:
        self.status = 0
        self.cameraparam = CameraParam()
        self.RunCase = {
            0: finger_gesture_drag_block    
        }

    def _SysCheck(self):
        # 1、检测相机是否存在
        # 2、相机的参数
        # 3、在输出图片上面显示检测已完成
        self.status = 1
        try:
            cap = cv2.VideoCapture(0)
        except:
            print("未检出到相机")
            exit(0)
            # img宽高
        img_width =int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        img_high = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.cameraparam.img_high = img_high
        self.cameraparam.img_width = img_width

        cap.release()

        self.status = 2 
        pass

    def MetaProj(self):
        # 在运行时候,在5s内选择需要执行的项目
        # 超过3s后，默认执行手势拖动方块任务
        start_time = time.time()
        cur_time = time.time()

        while 1:
            cur_time = time.time()

            if (cur_time - start_time) > 3:
                fun_case = 0
                break
        self.select_proj = self.MetaProj[fun_case]

    def MetaRun(self):
        self.select_proj.Run(self)


class CameraParam():
    def __init__(self) -> None:
        self.img_width = 0
        self.img_high = 0
        self.hz        = 0    
