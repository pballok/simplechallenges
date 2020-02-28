cmake_minimum_required(VERSION 3.10)

project(interview_1 CXX)

set(SOURCES
  AnalogClock.cpp
)

set(HEADERS
  AnalogClock.h
)

add_executable(${PROJECT_NAME}
  main.cpp
  ${SOURCES}
  ${HEADERS}
)

set(TEST_SOURCES
  AnalogClockTest.cpp
)

add_executable(AnalogClockTest
  ${TEST_SOURCES}
  ${SOURCES}
  ${HEADERS}
)

target_include_directories(AnalogClockTest
  PRIVATE ${CATCH2_INCLUDE_DIR}
)


enable_testing()

add_test(
  NAME AnalogClockTest
  COMMAND AnalogClockTest
)
