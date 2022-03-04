# pattern program1
n = int(input("Enter the number : "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end="")
    print()
# output
# 1
# 12
# 123
# 1234
# 12345
# 123456

# **************************************************************************************************
# n = int(input("Enter the number :"))
# for row in range(1, n+1):
#     for col in range(1,row+1):
#         print(row,end="")
#     print()
#     output
#     1
#     22
#     333
#     4444
#     55555
#     666666
#
# ***************************************************************************************************
# n = int(input("Enter number :"))
# num = 1
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num,end=" ")
#         num +=1
#     print()
#
#     output
#     1
#     2 3
#     4 5 6
#     7 8 9 10
#     11 12 13 14 15


#******************************************************************************************************
#amstrong numbers
# for i in range(1001):
#     num=i
#     result=0
#     n=len(str(num))
#     while(i!=0):
#         digits = i%10
#         result = result+digits**n
#         i = i//10
#         if num==result:
#             print(num)

#******************************************************************************************************
#factorial number

# n = int(input("enter the number :"))
# result = 1
# for i in range(n,0,-1):
#     result = result*i
# print("factorial number ",n,"is",result)

#******************************************************************************************************

#star pattern program
# n = int(input("Enter the number :"))
# for row in range(0,n):
#     for col in range(0,n):
#         if row==0 or col==(n-1) or row==col:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

#******************************************************************************************************
#string pattern
# string = input("enter the string : ")
# length = len(string)
# for row in range(length):
#     for col in range(row+1):
#         print(string[col],end="")
#     print()

#******************************************************************************************************
# #fibonocci number series
# n= int(input("Enter how many times it loop"))
# first = 0
# second = 1
# for i in range(n):
#     print(first)
#     temp = first
#     first=second
#     second=second+temp

#******************************************************************************************************
# n = int(input("enter number : "))
# for row in range(n,0,-1):
#     for col in range(1,row+1):
#         print(col,end="")
#     print()

#******************************************************************************************************

# lower = int(input("Enter lower number :"))
# upper = int(input("Enter upper number :"))
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#                 break
#         else:
#             print(num)

#******************************************************************************************************
# for row in range(1,5):
#     for col in range(1,8):
#         if row == 4 or row+col ==5 or col-row==3:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
# n= int(input("Enter number of rows :"))
# for row in range(1,n+1):
#     for col in range(1,n*2):
#         if row == n or row+col ==n+1 or col-row==n-1:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

# x = 5
# def add_fun():
#     y= 10
#     z=x+y
#     print(z)
# add_fun()

# import array as arr
# array1 = arr.array('i',[1,2,3,4,5])
# list1 = [1,"greeshma",80.5]
# print(array1)
# print(list1)

# def new_func():
#     print("hello")
# new_func()
#
#
# new_func()


# class Student:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
# S1 =Student("Greeshma",28,45000)
# print(S1.name)
# print(S1.age)
# print(S1.salary)

# a=lambda x,y : x+y
# print(a(5,6))

# import array as arr
# array1 = arr.array('i',[1,2,3,4,5])
# print(array1[::-1])

# from random import shuffle
# x = ['abc','pqr','xyz']
# shuffle(x)
# print(x)

# str = "greeshma"
# str1="Rani"
# print(str.capitalize())
# print(str1.capitalize())


"""
Using docstring as a comment.
This code divides 2 numbers
"""
# x=8
# y=4
# z=x+y
# print(z)
