from BankAccount import BankAccount

#Create instances of bank account
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)

    #Overriding the withdraw method from the parent class BankAccount
    def withdraw(self, amount):
        if amount >self.transfer_limit: #check if the amount is greater than the transfer limit
            print("Withdrawal limit exceeded")
        elif self.current_balance - amount < self.minimum_balance: #check if the balance is less than the minimum balance
            print("Insufficient funds")
        else:
            self.current_balance -= amount #subtract the amount from the balance
            print(f"\nWithdrawal: ${amount:.2f} | New Balance: ${self.current_balance:.2f}")