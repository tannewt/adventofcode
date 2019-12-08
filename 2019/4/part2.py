count = 0

for i in range(246515, 739105 + 1):
    digits = i
    last_digit = 10
    ok = False
    descending = True
    run = 1
    for _ in range(6):
        digit = digits % 10
        if digit > last_digit:
            descending = False
            break
        if digit == last_digit:
            run += 1
        else:
            if run == 2:
                ok = True
            run = 1
        last_digit = digit
        digits = digits // 10
    if descending and not ok and run == 2:
        print(i)
        count += 1
    if ok and descending:
        count += 1

#  453 is too low, 570 is not right
print(count)
