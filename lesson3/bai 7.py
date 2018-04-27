list = input("Please enter your list")
list1 = list.split(", ")
ascii = [[ord(ch) for ch in word] for word in list1]
ascii2=[]
while ascii:
    minimum=ascii[0]
    for i in ascii:
        if i < minimum:
            minimum = i
    ascii2.append(minimum)
    ascii.remove(minimum)
s = ([[chr(c) for c in cut]for cut in ascii2 ])
print(s)