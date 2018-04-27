col = int(input("Insert the number of columns"))
row = int(input("Insert the number of rows"))

def array(x,y):
    ar = [[i*j for j in range(x)]for i in range(y)]
    return ar
print(array(col,row))

