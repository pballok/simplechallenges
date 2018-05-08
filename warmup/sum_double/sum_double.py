def sum_double(num1, num2):
    sum = num1 + num2

    if num1 == num2:
        return 2 * sum

    return sum


if __name__ == "__main__":
    assert sum_double(2, 3) == 5
    assert sum_double(-4, 0) == -4
    assert sum_double(3, 3) == 12
