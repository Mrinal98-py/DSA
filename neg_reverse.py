num = 1534236469 

if num < 0:
    num = num * -1
    rev= 0
    while num > 0:
        last_digit = num % 10
        rev = rev*10 + last_digit
        num = num // 10
    print(rev * -1)
else:
    rev= 0
    while num > 0:
        last_digit = num % 10
        rev = rev*10 + last_digit
        num = num // 10
    print(rev)