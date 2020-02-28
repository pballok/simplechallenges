cmake_minimum_required(VERSION 2.8)

project(codewars CXX)

# -- gradebook --
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


# -- population --
add_executable(population
  population/solution.cpp
  population/test.cpp
)

target_include_directories(population
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_test(
  NAME population_test
  COMMAND population
)
