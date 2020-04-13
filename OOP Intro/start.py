# class Person:

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#         print("Constructor Working...")

#     def __del__(self):
#         print("Desctructor working...")

#     def person_info(self):
#         print(self.__name, " <-> ", self.__age, " years old")

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, new_age):
#         if self.__age == new_age:
#             print("The same age")
#         else:
#             self.__age = new_age


# bill = Person("Billy", 56)
# # print("Bill age before => ", bill.name)
# # print("Bill age before => ", bill.age)
# # bill.age = 58
# # bill.name = "Test" Error
# # print("Bill age after => ", bill.name)
# # print("Bill age after => ", bill.age)

# # bill.person_info()

# # print(bill.get_name())
# # print("Before +> ", bill.get_age())
# # bill.set_age(70)
# # print("After +> ", bill.get_age())

# stive = Person("Stiven", 26)
# # stive.person_info()
# adam = Person("Adam", 34)
# eva = Person("Eva", 27)
# tina = Person("Tina", 29)
# sara = Person("Sara", 39)

# person_list = []
# person_list.append(bill)
# person_list.append(stive)
# person_list.append(adam)
# person_list.append(eva)
# person_list.append(tina)
# person_list.append(sara)


# for person in person_list:
#     # person.person_info()
#     print(person.name, " = ", person.age)
#     person.age += 1

# print("===========================")

# for person in person_list:
#     # person.person_info()
#     print(person.name, " = ", person.age)


class Bank_Account:

    def __init__(self, account_num, currency, balance=0):
        self.__account_num = account_num
        self.__balance = balance
        self.__currency = currency
        self.__transactions = []
        print("Welcome to the deposit & withdrawal machine")

    def deposit(self, amount):
        amount = float(input("Enter amount to be Deposited: "))
        self.__balance += amount
        self.__transactions.append(+amount)
        return amount

    def withdraw(self, amount):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(-amount)
            return amount
        else:
            print("\n Insufficient balance  ")

    def get_account_num(self):
        return self.__account_num

    def get_balance(self):
        return self.__balance

    def get_currency(self):
        return self.__currency

    def recent_transactions(self):
        if len(self.__transactions) < 1:
            return None
        else:
            return self.__transactions.pop()

account = Bank_Account(5420405602321114, "$")
print('account number =', account.get_account_num())
print('account balance =', account.get_balance())
print('account currency =', account.get_currency())
print('deposit =', account.deposit(20), "$")
print('recent transaction is:', account.recent_transactions(), "$")
print('account balance =', account.get_balance(), "$")
print('withdrawal =', account.withdraw(50), "$")
print('recent transaction is:', account.recent_transactions(), "$")
print('account balance =', account.get_balance(), "$")