def sleep_in(weekday, vacation):
    return not weekday or vacation

if __name__ == "__main__":
    assert sleep_in(False, False)
    assert not sleep_in(True, False)
    assert sleep_in(False, True)
    assert sleep_in(True, True)
