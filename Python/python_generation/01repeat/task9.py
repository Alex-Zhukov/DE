def get_byte_size(size, size_type):
    size_pow = {"GB": 3, "MB": 2, "KB": 1, "B": 0}
    return size * 1024 ** size_pow[size_type]


def get_size_and_type(size):
    revert_size_pow = {3: "GB", 2: "MB", 1: "KB", 0: "B"}
    current_pow = 0
    while size > 1024:
        current_pow += 1
        size /= 1024
        if current_pow >= 3:
            break
    return round(size), revert_size_pow[current_pow]


with open("files.txt", encoding="UTF-8") as f:
    data = f.readlines()

clear_data = {}
for line in data:
    file_name, size, size_type = line.strip().split()
    file_type = file_name.split(".")[1]
    byte_size = get_byte_size(int(size), size_type)
    clear_data.setdefault(file_type, []).append((file_name, byte_size))

for k, v in sorted(clear_data.items(), key=lambda x: x[0]):
    summary = 0
    for file in sorted(v, key=lambda x: x[0]):
        print(file[0])
        summary += file[1]

    size, size_type = get_size_and_type(summary)

    print("----------")
    print(f"Summary: {size} {size_type}")
    print()

