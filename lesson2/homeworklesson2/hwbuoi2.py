#Bai1
n=5
for i in range(5):
    for j in range(i):
        print('* ', end="")
     print("")
 for i in range(5,0,-1):
     for j in range(i):
         print('* ', end="")
     print("")

#Bai2
count_odd = 0
count_even = 0
for x in range(9):
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#Bai3
for k in range(1500,2700):
    if not k%7 and not k%5:
        print(k,end="\n")
#Bai4
import random
number = random.randint(1,9)
for m in range(9):
    n = int(input("Your guess is:"))
    if n != number:
        print("Incorrect!")
        print(number)
    if n == number:
        print("Correct")
        quit()

#Bai5
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print(i,type(i),end="\n")

#Bai6
for i in range(6):
    if i == 3 and 6:
        continue
    print(i, end=" ")

#Bai7
a,b = 0,1
while b<50:
    print(b)
    a,b=b,a+b
#Bai8
for i in range(51):
    if not i % 3 and not i % 5: print("fizzbuzz")
    elif not i%3: print("fizz")
    elif not i%5: print("buzz")

    else: print(i)

#Bai9
r= int(input("insert row: "))
c= int(input("insert col: "))

def d_array(x,y):
   array = [[i*j for j in range(x)]for i in range(y)]
   return array

print(d_array(r,c))

#Bai10: khong bit lam
#Bai 11:
a = input("Your string?")
b = c = 0
for i in a:
    if i.isdigit():
        b+=1
    elif c.isalpha():
        l+=1
    else:
        continue
print("Digits",b)
print("Letters",c)

