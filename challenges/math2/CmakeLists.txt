add_executable(math2_solution_euclidean
  solution1.cpp
  math2_tests.cpp
)

target_include_directories(math2_solution_euclidean
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(math2_solution_euclidean
  catch2
)

add_test(
  NAME    Euclidean
  COMMAND math2_solution_euclidean
)
