#include "rclcpp/rclcpp.hpp"
#include "ledtank_ros2_driver_msg/msg/motor_value.hpp"

namespace ledtank_motor_driver
{

class MotorDriver : public rclcpp::Node
{
public:
  MotorDriver(const rclcpp::NodeOptions & options);

private:
  rclcpp::Subscription<ledtank_ros2_driver_msg::msg::MotorValue>::SharedPtr sub_;

  void changeMotorValue(const ledtank_ros2_driver_msg::msg::MotorValue::SharedPtr msg);
};
}
