import cv2
import numpy as np
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

hands =  mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)




class finger_gesture_drag_block():
    '''
    @s_x,s_y,s_w:初始时方块在图像上的像素点位置
    '''
    def __init__(self,s_x=100,s_y=100,s_w=100) -> None:
        self.s_x = s_x
        self.s_y = s_y
        self.s_w = s_w
        pass


def main():


    square_x, square_y, square_width = 100, 100, 100
    square_isactivate = False
    square_color = (255,0,0)
    cap = cv2.VideoCapture(0)

    # img宽高
    img_width =int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    img_high = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    while True:
        res, frame = cap.read()
        frame = cv2.flip(frame, 1)

        frame.flags.writeable=False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame)

        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # 判断是否出现双手
        if result.multi_hand_landmarks:
            # 遍历每双手
            for hands_landmark in result.multi_hand_landmarks:
                # 绘制21个关键点
                mp_drawing.draw_landmarks(
                    frame,
                    hands_landmark,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                # 保存食指点坐标
                hand_x_list = []
                hand_y_list = []
                for hand in hands_landmark.landmark:
                    hand_x_list.append(hand.x)
                    hand_y_list.append(hand.y)
                index_finger_x = int(hand_x_list[8] * img_width)
                index_finger_y = int(hand_y_list[8] * img_high)

                middle_finger_x = int(hand_x_list[12] * img_width)
                middle_finger_y = int(hand_y_list[12] * img_high)

                finger_dis = np.linalg.norm([index_finger_x-middle_finger_x,index_finger_y-middle_finger_y])
                print(finger_dis)
            if finger_dis < 30:
                if (index_finger_x > square_x) and (index_finger_x < square_x+square_width) and \
                (index_finger_y > square_y) and (index_finger_y < square_y+square_width):
                    if not square_isactivate:
                        l1 = index_finger_x - square_x
                        l2 = index_finger_y - square_y
                        square_isactivate = True
                        square_color = (255,255,0)
            else:
                square_isactivate = False
                square_color = (0,255,0)
            if square_isactivate:
                square_x = index_finger_x - l1
                square_y = index_finger_y - l2
        cv2.circle(frame,(index_finger_x,index_finger_y),radius=10,color=(0,255,255), thickness=-1)
        overlay = frame.copy()

        cv2.rectangle(frame, (square_x, square_y), (square_x+square_width, square_y+square_width),color=square_color,thickness=-1)
        frame = cv2.addWeighted(overlay, 0.5, frame, 1 - 0.5, 0)
        
        cv2.imshow("Virtual Img", frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break
    pass

    cap.release()

if __name__=="__main__":
    main()