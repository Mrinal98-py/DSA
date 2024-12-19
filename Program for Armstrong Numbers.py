num = 1634
# 153 370 371 407 
ad = num
length = len(str(num))
sum = 0
if num < 0: print("YAP YAP YAP -ve number")
if num < 10 and num >= 0:
    print("Armstrong Number")    
    
elif num >= 10:
    while num > 0:
        last_digit = num % 10 
        sum += last_digit ** length 
        num = num // 10
    if ad == sum:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

#     print("Not an Armstrong Number")
    