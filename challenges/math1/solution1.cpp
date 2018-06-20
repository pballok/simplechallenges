#include "solution.h"

unsigned long challenges::sum_of_integers_divisible_by_3_or_5(unsigned int limit)
{
    unsigned long sum = 0;

    for(unsigned int i = 3; i <= limit; ++i) {
        if(i % 3 == 0) {
            sum += i;
        }
        else {
            if(i % 5 == 0) {
                sum += i;
            }
        }
    }

    return sum;
}