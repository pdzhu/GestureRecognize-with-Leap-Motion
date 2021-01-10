# coding=utf-8
import sys
import Leap
import time
import pandas as pd
import glob

data = [[] for _ in range(61)]  # 一共61个，29+29+3
init_time = time.time()


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

        data[26].append(leftHand.palm_width)

        data[27].append(leftHand.sphere_radius)

        data[28].append(leftHand.stabilized_palm_position[0])
        data[29].append(leftHand.stabilized_palm_position[1])
        data[30].append(leftHand.stabilized_palm_position[2])

        #
        # 右手
        data[31].append(rightHand.palm_normal.yaw * Leap.RAD_TO_DEG)
        data[32].append(rightHand.palm_normal.pitch * Leap.RAD_TO_DEG)
        data[33].append(rightHand.palm_normal.roll * Leap.RAD_TO_DEG)

        #
        #  手掌位置  x  y  z   可考虑stabilized_palm_position
        data[34].append(rightHand.palm_position[0])
        data[35].append(rightHand.palm_position[1])
        data[36].append(rightHand.palm_position[2])

        #  手掌速度  x y z
        data[37].append(rightHand.palm_velocity[0])
        data[38].append(rightHand.palm_velocity[1])
        data[39].append(rightHand.palm_velocity[2])

        # 指尖位置  x y z
        data[40].append(rightHand.fingers[0].joint_position(3)[0])
        data[41].append(rightHand.fingers[0].joint_position(3)[1])
        data[42].append(rightHand.fingers[0].joint_position(3)[2])

        data[43].append(rightHand.fingers[1].joint_position(3)[0])
        data[44].append(rightHand.fingers[1].joint_position(3)[1])
        data[45].append(rightHand.fingers[1].joint_position(3)[2])

        data[46].append(rightHand.fingers[2].joint_position(3)[0])
        data[47].append(rightHand.fingers[2].joint_position(3)[1])
        data[48].append(rightHand.fingers[2].joint_position(3)[2])

        data[49].append(rightHand.fingers[3].joint_position(3)[0])
        data[50].append(rightHand.fingers[3].joint_position(3)[1])
        data[51].append(rightHand.fingers[3].joint_position(3)[2])

        data[52].append(rightHand.fingers[4].joint_position(3)[0])
        data[53].append(rightHand.fingers[4].joint_position(3)[1])
        data[54].append(rightHand.fingers[4].joint_position(3)[2])

        data[55].append(rightHand.palm_width)

        data[56].append(rightHand.sphere_radius)

        data[57].append(rightHand.stabilized_palm_position[0])
        data[58].append(rightHand.stabilized_palm_position[1])
        data[59].append(rightHand.stabilized_palm_position[2])

        data[60].append(2)   # 结果


def main():
    # Create a sample listener and controller
    listener = SimpleListener()
    controller = Leap.Controller()
    print "Press Enter to quit..."

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


if __name__ == "__main__":
    main()

    df = pd.DataFrame(data=data)
    df = df.transpose()

    # df.to_csv("../temp/%s.csv" % (str(1)), sep=',', index=False, header=False)
    # 获取当前文件夹下个数
    path_file_number = len(glob.glob(pathname='/home/pdzhu/GestureRecognitionSourceFiles/temp/*.csv'))
    print path_file_number
    df.to_csv("../temp/%s.csv" % (str(path_file_number + 1)), sep=',', index=False, header=False)

