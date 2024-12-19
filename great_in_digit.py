def greatest_in_digit(n):
    high = 0
    while n > 0:
        last_digit = n % 10 # get last digit

        if high < last_digit:
            high =  last_digit
        else:
            high = high
    
        n = n // 10 #remve lsat digit 
    print("Greatest in Digit is:", high)

n = 213916
greatest_in_digit(n)
