from savings_account import SavingsAccount
from checking_Account import CheckingAccount

def main():

    print("Welcome to the Software Engineering Bank!")

    #create savings account
    savings_account1 = SavingsAccount("John Doe", 500, 100, 1234, 5678, 0.05)
    savings_account2 = SavingsAccount("Jane Doe", 1000, 100, 1234, 5678, 0.5)

    #apply interest
    savings_account1.apply_interest()
    savings_account1.print_account_info()

    savings_account2.apply_interest()
    savings_account2.print_account_info()

    #create checking account
    checking_account1 = CheckingAccount("John Doe", 500, 100, 1234, 5678, 1000)
    checking_account2 = CheckingAccount("Jane Doe", 500, 100, 1234, 5678, 1000)

    #withdraw
    checking_account1.withdraw(100)
    checking_account1.print_account_info()

    checking_account2.withdraw(500)
    checking_account2.print_account_info()

if __name__ == "__main__":
     main()