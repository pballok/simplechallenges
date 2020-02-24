#!/usr/bin/env python3

def get_grade(s1, s2, s3):
  score = (s1 + s2 + s3) / 3

  if score < 60:
    return "F"

  if score < 70:
    return "D"

  if score < 80:
    return "C"

  if score < 90:
    return "B"

  return "A"

if __name__ == "__main__":
  assert(get_grade(95, 90, 93) == "A")
  assert(get_grade(100, 85, 96) == "A")
  assert(get_grade(92, 93, 94) == "A")

  assert(get_grade(70, 70, 100) == "B")
  assert(get_grade(82, 85, 87) == "B")
  assert(get_grade(84, 79, 85) == "B")

  assert(get_grade(70, 70, 70) == "C")
  assert(get_grade(75, 70, 79) == "C")
  assert(get_grade(60, 82, 76) == "C")

  assert(get_grade(65, 70, 59) == "D")
  assert(get_grade(66, 62, 68) == "D")
  assert(get_grade(58, 62, 70) == "D")

  assert(get_grade(44, 55, 52) == "F")
  assert(get_grade(48, 55, 52) == "F")
  assert(get_grade(58, 59, 60) == "F")

  print("All tests passed")
