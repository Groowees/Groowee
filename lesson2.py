# # number = 10+2
# # print(number)
# # print(type(number))
# # number = 20.5
# # print(number)
# # print(type(number))
# # number = "Vasya"
# # print(number)
# # print(type(number))
# # number = True
# # print(number)
# # print(type(number))
# #
# # #":=" моржовый оператор ( тут же создает пременную )
# # print(number := 10)
# # print(type(number))
#
# nuber2=number+2
# print(nuber2)
# print(6//4)
# # print(6%4)
# number = 106
# n1 = number // 100
# n2 = number // 10 % 10
# n3 = number % 10
# print(n1)
# print(n2)
# print(n3)
# result = n1 + n2 + n3
# print(result)
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(name + str(age))
#

# number = int(input("Enter a number: "))
# n1 = number // 1000
# n2 = number % 1000 // 100
# n3 = number % 100 //10
# n4 = number % 10
# print(n1)
# print(n2)
# print(n3)
# print(n4)
# result = n1 + n2 + n3 + n4
# # print(result)
#  12345
number = int(input("Enter a number: "))
n1 = number % 10
n2 = number % 100 // 10
n3 = number % 1000 // 100
n4 = number % 10000 // 1000
n5 = number // 10000
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
result = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
print(result)
