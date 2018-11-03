#include "AnalogClock.h"

#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>

void processInput(const std::string& input_file_name)
{
  std::ifstream infile(input_file_name);
  if (!infile.good()) {
    std::cerr << "Failed to read from file: " << input_file_name << std::endl;
    return;
  }

  std::cout << "Processing input from " << input_file_name << std::endl;

  std::string line;
  std::getline(infile, line);
  std::size_t line_count = std::stoi(line);

  for (std::size_t i = 1; i <= line_count; ++i) {
    bool good_input = true;
    std::getline(infile, line);

    int64_t seconds = 0;
    try {
      seconds = std::stoi(line);
    }
    catch (const std::exception&) {
      good_input = false;
    }

    if (!good_input || seconds < 0) {
      std::cout << "Case #" << i << ": Invalid input: " << line << std::endl;
      continue;
    }

    AnalogClock ac{std::chrono::seconds(seconds)};
    std::cout << "Case #" << i << " (" << seconds << " seconds): Hour hand degree: " << ac.hourHandAngle();
    std::cout << ", Minute hand degree: " << ac.minuteHandAngle() << std::endl;
  }
}

int main(int argc, char** argv)
{
  if (argc != 2) {
    std::cout << "Usage: " << argv[0] << " <input_file_name>\n";
    return 1;
  }

  processInput(argv[1]);

  return 0;
}
