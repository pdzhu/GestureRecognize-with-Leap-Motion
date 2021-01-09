# coding=utf-8
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.utils import np_utils
import Leap
import tensorflow as tf
import os
import time
import sys


data = [[] for _ in range(50)]  # 12这个数字可以改,表示有几个参数
init_time = time.time()
previous_time = 0

# Load the model
model = load_model('/home/pdzhu/GestureRecognitionSourceFiles/src/model/model_test.h5')
print "Model Loaded"

gesture = ["Swipe Right", "Swipe Left"]
audio = ["aplay /home/pdzhu/GestureRecognitionSourceFiles/resource/3.wav",
         "aplay /home/pdzhu/GestureRecognitionSourceFiles/resource/4.wav",
         "aplay /home/pdzhu/GestureRecognitionSourceFiles/resource/5.wav",
         "aplay /home/pdzhu/GestureRecognitionSourceFiles/resource/6.wav"]

graph = tf.get_default_graph()


class SimpleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_frame(self, controller):

        frame = controller.frame()
        leftHand = frame.hand(0)
        rightHand = frame.hand(0)   # 赋初值   能否
        hand = frame.hands
        if not hand.is_empty:
            for h in hand:
                if h.is_left:
                    leftHand = h

                else:
                    rightHand = h

        data[0].append(frame.id)
        data[1].append(time.time() - init_time)
        # 手掌向下角度   -180 ~ 180
        data[2].append(leftHand.palm_normal.yaw * Leap.RAD_TO_DEG)
        data[3].append(leftHand.palm_normal.pitch * Leap.RAD_TO_DEG)
        data[4].append(leftHand.palm_normal.roll * Leap.RAD_TO_DEG)
        #
        #  手掌位置  x  y  z   可考虑stabilized_palm_position
        data[5].append(leftHand.palm_position[0])
        data[6].append(leftHand.palm_position[1])
        data[7].append(leftHand.palm_position[2])

        #  手掌速度  x y z
        #  palm_width   手掌宽度  后期可考虑去除手掌大小影响
        data[8].append(leftHand.palm_velocity[0])
        data[9].append(leftHand.palm_velocity[1])
        data[10].append(leftHand.palm_velocity[2])

        # 指尖位置  x y z
        data[11].append(leftHand.fingers[0].joint_position(3)[0])
        data[12].append(leftHand.fingers[0].joint_position(3)[1])
        data[13].append(leftHand.fingers[0].joint_position(3)[2])

        data[14].append(leftHand.fingers[1].joint_position(3)[0])
        data[15].append(leftHand.fingers[1].joint_position(3)[1])
        data[16].append(leftHand.fingers[1].joint_position(3)[2])

        data[17].append(leftHand.fingers[2].joint_position(3)[0])
        data[18].append(leftHand.fingers[2].joint_position(3)[1])
        data[19].append(leftHand.fingers[2].joint_position(3)[2])

        data[20].append(leftHand.fingers[3].joint_position(3)[0])
        data[21].append(leftHand.fingers[3].joint_position(3)[1])
        data[22].append(leftHand.fingers[3].joint_position(3)[2])

        data[23].append(leftHand.fingers[4].joint_position(3)[0])
        data[24].append(leftHand.fingers[4].joint_position(3)[1])
        data[25].append(leftHand.fingers[4].joint_position(3)[2])

        data[26].append(rightHand.palm_normal.yaw * Leap.RAD_TO_DEG)
        data[27].append(rightHand.palm_normal.pitch * Leap.RAD_TO_DEG)
        data[28].append(rightHand.palm_normal.roll * Leap.RAD_TO_DEG)

        #
        #  手掌位置  x  y  z   可考虑stabilized_palm_position
        data[29].append(rightHand.palm_position[0])
        data[30].append(rightHand.palm_position[1])
        data[31].append(rightHand.palm_position[2])

        #  手掌速度  x y z
        #  palm_width   手掌宽度  后期可考虑去除手掌大小影响
        data[32].append(rightHand.palm_velocity[0])
        data[33].append(rightHand.palm_velocity[1])
        data[34].append(rightHand.palm_velocity[2])

        # 指尖位置  x y z
        data[35].append(rightHand.fingers[0].joint_position(3)[0])
        data[36].append(rightHand.fingers[0].joint_position(3)[1])
        data[37].append(rightHand.fingers[0].joint_position(3)[2])

        data[38].append(rightHand.fingers[1].joint_position(3)[0])
        data[39].append(rightHand.fingers[1].joint_position(3)[1])
        data[40].append(rightHand.fingers[1].joint_position(3)[2])

        data[41].append(rightHand.fingers[2].joint_position(3)[0])
        data[42].append(rightHand.fingers[2].joint_position(3)[1])
        data[43].append(rightHand.fingers[2].joint_position(3)[2])

        data[44].append(rightHand.fingers[3].joint_position(3)[0])
        data[45].append(rightHand.fingers[3].joint_position(3)[1])
        data[46].append(rightHand.fingers[3].joint_position(3)[2])

        data[47].append(rightHand.fingers[4].joint_position(3)[0])
        data[48].append(rightHand.fingers[4].joint_position(3)[1])
        data[49].append(rightHand.fingers[4].joint_position(3)[2])


def main():
    # Create a sample listener and controller
    listener = SimpleListener()
    controller = Leap.Controller()
    print "Press Enter to start..."

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.add_listener(listener)

    # Keep this process running until Enter is pressed

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
    df_right = pd.DataFrame(data=data)
    df_right = df_right.transpose()
    ls = [num for num in range(0, len(df_right), 3)]

    df_right = df_right.loc()[ls]                  # 隔3帧提取一次    可考虑换eval函数

    print len(df_right)
    a = len(df_right)
    for n in range(a, 150):  # 插入一行
        df_right.loc[n * 3] = df_right.loc[a * 3 - 3]     # 运算速度还不够快

    x = df_right.iloc[:, 1:50].values
    with graph.as_default():
        y_pred = model.predict(np.reshape(x, (1, x.shape[0], x.shape[1])))
    pred = np.argmax(y_pred)
    # Eliminate the False Postives
    print y_pred
    print pred
    # if (y_pred[0][0] or y_pred[0][1]) >= 0.2:
    if y_pred[0][pred] >= 0.5:
        os.system(audio[pred])
    print y_pred[0][1]


if __name__ == "__main__":
    main()
