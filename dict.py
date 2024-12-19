myfamily = {
  "child 01" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child 02" : {
    "name" : "Tobias",
    "year" : 2007
  }
}

for item,itemit in myfamily.items():
    print(item)
    
    for subitem in itemit:
        print(subitem + ':',itemit[subitem])


# simple code
# for item in myfamily.items():
#     print(item)

    # for subitem in item:
    #     print(item[subitem])
    
# for x,obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])

