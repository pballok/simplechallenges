#include "solution.h"

unsigned long sum_of_sequence_divisible_by_n(unsigned int n, unsigned int limit) {
    if(limit < n) return 0;

    unsigned int last_number = limit / n;
    return ((1 + last_number) * last_number * n) / 2;
}

unsigned long challenges::sum_of_integers_divisible_by_3_or_5(unsigned int limit)
{
    return sum_of_sequence_divisible_by_n(3, limit) + 
           sum_of_sequence_divisible_by_n(5, limit) - 
           sum_of_sequence_divisible_by_n(15, limit);
}
