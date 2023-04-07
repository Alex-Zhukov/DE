import sys
from datetime import datetime
from functools import reduce

data = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]

result = [data[i] - data[i - 1] for i in range(1, len(data))]

if all([i.total_seconds() > 0 for i in result]):
    print("ASC")
elif all([i.total_seconds() < 0 for i in result]):
    print("DESC")
else:
    print("MIX")
