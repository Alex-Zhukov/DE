reserved_emails = [input() for _ in range(int(input()))]
needed_emails = [input() for _ in range(int(input()))]

reserved_fio = [mail.split("@")[0] for mail in reserved_emails]

for fio in needed_emails:
    fio_copy = fio
    start_cnt = 1
    while True:
        if fio in reserved_fio:
            fio = fio_copy + str(start_cnt)
        else:
            reserved_fio.append(fio)
            print(fio + "@beegeek.bzz")
            break
        start_cnt += 1
