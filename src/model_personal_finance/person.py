import numpy as np
import pandas as pd

class Investor:
    """This class represents a retail investor who wants to grow his or her wealth.
    """
    def __init__(self, accounts, age, tax_bracket, salary, company_match):
        
        self.accounts = accounts
        self.age = age
        self.tax_bracket = tax_bracket
        self.salary = salary
        self.company_match = company_match # Percentage of salary


    def calculate_assets_at_age(self, age, investment_return=7):
        """Calculate the balance of all of an Investor's assets at a given age.

        :param age: Age for asset balance calculation, defaults to self.age
        :type age: int, optional
        :param investment_return: Assumed avg constant rate of return, defaults to 7%
        :type investment: float, optional
        """
        # Iterate through the accounts, call a method to output a dataframe with age, balance, account name
        # Aggregate each account, print result, and return the dataframe of data
        account_amortization = {'age' : np.arange(self.age, age, 1)}
        duration = age - self.age 
        for account_key in self.accounts.keys():
            account_amortization[account_key] = self.accounts[account_key].compound_balance(
                duration, investment_return)

        amortization = pd.DataFrame(account_amortization)
        return amortization.iloc[-1].sum()
