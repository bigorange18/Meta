import cv2, time
import yaml
from lib.general import check_git_status
from lib.general import get_camera_status
# from src.safe_detect import SafeDetect
# from src.finger_gesture_drag_block import HandControlVolume
from lib.classes import *
import torch
import time
import threading
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
        self.camera = Camera()
        self.sys_status = 0
        self._read_cfg(cfg)
        self._SysCheck()
        # 后台加载模型
        self.thread = threading.Thread(target=self.init_model, args=())
        self.thread.start()
        # check_git_status(self.MetaDic["git-repo"]["repo"], self.MetaDic["git-repo"]["branch"])

    def _detect(self):
        self.meta.model.conf = 0.3
        self.meta.sys_status = 3
        # 加载浮层
        self.overlay_person = self.getPng('./icons/person.png')
        self.overlay_vest = [
            self.getPng('./icons/vest_on.png'),
            self.getPng('./icons/vest_off.png')
        ]
        # 
        self.overlay_hat = [
            self.getPng('./icons/hat_blue.png'),
            self.getPng('./icons/hat_red.png'),
            self.getPng('./icons/hat_white.png'),
            self.getPng('./icons/hat_yellow.png'),
            self.getPng('./icons/hat_off.png'), # 最后一个不戴帽子
        ]
        self.color_hat = [(255,0,0),(0,0,255),(255,255,255),(0,255,255)]


        if self.meta.camera.is_active:
            cap = cv2.VideoCapture(0)
        while self.meta.sys_status ==3:
            ret,frame = cap.read()
            # 反转
            frame = cv2.flip(frame,1)
            # 转为RGB
            img_cvt = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # 记录推理耗时
            start_time = time.time()
            # 推理
            results = self.meta.model(img_cvt)
            pd = results.pandas().xyxy[0]
            

            person_list = pd[pd['name']=='person'].to_numpy()
            vest_list = pd[pd['name']=='vest'].to_numpy()
            hat_list = pd[pd['name'].str.contains('helmet')].to_numpy()

            #获取人员信息
            person_info_list = self.get_person_info_list(person_list,hat_list,vest_list)

            #遍历每个人，渲染相应数据
            self.render_frame(frame,person_info_list)
            end_time = time.time()
            fps_text = 1/(end_time - start_time)
            # cv2.putText(frame,'FPS: '+ str(round(fps_text,2)),(30,50),cv2.FONT_ITALIC,1,(0,255,0),2)
            # cv2.putText(frame,'Person: '+ str(len(person_info_list)),(30,100),cv2.FONT_ITALIC,1,(0,255,0),2)


            cv2.imshow('demo',frame)


            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()




    def init_model(self):
        self.model = torch.hub.load('./yolov5', 'custom', path='./weights/yolov5s.pt',source='local')  # local repo

    def _SysCheck(self, c=0):
        # 1、检测相机是否存在
        # 2、相机的参数
        # 3、在输出图片上面显示检测已完成
        cap = cv2.VideoCapture(c)
        if cap is None or not cap.isOpened():
            print('111')
            pass
        else:
            self.camera.is_active = True
            self.camera.width=int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.camera.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.sys_status = 2 
            cap.release()
        print("系统状态已经检测完成status:{}".format(self.sys_status))


    def _SysWork(self):
        pass

    def _read_cfg(self, cfg):
        with open(cfg, 'r') as f:
            dic = yaml.safe_load(f)
            return self.MetaDic.update(dic)


