#define CATCH_CONFIG_MAIN

#include "solution.h"
#include "catch2/catch.hpp"

SCENARIO("Gradebook test", "[Gradebook]")
{
  GIVEN("Average score above 89") {
    THEN("grade must be 'A'") {
      REQUIRE(getGrade(95, 90, 93) == 'A');
      REQUIRE(getGrade(100, 85, 96) == 'A');
      REQUIRE(getGrade(92, 93, 94) == 'A');
    }
  }

  GIVEN("Average score between 80 and 89") {
    THEN("grade must be 'B'") {
      REQUIRE(getGrade(70, 70, 100) == 'B');
      REQUIRE(getGrade(82, 85, 87) == 'B');
      REQUIRE(getGrade(84, 79, 85) == 'B');
    }
  }

  GIVEN("Average score between 70 and 79") {
    THEN("grade must be 'C'") {
      REQUIRE(getGrade(70, 70, 70) == 'C');
      REQUIRE(getGrade(75, 70, 79) == 'C');
      REQUIRE(getGrade(60, 82, 76) == 'C');
    }
  }

  GIVEN("Average score between 60 and 69") {
    THEN("grade must be 'D'") {
      REQUIRE(getGrade(65, 70, 59) == 'D');
      REQUIRE(getGrade(66, 62, 68) == 'D');
      REQUIRE(getGrade(58, 62, 70) == 'D');
    }
  }

  GIVEN("Average score below 60") {
    THEN("grade must be 'F'") {
      REQUIRE(getGrade(44, 55, 52) == 'F');
      REQUIRE(getGrade(48, 55, 52) == 'F');
      REQUIRE(getGrade(58, 59, 60) == 'F');
      REQUIRE(getGrade(0, 0, 0) == 'F');
    }
  }
}
