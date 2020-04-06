# 1

# currentTime = int(
#     input("Enter time in next format(e.g. 1am is 1 hours and 11pm is 23 hours):\n"))

# if 5 <= currentTime < 12:
#     print('Good morning')
# elif 12 <= currentTime < 16:
#     print('Good afternoon')
# elif 16 <= currentTime < 19:
#     print('Good evening')
# else:
#     print('Good night')

# 2

# lenght = float(input("Enter lenght: "))
# Choice = input("Do you want that in cm or inch? ")
# cm = (lenght / 2.54)
# inch = (lenght * 2.54)
# if Choice == "cm":
#     print(lenght, "cm", "is equal to:")
#     print(cm, "inch")
# elif Choice == "inch":
#     print(lenght, "inch", "is equal to:")
#     print(inch, "cm")

# 3

# t = input("Enter temperature in Celsius or in Fahrenheit (10C or 10F - example)\n")
# sign = t[-1]
# t = int(t[0:-1])
# if sign == 'C' or sign == 'c':
#     t = round(t * (9/5) + 32)
#     print(str(t) + 'F°')
# elif sign == 'F' or sign == 'f':
#     t = round((t - 32) * (5/9))
#     print(str(t) + 'C°')

# 4

# n1 = int(input("Enter 1st number:\n"))
# n2 = int(input("Enter 2nd number:\n"))
# n3 = int(input("Enter 3th number:\n"))
# n4 = int(input("Enter 4th number:\n"))
# n5 = int(input("Enter 5th number:\n"))
# n6 = int(input("Enter 6th number:\n"))
# n7 = int(input("Enter 7th number:\n"))
# n8 = int(input("Enter 8th number:\n"))
# res1 = n1*n2*n3*n4*n5*n6*n7*n8
# res2 = (n1+n2+n3+n4+n5+n6+n7+n8) / 8
# print("Arithmetic mean is: ", res2, "Product is: ", res1)

# 5

# import random

# minValue = 30
# maxValue = -10
# counter = 0
# while counter < 7:
#     randomTemp = random.randint(-10, 30)
#     counter += 1
#     if randomTemp > maxValue:
#         maxValue = randomTemp
#     if randomTemp < minValue:
#         minValue = randomTemp
#     print(randomTemp)
# print("Minimum Temperature =", minValue, "Maximum Temperature =", maxValue)
