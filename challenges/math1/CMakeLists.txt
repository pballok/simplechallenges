add_executable(solution_math1
  solution1.cpp
  math1_tests.cpp
)

target_include_directories(solution_math1
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(solution_math1
  catch2
)
