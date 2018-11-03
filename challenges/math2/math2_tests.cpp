#include "solution.h"

#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

SCENARIO("Calculate GCD of two numbers where the first number is larger than the second number", "[Math2]")
{
    GIVEN("Two numbers 12 and 8") {
        unsigned long result = challenges::greatest_common_divisor(12, 8);

        THEN("The Greatest Common Divisor must be 4") {
            REQUIRE(result == 4);
        }
    }
}

SCENARIO("Calculate GCD of two numbers where the first number is smaller than the second number", "[Math2]")
{
    GIVEN("Two numbers 45 and 255") {
        unsigned long result = challenges::greatest_common_divisor(45, 255);

        THEN("The Greatest Common Divisor must be 15") {
            REQUIRE(result == 15);
        }
    }
}

SCENARIO("Calculate GCD of two identical numbers", "[Math2]")
{
    GIVEN("Two numbers 16 and 16") {
        unsigned long result = challenges::greatest_common_divisor(16, 16);

        THEN("The Greatest Common Divisor must be 16") {
            REQUIRE(result == 16);
        }
    }
}

SCENARIO("Calculate GCD of two numbers where one number is divisor of other number", "[Math2]")
{
    GIVEN("Two numbers 80 and 40") {
        unsigned long result = challenges::greatest_common_divisor(80, 40);

        THEN("The Greatest Common Divisor must be 40") {
            REQUIRE(result == 40);
        }
    }
}
