#include "solution.h"

unsigned int challenges::greatest_common_divisor(unsigned int a, unsigned int b)
{
    unsigned int larger =  (a < b ? b : a);
    unsigned int smaller = (a < b ? a : b);

    unsigned int remainder = larger % smaller;

    if(remainder == 0) return smaller;

    return challenges::greatest_common_divisor(remainder, smaller);
}