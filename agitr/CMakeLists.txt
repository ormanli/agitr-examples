cmake_minimum_required(VERSION 2.8.3)

project(agitr)

set(CATKIN_DEPS geometry_msgs rospy turtlesim std_srvs)
set(SYS_DEPS python-sys)

find_package(catkin REQUIRED COMPONENTS ${CATKIN_DEPS})

catkin_python_setup()

catkin_package(
    DEPENDS ${SYS_DEPS}
    CATKIN_DEPENDS ${CATKIN_DEPS}
)

catkin_install_python(PROGRAMS hello.py subpose.py pubvel.py count.py anon.py reverse_cmd_vel.py set_bg_color.py pubvel_with_max.py spawn_turtle.py pubvel_toggle.py
         DESTINATION ${CATKIN_PACKAGE_PYTHON_DESTINATION}
)