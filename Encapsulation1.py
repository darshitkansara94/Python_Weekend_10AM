class Bank():
    def __init__(self):
        self.__balance = 0 # Private property

    def display_balance(self):
        print(self.__balance)

    def update_balance(self,amount):
        self.__balance = amount

bank = Bank() # Initializing the Bank object
bank.update_balance(10)
bank.display_balance()
