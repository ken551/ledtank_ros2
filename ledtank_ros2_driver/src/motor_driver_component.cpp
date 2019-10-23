#include "ledtank_ros2_driver/motor_driver_component.hpp"

#include <chrono>
#include <memory>
#include <wiringPi.h>
#include <softPwm.h>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

namespace ledtank_motor_driver
{

MotorDriver::MotorDriver(const rclcpp::NodeOptions & options)
: Node("ledtank_motor_driver", options)
{
	wiringPiSetup();
    wiringPiSetupGpio();
    softPwmCreate(13,0,100);
    softPwmCreate(19,0,100);
    softPwmCreate(5,0,100);
    softPwmCreate(6,0,100);
 	sub_ = this->create_subscription<ledtank_ros2_driver_msg::msg::MotorValue>(
    "ledtank_motor_value", 10, std::bind(&MotorDriver::changeMotorValue, this, _1));
}

void MotorDriver::changeMotorValue(const ledtank_ros2_driver_msg::msg::MotorValue::SharedPtr msg)
{
	RCLCPP_INFO(this->get_logger(), "Change Motor Value");
	int rightDuty = msg->right_value;
	int leftDuty = msg->left_value;

	if(rightDuty >= 100) {
		rightDuty = 100;
	} else if(rightDuty <= -100) {
		rightDuty = -100;
	}
	if(leftDuty >= 100) {
		leftDuty = 100;
	} else if(leftDuty <= -100) {
		leftDuty = -100;
	}
	if (leftDuty>= 0) {
		softPwmWrite(13,leftDuty);
		softPwmWrite(19,0);
	} else {
		softPwmWrite(13,0);
		softPwmWrite(19,-leftDuty);
	}
	if (rightDuty>= 0) {
		softPwmWrite(5,rightDuty);
		softPwmWrite(6,0);
	} else {
		softPwmWrite(5,0);
		softPwmWrite(6,-rightDuty);
	}
}

}


// 動的にコンポーネントノードをロードできるために登録する
#include "rclcpp_components/register_node_macro.hpp"
RCLCPP_COMPONENTS_REGISTER_NODE(ledtank_motor_driver::MotorDriver)
