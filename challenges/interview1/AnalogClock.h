#ifndef ANALOG_CLOCK_H
#define ANALOG_CLOCK_H

#include <chrono>

class AnalogClock
{
public:
  explicit AnalogClock(std::chrono::seconds seconds_since_midnight);
  AnalogClock(const AnalogClock& other) = default;
  AnalogClock(AnalogClock&& other) = default;
  AnalogClock& operator=(const AnalogClock& other) = default;
  AnalogClock& operator=(AnalogClock&& other) = default;
  ~AnalogClock() = default;

  unsigned int hourHandAngle() const;
  unsigned int minuteHandAngle() const;

private:
  std::chrono::seconds minutes_since_midnight_;  //store elapsed whole minutes only
};

#endif // ANALOG_CLOCK_H
