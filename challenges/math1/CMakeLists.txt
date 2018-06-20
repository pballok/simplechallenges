add_executable(math1_solution_suggested
  solution1.cpp
  math1_tests.cpp
)

target_include_directories(math1_solution_suggested
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(math1_solution_suggested
  catch2
)

add_test(
  name    math1_solution_suggested
)



add_executable(math1_solution_fast
  solution2.cpp
  math1_tests.cpp
)

target_include_directories(math1_solution_fast
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(math1_solution_fast
  catch2
)

add_test(
  name    math1_solution_fast
)