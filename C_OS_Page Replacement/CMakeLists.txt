cmake_minimum_required(VERSION 3.20)
project(C_OS_Page_Replacement C)

set(CMAKE_C_STANDARD 99)

add_executable(C_OS_Page_Replacement FIFO.c LRU.cpp)
