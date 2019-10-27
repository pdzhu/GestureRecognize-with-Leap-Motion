# coding=utf-8
import sys
import Leap
import time
import pandas as pd

data = [[] for _ in range(26)]  # 12这个数字可以改,表示有几个参数
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

        print leftHand.fingers[1].joint_position(3)
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
    df.to_csv("./CSV_la/%s.csv" % (str(3)), sep=',', index=False, header=False)

