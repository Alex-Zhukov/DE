import sys

data = [line for line in sys.stdin]
for num_line in range(len(data)):
    if data[num_line].strip().startswith("#"):
        data[num_line] = '\n'

print(*data)
