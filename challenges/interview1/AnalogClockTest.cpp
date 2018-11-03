#define CATCH_CONFIG_MAIN

#include "AnalogClock.h"
#include "catch2/catch.hpp"

SCENARIO("Time within 24 hours", "[AnalogClock]")
{
  GIVEN("Time is exactly midnight") {
    AnalogClock ac(std::chrono::seconds(0));

    THEN("Both hands of the clock must be at 0 degrees") {
      REQUIRE(ac.hourHandAngle() == 0);
      REQUIRE(ac.minuteHandAngle() == 0);
    }
  }

  GIVEN("Time is 02:00") {
    AnalogClock ac(std::chrono::hours(2));

    THEN("Hour hand must be at 60 degrees, minute hand must be at 0") {
      REQUIRE(ac.hourHandAngle() == 60);
      REQUIRE(ac.minuteHandAngle() == 0);
    }
  }

  GIVEN("Time is 17:00") {
    AnalogClock ac(std::chrono::hours(17));

    THEN("Hour hand must be at 150 degrees, minute hand must be at 0") {
      REQUIRE(ac.hourHandAngle() == 150);
      REQUIRE(ac.minuteHandAngle() == 0);
    }
  }

  GIVEN("Time is 05:45") {
    AnalogClock ac(std::chrono::minutes(345));

    THEN("Hour hand must be at 172 degrees, minute hand must be at 270") {
      REQUIRE(ac.hourHandAngle() == 172);
      REQUIRE(ac.minuteHandAngle() == 270);
    }
  }

  GIVEN("Time is 15:37") {
    AnalogClock ac(std::chrono::minutes(937));

    THEN("Hour hand must be at 108 degrees, minute hand must be at 222") {
      REQUIRE(ac.hourHandAngle() == 108);
      REQUIRE(ac.minuteHandAngle() == 222);
    }
  }
}



SCENARIO("Time is outside of 24 hours", "[AnalogClock]")
{
  GIVEN("Time is 28:00") {
    AnalogClock ac(std::chrono::hours(28));

    THEN("Hour hand must be at 120 degrees, minute hand must be at 0") {
      REQUIRE(ac.hourHandAngle() == 120);
      REQUIRE(ac.minuteHandAngle() == 0);
    }
  }

  GIVEN("Time is 30:30") {
    AnalogClock ac(std::chrono::minutes(1830));

    THEN("Hour hand must be at 195 degrees, minute hand must be at 180") {
      REQUIRE(ac.hourHandAngle() == 195);
      REQUIRE(ac.minuteHandAngle() == 180);
    }
  }
}



SCENARIO("Interview examples", "[AnalogClock]")
{
  GIVEN("12345 seconds has passed") {
    AnalogClock ac(std::chrono::seconds(12345));

    THEN("Hour hand must be at 102 degrees, minute hand must be at 150") {
      REQUIRE(ac.hourHandAngle() == 102);
      REQUIRE(ac.minuteHandAngle() == 150);
    }
  }

  GIVEN("3600 seconds has passed") {
    AnalogClock ac(std::chrono::seconds(3600));

    THEN("Hour hand must be at 30 degrees, minute hand must be at 0") {
      REQUIRE(ac.hourHandAngle() == 30);
      REQUIRE(ac.minuteHandAngle() == 0);
    }
  }
}
