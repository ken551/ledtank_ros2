cmake_minimum_required(VERSION 3.5)
project(ledtank_ros2_driver)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(ledtank_ros2_driver_msg REQUIRED)

include_directories(include)

add_library(motor_driver_component SHARED src/motor_driver_component.cpp)
ament_target_dependencies(motor_driver_component
  rclcpp
  rclcpp_components
  ledtank_ros2_driver_msg
  )
find_library(wiringPi_LIB wiringPi)
target_link_libraries(motor_driver_component ${wiringPi_LIB})
rclcpp_components_register_nodes(motor_driver_component "ledtank_ros2_driver::MotorDriver")

ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_dependencies(rclcpp_components)
ament_export_dependencies(greeting_msg)

ament_export_include_directories(include)

ament_export_libraries(motor_driver_component)

add_executable(motor_driver src/motor_driver.cpp)
ament_target_dependencies(motor_driver rclcpp ledtank_ros2_driver_msg)

target_link_libraries(motor_driver motor_driver_component)

install(DIRECTORY
  include/ledtank_ros2_driver
  DESTINATION include
  )

install(TARGETS
  motor_driver_component
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

install(TARGETS
  motor_driver
  DESTINATION lib/${PROJECT_NAME}
)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
