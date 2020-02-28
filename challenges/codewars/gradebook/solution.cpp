#include "solution.h"

char getGrade(int a, int b, int c) {
  int score = (a + b + c) / 3;

  if(score < 60) return 'F';
  if(score < 70) return 'D';
  if(score < 80) return 'C';
  if(score < 90) return 'B';
  return 'A';
}
