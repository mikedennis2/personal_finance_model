import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick 

class Investor:
    """This class represents a retail investor who wants to grow his or her wealth.
    """
    def __init__(self, accounts, expenses, age, tax_bracket, salary, company_match):
        
        self.accounts = accounts # Dictionary of account names and InvestmentAccounts
        self.age = age
        self.tax_bracket = tax_bracket
        self.salary = salary
        self.company_match = company_match # Percentage of salary
        self.expenses = expenses 


    def calculate_assets_at_age(self, age, investment_return=7):
        """Calculate the balance of all of an Investor's assets at a given age.

        :param age: Age for asset balance calculation, defaults to self.age
        :type age: int, optional
        :param investment_return: Assumed avg constant rate of return, defaults to 7%
        :type investment: float, optional
        """
        account_amortization = {'age' : np.arange(self.age, age, 1)}
        duration = age - self.age 
        for account_key in self.accounts.keys():
            account_amortization[account_key] = self.accounts[account_key].compound_balance(
                duration, investment_return)

        amortization = pd.DataFrame(account_amortization)
        amortization['total'] = amortization.sum(axis=1)
        return amortization.iloc[-1].sum(), amortization

    
    def plot_assets(self, until_age=65, investment_return=7):
        _, amortized_assets = self.calculate_assets_at_age(until_age, investment_return)
        fig, ax = plt.subplots(figsize=(15, 8))
        legend = []
        for col in amortized_assets:
            if col != 'age':
                ax.plot(amortized_assets['age'], amortized_assets[col])
                ax.set_xlabel('Age')
                ax.set_ylabel('Total Value ($)')
                legend.append(col)

        fmt = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick) 
        ax.legend(legend)
        ax.grid()
        plt.show()


    def determine_taxes(self):
        # or something like this to figure out an investor's tax liability based on account contributions and salary
        pass
