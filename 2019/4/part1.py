count = 0

for i in range(246515, 739105 + 1):
    digits = i
    last_digit = 10
    ok = False
    for _ in range(6):
        digit = digits % 10
        if digit > last_digit:
            ok = False
            break
        if digit == last_digit:
            ok = True
        last_digit = digit
        digits = digits // 10
    if ok:
        print(i)
        count += 1
print(count)
