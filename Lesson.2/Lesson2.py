# def sum():
#     print("Hey apple")
# sum()


# def sum(a, b):
#     print(a + b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum(a, b)


# def sum(a, b):
#     return a + b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# result = sum(a, b)
# print("Result =", result)


# global glob

# def sum(a=0, b=0):
#     glob = "Global Wars"
#     if a > 0:
#         return a + b
#     else:
#         print("Test")
#         return 0

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# res = sum(a, b)
# print("Result =", res)
# print(glob)


# def sum(*params):
#     res = 0
#     for item in params:
#         print(item)
#         res += item
#     return res

# result = sum(2, 5, 15)
# print("Result =>", result)


# tmp = 10
# for i in range(1, tmp):
#     print(i)

# 1

# a = int(input("First number: "))
# b = int(input("Second number: "))

# def find_range(a, b):
#     res = 0
#     for i in range(a+1, b):
#         res += i
#     return res

# result = find_range(a, b)
# print("Result =>", result)

# 2

# def distance(lenght, time):
#     return lenght/time

# lenght = float(input("Enter length: "))
# time = float(input("Enter time: "))

# result = distance(lenght, time)
# print("Speed is:", result)



# arr = [4, 5, 6, 9, 8, 1, 4]
# print(arr, "type => ", type(arr))
# for i in arr:
#     print(i)
# print("=================================>")
# arr[2] = 150
# for i in arr:
#     print(i)

# arr.append(99)
# print("=================================>")
# arr[2] = 150
# for i in arr:
#     print(i)

# arr.insert(2, 88)
# print("=================================>")
# for i in arr:
#     print(i)

# arr.remove(4)
# print("=================================>")
# for i in arr:
#     print(i)

# print("index =>", arr.index(1))

# print("arr len =>", len(arr))

# print("count =>", arr.count(8))

# arr.pop()
# print("after pop =>")
# for i in arr:
#     print(i)

# print("Sort ==========>")
# arr.sort()
# for i in arr:
#     print(i)

# print("Reverse ==========>")
# arr.reverse()
# for i in arr:
#     print(i)

# print("Max =>", max(arr))
# print("Min =>", min(arr))



# arr = [4, 5, 7, 4, [34, 5, 3], 43, 34, "Works", True]
# print(arr)
# arr[4][1] = 90
# print(arr)



# person = ["Tom", "Bill", "Abram", "Steel", "Adam"]
# for i in person:
#     print(i)

# person.sort()
# for i in person:
#     print(i)

# 3

# from random import randint

# numbers = []
# for i in range(30):
#     numbers.append(randint(-20, 30))
#     if numbers[i] < 0:
#         numbers[i] = -numbers[i]
#     print(numbers)



# lang = ["C++", "Python", "JavaScript", "C#", "Java"]
# # prog = lang
# # print(prog)
# # prog[0] = "Kotlin"
# # print("Prog =>", prog)
# # print("Lang =>", lang)

# # import copy 
# # prog = copy.deepcopy(lang)
# # prog[0] = "Kotlin"
# # print("Prog =>", prog)
# # print("Lang =>", lang)

# part = lang[2:8:2]
# part = lang[:4]
# print(part)



# car = ("Bmw", "Renault", "VW", "Audi")
# print(car)

# for i in car:
#     print(i)

# print(car[-1])

# print(len(car))
# print("Audi count ", car.count("Audi"))

# i = 0
# while i < len(car):
#     print(car[i])
#     i += 1

# person = ("Bill", 34)

# name, age = person
# print("Name : ", name, "\nAge: ", age)



countries = {
    "UA": "Ukraine",
    "US": "USA",
    "BR": "Brasil"
}

for key, value in countries.items():
    print(key, "====", value)

countries.pop("BR")
print("=======After=======")

for key, value in countries.items():
    print(key, "====", value)

# for key, value in countries.items():
#     print(key, "====", value)

# for key in countries.keys():
#     print(key)

# for value in countries.values():
#     print(value)

# print(countries["UA"])
print(countries.get("US"))
countries["IT"] = "Italy"
for key, value in countries.items():
    print(key, "====", value)