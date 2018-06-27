#include "solution.h"

unsigned long sum_of_sequence_divisible_by_n(unsigned int n, unsigned int limit) {
    return (n == 0 || limit < n ? 0 :
                                  (((1 + (limit / n)) * (limit / n)) / 2) * n);
}

unsigned long challenges::sum_of_integers_divisible_by_3_or_5(unsigned int limit)
{
    return sum_of_sequence_divisible_by_n(3, limit) + 
           sum_of_sequence_divisible_by_n(5, limit) - 
           sum_of_sequence_divisible_by_n(15, limit);
}
