n = int(input())
groups = {}
for num in range(1, n + 1):
    sum_of_chars = sum(map(int, str(num)))
    groups.setdefault(sum_of_chars, []).append(num)

max_len = max(groups.items(), key=lambda x: len(x[1]))
print(len(max_len[1]))

# data = {}
#
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))