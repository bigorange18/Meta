import cv2, time
import yaml
from lib.general import check_git_status
from lib.general import get_camera_status
from src.safe_detect import SafeDetect
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
            4: 
        """
        # 1.检测本地代码与git仓库代码
        self.MetaDic = dict()
        self.read_cfg(cfg)
        check_git_status(self.MetaDic["git-repo"]["repo"], self.MetaDic["git-repo"]["branch"])
        self.cameraparam = get_camera_status()
        self.status = 0
        self.mate_0      = HandControlVolume()
        self.mate_1      = SafeDetect()
        self.RunCase = {
            0: self.mate_0,  
            1: self.mate_1  
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
        print("系统状态已经检测完成status:{}".format(self.status))
        pass

    def MetaProj(self):
        # 在运行时候,在5s内选择需要执行的项目
        # 超过3s后，默认执行手势拖动方块任务
        start_time = time.time()
        cur_time = time.time()
        project_infos = {
            0: "手势拖转方框娱乐项目,祝您玩的开心!!!"
        }
        # while 1:
        #     cur_time = time.time()

        #     if (cur_time - start_time) > 3:
        #         fun_case = 0
        #         break
        print("请输入需要运行的项目:")
        # fun_case = int(input())
        print("您需要参与的项目为:{}".format(project_infos[0]))
        print("按ESC键退出")
        # self.select_proj = self.RunCase[fun_case]

    def MetaRun(self):
        print("111")
        self.mate_0.Run()


    def read_cfg(self, cfg):
        with open(cfg, 'r') as f:
            dic = yaml.safe_load(f)
            return self.MetaDic.update(dic)


