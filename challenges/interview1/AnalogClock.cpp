#include "AnalogClock.h"

#include <iostream>

using HourHandDegrees = std::chrono::duration<double, std::ratio<3600, 30>>;  //3600 seconds is 30 degrees on the hour hand
using MinuteHandDegrees = std::chrono::duration<double, std::ratio<3600, 360>>; //3600 seconds is 360 degrees on the minute hand

AnalogClock::AnalogClock(std::chrono::seconds seconds_since_midnight)
  : minutes_since_midnight_(std::chrono::duration_cast<std::chrono::minutes>(seconds_since_midnight))
{
}

unsigned int AnalogClock::hourHandAngle() const
{
  auto degrees = static_cast<unsigned int>(HourHandDegrees(minutes_since_midnight_).count());
  return degrees % 360;
}

unsigned int AnalogClock::minuteHandAngle() const
{
  auto degrees = static_cast<unsigned int>(MinuteHandDegrees(minutes_since_midnight_).count());
  return degrees % 360;
}
