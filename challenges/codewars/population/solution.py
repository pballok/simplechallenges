def nb_year(p0, percent, aug, p):
    year = 0
    pop = p0
    percent = percent / 100.0
    while pop < p:
      year += 1
      pop += pop * percent + aug

    return year

if __name__ == "__main__":
  assert(nb_year(1500, 5, 100, 5000) == 15)
  assert(nb_year(1500000, 2.5, 10000, 2000000) == 10)
  assert(nb_year(1500000, 0.25, 1000, 2000000) == 94)

  print("All tests passed")
