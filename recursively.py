def sumOfSeries(n):
    total = 0
    sum = 0
    if n == 0:
        return 0
    else: 
        sumOfSeries(n-1)
        sum = sum + n*n*n
        total = total + sum 
    print(total)
    
def printNos(n):
    print(n, end=" ")
    printNos(n-1)


def printer(n):
    if n == 0: return 0
    else: printer(n-1) 
    print(3*n, end=" ")

# printer(5)
a= 5
sumOfSeries(a)
