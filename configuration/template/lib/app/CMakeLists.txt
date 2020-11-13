cmake_minimum_required(VERSION 3.1.3)
project(exampleApp CXX)

add_executable(${PROJECT_NAME} main.cpp)
conan_target_link_libraries(${PROJECT_NAME})
target_link_libraries(${PROJECT_NAME} exampleLib)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 17)