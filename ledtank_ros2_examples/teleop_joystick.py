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
from rclpy.node import Node
from ledtank_ros2_driver_msg.msg import MotorValue
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import sys, select, termios, tty

class JoyListener(Node):

    def __init__(self):
        super().__init__("teleop_joystick")
        self.pub = self.create_publisher(MotorValue, "ledtank_motor_value")
        self.create_subscription(Joy,"joy",self.callback)
        self.old_left = 0
        self.old_right = 0

    def callback(self,msg):
        print("hoge")
        left=int(msg.axes[1]*100)
        left=self.shapeValue(left)
        right=int(msg.axes[2]*100)
        right=self.shapeValue(right)
        if self.old_left != left or self.old_right != right :
            msg = MotorValue()
            msg.left_value = left
            msg.right_value = right
            self.pub.publish(msg)
            self.old_left = left
            self.old_right = right
        print(left)
        print("piko")
        print(right)

    def shapeValue(self,value):
        if value > 100:
            return 100
        if value < -100:
            return -100
        else:
            return value
 
def main():
    rclpy.init()
    node = JoyListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()
