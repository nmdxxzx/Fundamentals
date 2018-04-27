list = [7,5,3,10]
newlist = []
while list:
    minimum = list[0]
    for i in list:
        if i < minimum:
            minimum=i
    newlist.append(minimum)
    list.remove(minimum)
print(newlist)
