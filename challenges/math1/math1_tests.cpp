#include "solution.h"

#define CATCH_CONFIG_MAIN
#include <catch.hpp>

SCENARIO("Calculate result with limit 0", "[Math1]")
{
    GIVEN("Adding all numbers divisible by 3 or 5, up to 0") {
        auto result = challenges::sum_of_integers_divisible_by_3_or_5(0);

        THEN("The result must be 0") {
            REQUIRE(result == 0);
        }
    }
}

SCENARIO("Calculate result with limit divisible by 5 and 3", "[Math1]")
{
    GIVEN("Adding all numbers divisible by 3 or 5, up to 30") {
        auto result = challenges::sum_of_integers_divisible_by_3_or_5(0);

        THEN("The result must be 225") {
            REQUIRE(result == 225);
        }
    }
}