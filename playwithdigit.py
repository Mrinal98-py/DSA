def count(n):
    count = 0
    while n >0:
        n = n // 10
        count += 1
    print("total no of digit in the number is: ", count)
    
def reverse(n):
    rev  = 0
    while n > 0:
        last = n % 10
        rev = rev *10 + last
        n = n//10
    print("Reverse of the number is: ", rev)    
    
def sunofdigit(n):
    sum = 0
    while n > 0:
        last_digit = n % 10
        sum += last_digit
        n = n // 10
    print("Sum of the digits is: ", sum)

def greatest_in_digit(n):
    high = 0
    while n > 0:
        last_digit = n % 10 # get last digit 
        if last_digit >= high: #comapre and replace
            high = last_digit
        n = n // 10 #remve lsat digit 
    print("Greatest in Digit is:", high)

def small_in_digit(n):
    small = 9
    while n > 0:
        last_digit = n % 10
        if small > last_digit:
            small = last_digit
        n = n // 10
    print("Smallest digit in num is:",small)

# main code

number = -64325967
print("Number is: ", number)

# call the function 
count(number)
reverse(number)
sunofdigit(number)
greatest_in_digit(number)
small_in_digit(number)