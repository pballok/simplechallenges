add_executable(test_math1_suggested
  solution1.cpp
  math1_tests.cpp
)

target_include_directories(test_math1_suggested
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(test_math1_suggested
  catch2
)

add_test(
  NAME    Suggested
  COMMAND test_math1_suggested
)



add_executable(test_math1_fast
  solution2.cpp
  math1_tests.cpp
)

target_include_directories(test_math1_fast
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(test_math1_fast
  catch2
)

add_test(
  NAME    Fast
  COMMAND test_math1_fast
)



add_executable(test_math1_recursive
  solution3.cpp
  math1_tests.cpp
)

target_include_directories(test_math1_recursive
  PRIVATE ${CATCH2_INCLUDE_DIR}
)

add_dependencies(test_math1_recursive
  catch2
)

add_test(
  NAME    Recursive
  COMMAND test_math1_recursive
)