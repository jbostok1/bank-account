from BankAccount import BankAccount

#Create instances of bank account
class SavingsAccount(BankAccount):
    #Define constructor
    def __init__(self, customer_name, current_balance, minimum_balance, account_number,routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate
    
    #Define methods
    def apply_interest(self):
        interest = self.current_balance * self.interest_rate #calculate interest
        self.current_balance += interest
        print(f"\nInterest: ${interest:.2f} | New Balance: ${self.current_balance:.2f}")