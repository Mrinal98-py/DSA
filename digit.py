def reverse(n):
    rev = 0
    while (n>0):
        last_digit = n % 10
        rev = rev*10 + last_digit
        n = n//10
    print("The Reverse no is ",rev)
    
    
    
def countDig(n):
    cont = 0    # increment while n%10 !=0
    while (n>0):
        last_digit = n%10
        cont +=1    # increment the counter
        n = n//10   # remove the last digit
    print("The no of digit:",cont)

num = 6212
countDig(num)
