import sys

data = [line.strip() for line in sys.stdin if line.strip().startswith("#")]

print(len(data))
