from functools import reduce

languages = [set(input().split(", ")) for _ in range(int(input()))]

result = list(reduce(lambda x, y: x.intersection(y), languages))

if result:
    print(', '.join(sorted(result)))
else:
    print("Сериал снять не удастся")
