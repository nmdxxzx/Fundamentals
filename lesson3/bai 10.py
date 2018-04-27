a = input("Please type your sentence")
b = c = 0

for i in a:
    if i.isupper():
        b+=1
    elif i.islower():
        c+=1
    else:
        continue
print("UPPER CASE", b)
print("lower case", c)