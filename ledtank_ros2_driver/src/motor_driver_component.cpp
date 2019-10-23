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
 	sub_ = this->create_subscription<ledtank_ros2_driver_msg::msg::MotorValue>(
    "ledtank_motor_value", 10, std::bind(&MotorDriver::changeMotorValue, this, _1));
}

void MotorDriver::changeMotorValue(const ledtank_ros2_driver_msg::msg::MotorValue::SharedPtr msg)
{
	RCLCPP_INFO(this->get_logger(), "Change Motor Value");
	float duty = msg->left_value;
	if(duty >= 100) {
		duty = 100;
	} else if(duty <= -100) {
		duty = -100;
	}
	if (duty>= 0) {
		softPwmWrite(13,duty);
		softPwmWrite(19,0);
	} else {
		softPwmWrite(13,0);
		softPwmWrite(19,-duty);
	}
}

}


// 動的にコンポーネントノードをロードできるために登録する
//RCLCPP_COMPONENTS_REGISTER_NODE(ledtank_motor_driver::MotorDriver);
