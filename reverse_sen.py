sen = "buddy wants to play a game"

arr = sen.split()
print(type(arr))
arr = arr[::-1]
print(arr)

rev = ""
for i in arr:
    rev = rev + i + " "

print(rev,"Ans")


