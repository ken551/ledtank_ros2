
#include <rclcpp/rclcpp.hpp>
#include <memory>

#include "ledtank_ros2_driver/motor_driver_component.hpp"

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::NodeOptions options;
  rclcpp::spin(std::make_shared<ledtank_motor_driver::MotorDriver>(options));
  rclcpp::shutdown();
  return 0;
}