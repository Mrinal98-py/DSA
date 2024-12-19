def sumOfSeries(n):
    if n == 0: 
        print("0")
    else:
        printr = n**3 + sumOfSeries(n-1)
        print(printr)
# print(sumOfSeries(sum))
n = 5
sumOfSeries(n)