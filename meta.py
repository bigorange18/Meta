import sys
import cv2
import time
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox,QMainWindow,QFileDialog,QDialog,QScrollArea,QLabel
from PySide6.QtWidgets import QMainWindow, QDialog, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QCursor, QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from window.login_ui import Ui_Dialog
from window.MateWin_ui import Ui_MainWindow
from lib.Windows import Windows
from src.video_detect import PPE_detect
from src.MetaSystem import MetaSystem
# 继承QWidget类，以获取其属性和方法
class LoginWindow(QWidget, Ui_Dialog):
    '''登录界面处理窗口'''
    def __init__(self, win_width=500):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("登录界面")
        # 调整窗口位置
        qr = self.frameGeometry()
        screen_w = QApplication.primaryScreen().size().width()
        screen_h = QApplication.primaryScreen().size().height()
        win_w = self.frameGeometry().getRect()[2]
        win_h = self.frameGeometry().getRect()[3]
        self.win_x = (screen_w - win_w) / 2
        self.win_y = (screen_h - win_h) / 2
        self.move(self.win_x, self.win_y)
        self.setupUi(self)
        # 登录
        self.login_button.clicked.connect(self.login_botton_clicked)
        # 取消
        self.login_fail.clicked.connect(self.closewin)

    def login_botton_clicked(self):
        #! todo
        msg = QMessageBox.clickedButton(QMessageBox())
        username = self.login_name.text().strip()
        password = self.login_password.text().strip()
        print(username, password)
        print("button clicked")
        # 关闭当前页面,打开Meta处理界面
        Windows.MetaWin = MateWindow()
        Windows.MetaWin.show()
        self.hide()
        # 清空密码
        self.login_password.setText("")


    def loadVideo(self):
        # self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0])) # 选取视频文件
        pass



    def closewin(self):
        return self.close()

class MateWindow(QMainWindow,Ui_MainWindow):
    '''Meta处理窗口
    @b:QPushButton
    @lab:QLabel
    @l: listWidget
    '''
    def __init__(self, parent=None):
        super().__init__()
        """
        1、参数配置
        2 硬件检测
        3、窗口设置
        """
        self.meta = MetaSystem()
        screen_w = QApplication.primaryScreen().size().width()
        screen_h = QApplication.primaryScreen().size().height()
        win_w = self.frameGeometry().getRect()[2]
        win_h = self.frameGeometry().getRect()[3]
        self.win_x = (screen_w/2 - win_w)
        self.win_y = (screen_h/2 - win_h) 
        self.cap = None
        self.move(self.win_x, self.win_y)
        self.setupUi(self)
        self.botton_bind()
        self.show()

    def back2login(self):
        print("button clicked")
        self.close()
        # Windows.LoginWin.show()


    def msg_print(self):
        pass

    def palyvideo(self):
        pass

    def getPng(self,fileName):
        """
        获取PNG图像
        @return numpy array 
        """
        overlay = cv2.imread(fileName)
        # overlay = cv2.cvtColor(overlay,cv2.COLOR_RGB2BGR)
        overlay = cv2.resize(overlay,(0,0), fx=0.3, fy=0.3)
        return overlay


    def get_iou(self,boxA, boxB):
        """
        计算两个框的IOU

        @param: boxA,boxB list形式的框坐标
        @return: iou float 
        """
        boxA = [int(x) for x in boxA]
        boxB = [int(x) for x in boxB]

        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

        iou = interArea / float(boxAArea + boxBArea - interArea)

        return iou
    def get_person_info_list(self,person_list,hat_list,vest_list):
        """
        获取每个人的完整信息
        
        @param: person_list,hat_list,vest_list numpy array
        @return  person_info_list list
        """
        hat_iou_thresh = 0
        vest_iou_thresh = 0

        person_info_list = []

        for person in person_list:
            person_info_item = [[],[],[]]
            # 人体框
            person_box = person[:5]
            
            person_info_item[0]= person_box
            # 依次与帽子计算IOU
            for hat in hat_list:
                hat_box = hat[:6]
                hat_iou = self.get_iou(person_box, hat_box)
                
                if hat_iou > hat_iou_thresh:
                    person_info_item[1] = hat_box
                    break
                    
            # 依次与防护服计算IOU
            for vest in vest_list:
                vest_box = vest[:5]
                vest_iou = self.get_iou(person_box, vest_box)

                
                if vest_iou > vest_iou_thresh:
                    person_info_item[2] = vest_box
                    break

            person_info_list.append(person_info_item)
        
        return person_info_list


    def display_camera(self):
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
            print(person_list)
            #遍历每个人，渲染相应数据
            for person_box in person_list:
                p_l,p_t,p_r,p_b = person_box[:4]
                p_l,p_t,p_r,p_b = int(p_l),int(p_t),int(p_r),int(p_b)
                conf = person_box[4]
                conf_txt =str(round(conf*100,1) ) + '%'
                cv2.rectangle(frame,(p_l,p_t),(p_r,p_b),(0,255,0),5)
                cv2.putText(frame,conf_txt,(p_l,p_t-35),cv2.FONT_ITALIC,1,(0,255,0),2)  
            end_time = time.time()
            fps_text = 1/(end_time - start_time)
            cv2.putText(frame,'FPS: '+ str(round(fps_text,2)),(30,50),cv2.FONT_ITALIC,1,(0,255,0),2)
            cv2.putText(frame,'Person: '+ str(len(person_list)),(30,100),cv2.FONT_ITALIC,1,(0,255,0),2)
            frame_2_pixmap = QImage(frame.data, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888).rgbSwapped()
            self.lab_img.setPixmap(QPixmap.fromImage(frame_2_pixmap))
            cv2.imshow('demo',frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        pass


    def botton_bind(self):
        # 选择文件
        self.b_filename.clicked.connect(self.select_file)
        # 退出
        self.a_Exit.triggered.connect(self.closewin)

        # 
        self.b_start.clicked.connect(self.display_camera)
        # 停止
        self.b_end.clicked.connect(self.detect_stop)

        # 
        self.l_fuction.currentItemChanged.connect(self.display_function_page)

    def display_function_page(self,current, previous):
        print(self.l_fuction.currentIndex().row(),self.l_fuction.currentItem().text())
        return self.stackedWidget.setCurrentIndex(self.l_fuction.currentIndex().row())


    def select_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self,dir="./Mate/img", filter="*.jpg; *.png; *.jpeg")
        if self.file_path:
            self.lab_img.setPixmap(QPixmap(self.file_path))
            # self.lab_img.setScaledContents(True)
            self.b_filename.setText(self.file_path)

    def detect_stop(self):
        self.meta.sys_status = 2
        if self.cap is not None:
            self.cap.release()


    def closewin(self):
        return self.close()

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    
    # qtmodern.styles.dark(app)
    # 初始化并展示我们的界面组件
    Windows.LoginWin = MateWindow()
    Windows.LoginWin.show() 
    # 结束QApplication
    sys.exit(app.exec())
    
