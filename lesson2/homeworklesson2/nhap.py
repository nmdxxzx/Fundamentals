from re import search
password = input("Type your desired password")
x = True
while x:
    if not (len(password)>6 and len(password)<16):
        break
    elif not search("[a-z]",password):
        break
    elif not search("[A-Z]",password):
        break
    elif not search("[0-9]",password):
        break
    elif not search("[@#$]",password):
        break
    print("Valid password")



else:
    print("Invalid password")