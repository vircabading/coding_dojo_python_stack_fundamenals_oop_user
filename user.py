# *********************************************************
# Subj: Coding Dojo > Python > Fundamentals: User
# By:   Virgilio D. Cabading Jr.    Created: October 26, 2021
# *********************************************************

# //// CLASS USER /////////////////////////////////////////
from _typeshed import Self


class User:

    # **** CLASS METHODS **********************************
    def __init__(self) -> None:                             # Class Instance Constructor
        self.account_balance = 0;
    
    def make_withdrawal (self, amount) -> Self:             # Method that decreases the user's account_balance by specified amount
        self.account_balance -= amount
        return self

# //// MAIN EXECUTABLE SECTION ////////////////////////////

