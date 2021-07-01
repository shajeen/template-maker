
cmake_minimum_required(VERSION 3.1.3)
project(example CXX)

# Download automatically, you can also just copy the conan.cmake file
if(NOT EXISTS "${CMAKE_CURRENT_BINARY_DIR}/conan.cmake")
   message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
   file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
                  "${CMAKE_CURRENT_BINARY_DIR}/conan.cmake")
endif()
include(${CMAKE_CURRENT_BINARY_DIR}/conan.cmake)
conan_cmake_run(CONANFILE conanfile.txt
                BASIC_SETUP CMAKE_TARGETS
                BUILD missing)

file(GLOB INC ${PROJECT_SOURCE_DIR}/src/*.h)
file(GLOB SRC ${PROJECT_SOURCE_DIR}/src/*.cpp)
add_executable(${PROJECT_NAME} ${INC} ${SRC})
conan_target_link_libraries(${PROJECT_NAME})
target_link_libraries(${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 17)
