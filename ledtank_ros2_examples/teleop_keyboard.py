# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
import rclpy
from ledtank_ros2_driver_msg.msg import MotorValue
from std_msgs.msg import String
import sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


 
 
def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('teleop_keyboard')
    publisher = node.create_publisher(MotorValue, 'ledtank_motor_value')
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    msg = MotorValue()
    msg.left_value = 0
    msg.right_value = 0
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    print('hogepiko!')
    i=0
    while True: 
        try:  
            key = sys.stdin.read(1)
            if key == 'w':
                msg.left_value = 90
                msg.right_value = 90
            if key == 's':
                msg.left_value = -90
                msg.right_value = -90
            if key == 'a':
                msg.left_value = 0
                msg.right_value = 90
            if key == 'd':
                msg.left_value = 90
                msg.right_value = 0
            if key == 'e':
                msg.left_value = 0
                msg.right_value = 0
            if key == 'q':
                break
            publisher.publish(msg)
        except:
            import traceback
            traceback.print_exc()
            break
    print('end!')
    termios.tcsetattr(fd, termios.TCSANOW, old)

    node.destroy_node()
    rclpy.shutdown()

 
 
if __name__ == '__main__':
    main()