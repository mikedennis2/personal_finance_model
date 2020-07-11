import numpy_financial as npf 
import numpy as np

class InvestmentAccount:
    def __init__(self, name, init_balance, contribution_yearly, divident_yield):
        self.name = name
        self.balance = init_balance
        self.yearly_contribution = contribution_yearly
        self.divident_yield = divident_yield
        self.future_value_array = None 


    def compound_balance(self, duration_years, rate_percent):
        try:
            # Balance could be an array or a number
            pv = self.balance[0]
        except TypeError:
            pv = self.balance 

        try:
            rate_array_len = len(rate_percent)
            if rate_array_len != duration_years:
                raise RuntimeError('Incorrect array size for the given duration')
            rate_array = rate_percent / 100
        except:
            rate_array = np.ones(duration_years) * rate_percent / 100

        # Compound the contributions over the duration, including the divident/distribution yield
        future_value_array = np.zeros(rate_array.size)
        future_value_array[0] = pv
        for i in range(1, duration_years):
            additional_investment = future_value_array[i - 1] * self.divident_yield + self.yearly_contribution
            value_for_compounding = future_value_array[i - 1] + additional_investment
            future_value_array[i] = value_for_compounding * (1 + rate_array[i - 1])
        self.future_value_array = future_value_array
        return future_value_array



class PretaxRetirement(InvestmentAccount):
    """This class represents a pre tax retirement account such as a 401k or traditional IRA
    """
    pass


class TaxableBrokerage(InvestmentAccount):
    """This class represents a person's taxable brokerage account.
    """
    pass


class RothAccount(InvestmentAccount):
    """This class represents a roth basis account (roth 401k or IRA).
    """
    pass


class HealthSavingsAccount(InvestmentAccount):
    pass