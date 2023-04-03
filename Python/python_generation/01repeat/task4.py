from collections import Counter


def print_not_unique(input: str):
    numbers = map(int, input.split())
    sorted_counter = {k: v for k, v in sorted(Counter(numbers).items(), key=lambda x: x[0])
                      if v > 1}
    print(*sorted_counter)



input_numbers = '4 8 0 3 4 2 0 3'

print_not_unique(input_numbers)
