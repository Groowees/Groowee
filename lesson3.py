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
# # # #     print("Incorrect hours")
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
# if number1 <= number2 <= number3:
#     print("number1")
# elif number2 <= number1 <= number3:
#     print("number2")
# elif number3 <= number1 <= number2:
#     print("number3")
# else :
#     print("Incorrect input")

# user_select = int(input("1. Start\n2. Settings\n3. Saved games\n4. Exit\nSelect your choice: "))
#
# # v1
# if user_select == 1:
#     print("Starting game...")
# elif user_select == 2:
#     print("Settings")
# elif user_select == 3:
#     print("Saved games")
# elif user_select == 4:
#     print("Exit")
# else :
# #     print("Wrong input")
# number_b = 3
# if number_b < 5 :
#     number_a = 10
# else :
#     number_a = 20
#
# print(number_a)

number1 = int(input("Enter a first number: "))
simbol =  str(input("Enter a simbol: "))
number2 =  int(input("Enter a second number: "))
match simbol:
    case "-" :
        print(number1 - number2)
    case "+" :
        print(number1 + number2)
    case "*" :
        print(number1 * number2)
if simbol == "/" :
    if number1 > 0 and number2 > 0:
        print(number1 / number2)
    else:
        print("Incorrect input")
#






