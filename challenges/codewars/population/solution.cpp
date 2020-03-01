#include "solution.h"

#include <cmath>

int Arge::nbYear(int p0, double percent, int aug, int p)
{
  int years = 0;
  int pop = p0;
  percent = percent / 100.0;
  while(pop < p) {
      ++years;
      pop += pop * percent + aug;
  }

  return years;
}
