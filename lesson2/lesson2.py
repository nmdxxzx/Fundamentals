# # # # # # # import datetime
# # # # # # # n = int(input("Nhap vao nam sinh cua ban?"))
# # # # # # # age = 2018 - n
# # # # # # # print("Tuoi cua ban la", age)
# # # # # # # if age<10:
# # # # # # #     print("Ban la baby")
# # # # # # # elif 18>age>=14:
# # # # # # #     print("Ban la teenager")
# # # # # # # else:
# # # # # # #     print("Ban la adult!!!")
# # # # # # #
# # # # # #
# # # # # # import math
# # # # # # a = int(input("Nhap he so cua A"))
# # # # # # b = int(input("Nhap he so cua B"))
# # # # # # c = int(input("Nhap he so cua C"))
# # # # # #
# # # # # #
# # # # # # if a == 0:
# # # # # #     print("Phuong trinh khong phai phuong trinh bac 2")
# # # # # # else:
# # # # # #     delta = b ** 2 - 4 * a * c
# # # # # #     if delta<0:
# # # # # #         print("phuong trinh vo nghiem")
# # # # # #     else:
# # # # # #         if delta==0:
# # # # # #             x=-b/(2*a)
# # # # # #             print("phuong trinh co nghiem kep la",x)
# # # # # #         else:
# # # # # #             x1 = (-b-math.sqrt(delta))/(2 * a)
# # # # # #             x2 = (-b+math.sqrt(delta))/(2 * a)
# # # # # #             print("x1 = ", x1)
# # # # # #             print("x2 = ", x2)
# # # # # #
# # # # #
# # # # # a=[5,2,3,5]
# # # # # sum = 0
# # # # # for i in range(len(a)):
# # # # #     sum = sum+a[i]
# # # # # print("sum of a:",sum)
# # # # import random
# # # # a =[]
# # # # for i in range(20):
# # # #     a.append(random.randint(1,100))
# # # # for i in range(20):
# # # #     print(a[i],end="  ")
# # # # print('max cua a la',max(a))
# # # #
# # # a = [1, "xin chao", {2,3}]
# # # b = [[1,4],[2,3,4],1]
# # # c = [{1,2,3,4},{8,6,34,19}]
# # # for x,y,z,p in c:
# # #     print(x,y,z,p)
# #
# # a = [4,6,8,9]
# # print(a[2:4])
#
# a = ["sadness", "happiness"]
# n = '''░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░
# ░░░░░░░░░░░░▄████████████████▄░░░░░░░░░░
# ░░░░░░░░░░▄██▀░░░░░░░▀▀████████▄░░░░░░░░
# ░░░░░░░░░▄█▀░░░░░░░░░░░░░▀▀██████▄░░░░░░
# ░░░░░░░░░███▄░░░░░░░░░░░░░░░▀██████░░░░░
# ░░░░░░░░▄░░▀▀█░░░░░░░░░░░░░░░░██████░░░░
# ░░░░░░░█▄██▀▄░░░░░▄███▄▄░░░░░░███████░░░
# ░░░░░░▄▀▀▀██▀░░░░░▄▄▄░░▀█░░░░█████████░░
# ░░░░░▄▀░░░░▄▀░▄░░█▄██▀▄░░░░░██████████░░
# ░░░░░█░░░░▀░░░█░░░▀▀▀▀▀░░░░░██████████▄░
# ░░░░░░░▄█▄░░░░░▄░░░░░░░░░░░░██████████▀░
# ░░░░░░█▀░░░░▀▀░░░░░░░░░░░░░███▀███████░░
# ░░░▄▄░▀░▄░░░░░░░░░░░░░░░░░░▀░░░██████░░░
# ██████░░█▄█▀░▄░░██░░░░░░░░░░░█▄█████▀░░░
# ██████░░░▀████▀░▀░░░░░░░░░░░▄▀█████████▄
# ██████░░░░░░░░░░░░░░░░░░░░▀▄████████████
# ██████░░▄░░░░░░░░░░░░░▄░░░██████████████
# ██████░░░░░░░░░░░░░▄█▀░░▄███████████████
# ███████▄▄░░░░░░░░░▀░░░▄▀▄███████████████'''
#
# print(n)

def tinh_tong_mang(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum
b = [2,5,7,9,11]
sum = tinh_tong_mang(b)
print(sum)
