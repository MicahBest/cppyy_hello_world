cmake_minimum_required(VERSION 3.12)
project(HelloCppyy)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add library
add_library(hello SHARED src/hello.cpp)

# Set the output name to "hello.so" without "lib" prefix
set_target_properties(hello PROPERTIES PREFIX "" OUTPUT_NAME "hello")

# Include the directory containing header files (optional if headers are in the same directory)
target_include_directories(hello PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
