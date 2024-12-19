str = "C.12!"
s1 = ""
for i in str:
    if i.isalnum():
        print(i)
        s1 = s1 + i
    else:
        print(i,"<-NOT")        
print(s1)