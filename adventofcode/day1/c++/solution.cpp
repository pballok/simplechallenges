#include <iostream>
#include <fstream>

int main(int, char**)
{
  const std::string input_file_name = "../input.txt";

  std::ifstream infile(input_file_name);
  if (!infile.good()) {
    std::cerr << "Failed to read from file: " << input_file_name << std::endl;
    return 1;
  }

  long int weight = 0;
  long int fuel = 0;
  while(infile >> weight) {
    fuel += (weight / 3) - 2;
  }

  std::cout << fuel << std::endl;

  return 0;
}
