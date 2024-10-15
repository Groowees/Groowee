# # #v1
# # n1 = 10
# # n2 = 20
# # #v2
# # n1,n2 = 10, 20
# # print(n1 > n2)
# # print(n1 >= n2)
# # print(n1 < n2)
# # print(n1 <= n2)
# # print(n1 == n2)
# # print(n1 != n2)
# # # # #
# # hours = int(input("Enter Hours: "))
# # # if hours >= 12:
# # #     print("PM")
# # # else:
# # #     print("AM")
# # # #
# # if 12 <= hours <= 24:
# #     print("PM")
# # elif 0 <= hours <= 12:
# #     print("AM")
# # else:
# # #     print("Incorrect hours")
numer1 = int(input("Enter first number: "))
numer2 = int(input("Enter second number: "))
numer3 = int(input("Enter third number: "))
if numer1 <= numer2 <= numer3:
    print("number1")
elif numer2 <= numer1 <= numer3:
    print("number2")
elif numer3 <= numer1 <= numer2:
    print("number3")












# number_b = 3
# number_a = 10 if number_b < 5 else 20
# print(number_a)