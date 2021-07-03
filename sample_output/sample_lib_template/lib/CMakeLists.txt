cmake_minimum_required(VERSION 3.1)
project(sample_lib_templateLib VERSION 0.0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#conan
if (NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/memsharded/cmake-conan")
    file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake" "${CMAKE_BINARY_DIR}/conan.cmake")
endif ()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run(CONANFILE conanfile.py BASIC_SETUP NO_OUTPUT_DIRS CMAKE_TARGETS BUILD missing)

include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
file(GLOB_RECURSE source src/*)
add_library(${PROJECT_NAME} SHARED ${source})
conan_target_link_libraries(${PROJECT_NAME})
target_include_directories(${PROJECT_NAME} PUBLIC include)