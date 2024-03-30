def nthSandwich(n):
    if n == 0:
        return 11
    count = 0
    num = 1
    while True:
        num_str = str(num)
        first_digit = int(num_str[0])
        last_digit = int(num_str[-1])
        if first_digit != 0 and first_digit == last_digit and str(first_digit) not in num_str[1:-1]:
            count += 1
            if count == n:
                return num
        num += 1
