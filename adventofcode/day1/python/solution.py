
def main():
  fuel = 0
  with open("../input.txt") as f:
    for weight in f.readlines():
      fuel += (int(weight) // 3) - 2

  print(fuel)

main()
