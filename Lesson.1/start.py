import random

# a = 10  # integer
# print(a, type(a))

# a = 10.6  # float
# print(a, type(a))

# a = True  # boolean
# print(a, type(a))

# a = "Bill"  # string
# print(a, type(a))

# name = input("Your name: ")
# age = float(input("Your age: "))
# print(name, type(name))
# print(age, type(age))

# a = int(input("Number 1: "))
# b = int(input("Number 2: "))
# c = int(input("Number 3: "))
# res = a + b
# print("Result = ", res)

# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a = b")

# if a > b and a > c:
#     print("first if ")
# elif a > b or b > c:
#     print("elif")

# a = int(input("Enter km: "))
# res = a * 1000
# print("Result (m) = ", res)


# print("Welcome to the currency converter.")
# UAH = float(input("Enter amount of UAH: "))
# Choice = input("Do you want that in USD, EUR or GBP? ")
# GBP = (UAH / 34.32)
# USD = (UAH / 27.70)
# EUR = (UAH / 30.25)
# if Choice == "GBP":
#     print("₴", UAH, "is equal to:")
#     print("£", GBP)
# elif Choice == "USD":
#     print ("₴",UAH, "is equal to:")
#     print ("$", USD)
# elif Choice == "EUR":
#     print ("₴",UAH, "is equal to:")
#     print ("€", EUR)


# km = float(input("Enter amount of kilometers you need to reach: "))
# price = float(input("Enter price/1l: "))
# consumption = float(input("Enter fuel consumption of your car: "))
# res = (km / consumption * price)
# print("You need to spend: ",res,"UAH")


# a = random.randrange(0, 10)
# b = random.randrange(0, 10)
# c = random.randrange(0, 10)
# print(a, b, c)
# if a == b == c:
#     print('All equal')


# exit = False
# while not exit:
#     choice = int(input("1. Add\n2. Div\n0. Exit\n==>"))
#     if choice == 1:
#         print("a+b")
#         print("sum: ", float(input("Enter a: "))+float(input("Enter b: ")))
#     elif choice == 2:
#         print("a/b")
#         print("div: ", float(input("Enter a: "))/float(input("Enter b: ")))
#     elif choice == 0:
#         exit = True


# i = 0
# counter = 0
# while i < 7:
#     i += 1
#     temp = random.randint(-10, 30)
#     if temp > 10:
#         counter += 1
#         print(temp)
# print("More then 10° => ", counter, "days")


number = 8
counter = 0
for i in range(1, number):
    temp = random.randint(-10, 30)
    if temp > 10:
        counter += 1
    print(temp)
print("More then 10° => ", counter, "days")
