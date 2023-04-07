import sys

data = [line.strip() for line in sys.stdin]
target_tag = data[-1]
news = sorted([el.split(' / ') for el in data[:-1] if el.split(' / ')[1] == target_tag],
              key=lambda x: (float(x[2]), x[0]))

for tag in news:
    print(tag[0])
