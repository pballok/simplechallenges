#include "solution.h"

unsigned long challenges::sum_of_integers_divisible_by_3_or_5(unsigned int limit)
{
    return (limit < 3 ? 0 :
                       challenges::sum_of_integers_divisible_by_3_or_5(limit - 1) + (limit % 3 == 0 || limit % 5 == 0 ? limit : 0));
}
