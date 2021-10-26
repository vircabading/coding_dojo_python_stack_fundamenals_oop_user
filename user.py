# *********************************************************
# Subj: Coding Dojo > Python > Fundamentals: User
# By:   Virgilio D. Cabading Jr.    Created: October 26, 2021
# *********************************************************

# //// CLASS USER /////////////////////////////////////////
class User:

    # **** CLASS METHODS **********************************
    def __init__(self) -> None:                             # Class Instance Constructor
        self.first_name = "John"
        self.last_name = "Doe"
        self.account_balance = 0;
    
    def make_withdrawal (self, amount):                     # Method that decreases the user's account_balance by specified amount
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"{' Balance Information ':*^80}")
        print(f" User: {self.first_name} {self.last_name} ::: Balance: {self.account_balance}\n")
        return self

    def info(self):                                         # Method that displays info of class instance
        print(f"{' {self.first_name} {self.last_name} Information ':*^80}")
        print(f"first_name : {self.first_name}")
        print(f"last_name : {self.last_name}")
        print(f"account_balance: {self.account_balance}\n")
        return self

# //// MAIN EXECUTABLE SECTION ////////////////////////////

Virgilio = User()
Virgilio.info().account_balance = 1000
Virgilio.info().make_withdrawal(200)
Virgilio.display_user_balance()
