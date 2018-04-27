a = input("Your string?")
b = c = 0
for i in a:
    if i.isdigit():
        b+=1
    elif i.isalpha():
        c+=1
    else:
        continue
print("Digits",b)
print("Letters",c)