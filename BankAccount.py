class BankAccount:
    #Class attributes
    bank_name = "Software Engineering Bank"

    #Constructor 
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  #this is the protected member
        self._routing_number = routing_number  #this is the private member

    #Methods
    def deposit(self, amount):
        self.current_balance += amount
        print(f"\nDeposit: ${amount:.2f} | New Balance: ${self.current_balance:.2f}")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Insufficient funds")
        else:
            self.current_balance -= amount
            print(f"\nWithdrawal: ${amount:.2f} | New Balance: ${self.current_balance:.2f}")

    def print_account_info(self):
        print("\n=== Account Information ===")
        print(f"Bank: {self.bank_name}")
        print(f"Customer: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("============================\n")

# #Create instances
# account1 = BankAccount("John Doe", 500, 100)
# account2 = BankAccount("Jane Doe", 500, 100)
#
# #Call methods
# account1.deposit(100)
# account1.withdraw(50)
# account1.print_account_info()
#
# account2.deposit(500)
# account2.withdraw(6000)
# account2.print_account_info()
