def small_in_digit(n):
    small = 9
    while n > 0:
        last_digit = n % 10
        if small > last_digit:
            small = last_digit
        n = n // 10
    print("Smallest digit in num is:",small)

num = 31246
small_in_digit(num)
