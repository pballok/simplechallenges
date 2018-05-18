def near_hundred(num):
    return abs(num - 100) <= 10


if __name__ == "__main__":
    assert not near_hundred(-95)
    assert not near_hundred(0)
    assert not near_hundred(89)
    assert near_hundred(90)
    assert near_hundred(91)
    assert near_hundred(100)
    assert near_hundred(109)
    assert near_hundred(110)
    assert not near_hundred(111)

    print("All tests PASSED!")
