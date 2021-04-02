class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = 50000
        self.main()

    def balance_enquiry(self):
        print(self.balance)

    def cash_withdrawl(self, amount):
        if int(amount) <= self.balance:
            self.balance = self.balance - int(amount)
        else:
            print("Out of range!")

    def add_cash(self, amount):
        if int(amount) > 0:
            self.balance = self.balance + int(amount)
        else:
            print("Out of range")

    def main(self):
        print("You have ", self.balance, "in your account")
        while True:
            task = input(
                "What do you want to do (1: balance enquiry, 2: withdraw cash, 3: add cash, 4: exit): "
            )
            if task == "1":
                self.balance_enquiry()
            elif task == "2":
                amountToWithDraw = input(
                    "How much cash do you want to withdraw? ")
                self.cash_withdrawl(amountToWithDraw)
            elif task == "3":
                amountToAdd = input("How much cash do you want to add? ")
                self.add_cash(amountToAdd)
            else:
                raise SystemExit
