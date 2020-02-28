#include "solution.h"

#include <cmath>

int Arge::nbYear(int p0, double percent, int aug, int p)
{
  double perc = 1.0 + (percent / 100.0);
  int years = 0;
  int pop = p0;
  while(pop < p) {
      ++years;
      pop = pop * perc + aug;
  }

  return years;
}
