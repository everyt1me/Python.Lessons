from datetime import datetime


class DiscountCard:
    def __init__(self, card_number, date_of_issue, amount=0):
        self.__card_number = card_number
        self.__date_of_issue = date_of_issue
        self.__discount = 1
        self.__amount = 0

        if amount != 0:
            self.__add(amount)

    def __date_validate(self, date_of_issue):
        try:
            if self.__date_of_issue != datetime.strptime(self.__date_of_issue, "%d/%m/%Y").strftime('%d/%m/%Y'):
                raise ValueError
            return True
        except ValueError:
            return False

    def __add(self, amount):
        if float(amount) > 0:
            self.__amount += float(amount)
            self.__discount = 1 + self.__amount // 1000

    def __str__(self):
        return "Discount Card: #"+str(self.__card_number)+", discount: "+str(self.__discount)+"%, date of issue: "+str(self.__date_of_issue)

    def buy_something(self, amount):
        self.__add(amount)

    def print_discount(self):
        print("Current discount: ", self.__discount, "%")

    def amount_to_increase_discount(self):
        print("To increase the value of the discount, you still need to buy the product for the next amount:",
              1000 - self.__amount % 1000)


card = DiscountCard(card_number=2565485, amount=500,
                    date_of_issue="05/30/2020")
print(card)
card.buy_something("5000")
card.print_discount()
print(card)
card.amount_to_increase_discount()
