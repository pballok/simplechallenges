cmake_minimum_required(VERSION 2.8)

project(codewars CXX)

add_executable(gradebook
  gradebook/solution.cpp
  gradebook/test.cpp
)

target_include_directories(gradebook
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_test(
  NAME gradebook_test
  COMMAND gradebook
)
