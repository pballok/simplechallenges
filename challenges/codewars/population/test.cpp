#define CATCH_CONFIG_MAIN

#include "solution.h"
#include "catch2/catch.hpp"

SCENARIO("Population test", "[Population]")
{
  GIVEN("Basic population tests") {
    THEN("tests must pass.") {
      REQUIRE(Arge::nbYear(1500, 5, 100, 5000) == 15);
      REQUIRE(Arge::nbYear(1500000, 2.5, 10000, 2000000) == 10);
      REQUIRE(Arge::nbYear(1500000, 0.25, 1000, 2000000) == 94);
      REQUIRE(Arge::nbYear(1500000, 0.25, -1000, 2000000) == 151);
    }
  }
}
