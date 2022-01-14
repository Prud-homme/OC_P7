from __future__ import annotations


def invest(
    actions: list[tuple[str, int, int]], investment: list[int], max_expenses: int
) -> tuple[bool, int]:
    """
    The function calculates the profit and expense for an investment of shares.
    Returns a boolean to know if the expense is lower than the defined max and the associated profit
    """
    expenses = 0
    profit = 0
    for i in range(len(actions)):
        action_cost = actions[i][1]
        action_profit = actions[i][2]
        expenses += action_cost * investment[i]
        profit += action_cost * investment[i] * action_profit / 100
    return expenses <= max_expenses, profit



def bruteforce_invest_nested_for(
    actions: list[tuple[str, int, int]], max_expenses: int
) -> tuple[list[list[int]], list[int]]:
    """
    The function calculates for all possible investments the profit
    and the expense associated with each of these investments.
    Returns a list of investments whose expense does not exceed
    a maximum value and a list of associated profit
    """
    investment_mix = []
    profits = []
    for i1 in (0, 1):
        for i2 in (0, 1):
            for i3 in (0, 1):
                for i4 in (0, 1):
                    for i5 in (0, 1):
                        for i6 in (0, 1):
                            for i7 in (0, 1):
                                for i8 in (0, 1):
                                    for i9 in (0, 1):
                                        for i10 in (0, 1):
                                            for i11 in (0, 1):
                                                for i12 in (0, 1):
                                                    for i13 in (0, 1):
                                                        for i14 in (0, 1):
                                                            for i15 in (0, 1):
                                                                for i16 in (0, 1):
                                                                    for i17 in (0, 1):
                                                                        for i18 in (0,1):
                                                                            for i19 in (0,1):
                                                                                for i20 in (0,1):
                                                                                    investment = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20]
                                                                                    valid_expenses, profit = invest(actions, investment, max_expenses)
                                                                                    if valid_expenses:
                                                                                        investment_mix.append(investment)
                                                                                        profits.append(profit)
    return investment_mix, profits


import time
def bruteforce_invest_while(
    actions: list[tuple[str, int, int]], max_expenses: int
) -> tuple[list[list[int]], list[int]]:
    """
    The function calculates for all possible investments the profit
    and the expense associated with each of these investments.
    Returns a list of investments whose expense does not exceed
    a maximum value and a list of associated profit
    """
    
    action_i = 0
    nb_actions = len(actions)
    investments = [[0],[1]]
    index = 0
    choice = 0
    new_investments = []
    while action_i < nb_actions-1:
        
        new_investment = investments[index].copy()
        new_investment.append(choice)
        new_investments.append(new_investment)

        if choice == 1:
            index += 1

        if choice == 0:
            choice += 1
        else:
            choice -= 1

        if index == len(investments):
            action_i += 1

            index=0
            investments = new_investments
            new_investments = []

    investment_mix = []
    profits = []

    #start_time = time.time()

    for investment in investments:
        valid_expenses, profit = invest(actions, investment, max_expenses)
        if valid_expenses:
            investment_mix.append(investment)
            profits.append(profit)
    
    #end_time = time.time() - start_time
    #print("--- %s seconds ---" % (end_time))
    return investment_mix, profits

import numpy as np
def bruteforce_invest_whilev2(cost, profit, max_expenses):
    """
    The function calculates for all possible investments the profit
    and the expense associated with each of these investments.
    Returns a list of investments whose expense does not exceed
    a maximum value and a list of associated profit
    """
    nb_actions = len(cost)

    action_i = 0
    
    expenses = [[]]
    
    index = 0
    choice = 0
    new_expenses = []
    while action_i < nb_actions:
        
        new_expense = expenses[index].copy()
        cost_i = cost[action_i]
        
        if sum(new_expense) + cost_i <= max_expenses:
            new_expense.append(choice * cost_i)
            new_expenses.append(new_expense)

        if choice == 1:
            choice -= 1
            index += 1
        else:
            choice += 1            

        if index == len(expenses):
            action_i += 1

            index=0
            expenses = new_expenses
            new_expenses = []

    profits = np.multiply(np.array(expenses), profit/100)
    #profits = [[expenses[i][j] * profit[j] for j in range(len(profit))] for i in range(len(expenses))]
    return profits



from joblib import Parallel, delayed

def check_invest(actions, investment, max_expenses,investment_mix,profits):
    valid_expenses, profit = invest(actions, investment, max_expenses)
    if valid_expenses:
        return investment, profit

def bruteforce_invest_while_thread(
    actions: list[tuple[str, int, int]], max_expenses: int
) -> tuple[list[list[int]], list[int]]:
    """
    The function calculates for all possible investments the profit
    and the expense associated with each of these investments.
    Returns a list of investments whose expense does not exceed
    a maximum value and a list of associated profit
    """
    
    action_i = 0
    nb_actions = len(actions)
    investments = [[0],[1]]
    index = 0
    choice = 0
    new_investments = []
    while action_i < nb_actions-1:
        
        new_investment = investments[index].copy()
        new_investment.append(choice)
        new_investments.append(new_investment)

        if choice == 1:
            index += 1

        if choice == 0:
            choice += 1
        else:
            choice -= 1

        if index == len(investments):
            action_i += 1

            index=0
            investments = new_investments
            new_investments = []

    investment_mix = []
    profits = []
    start_time = time.time()

    test = Parallel(n_jobs=-1)(delayed(check_invest)(actions, investment, max_expenses,investment_mix,profits) for investment in investments)

    
    investment_mix, profits = zip(*[elt for elt in test if elt is not None])
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    return investment_mix, profits
    





def run_nested_for(actions: list[tuple[str, int, int]], max_expenses: int):
    """
    The function returns the list of possible investments and
    the associated profits according to a brute-force algorithm
    """
    investment_mix, profits = bruteforce_invest_nested_for(actions, max_expenses)
    return investment_mix, profits

def run_while(actions: list[tuple[str, int, int]], max_expenses: int):
    """
    The function returns the list of possible investments and
    the associated profits according to a brute-force algorithm
    """
    investment_mix, profits = bruteforce_invest_while(actions, max_expenses)
    return investment_mix, profits

def run_while_thread(actions: list[tuple[str, int, int]], max_expenses: int):
    """
    The function returns the list of possible investments and
    the associated profits according to a brute-force algorithm
    """
    investment_mix, profits = bruteforce_invest_while_thread(actions, max_expenses)
    return investment_mix, profits




def run_whilev2(actions: list[tuple[str, int, int]], max_expenses: int):
    """
    The function returns the list of possible investments and
    the associated profits according to a brute-force algorithm
    """
    profits = bruteforce_invest_whilev2(cost, profit, max_expenses)
    return profits




import numpy as np
def bruteforce_invest_while_numpy(cost, profit, max_expenses):
#    actions: list[tuple[str, int, int]], max_expenses: int
#) -> tuple[list[list[int]], list[int]]:
    """
    The function calculates for all possible investments the profit
    and the expense associated with each of these investments.
    Returns a list of investments whose expense does not exceed
    a maximum value and a list of associated profit
    """
    
    action_i = 0
    nb_actions = len(cost)
    investments = [[0],[1]]
    index = 0
    choice = 0
    new_investments = []
    while action_i < nb_actions-1:
        
        new_investment = investments[index].copy()
        new_investment.append(choice)
        new_investments.append(new_investment)

        if choice == 1:
            index += 1

        if choice == 0:
            choice += 1
        else:
            choice -= 1

        if index == len(investments):
            action_i += 1

            index=0
            investments = new_investments
            new_investments = []


    #start_time = time.time()
    expenses = np.multiply(investments,cost)
    print(len(expenses))
    exp_i = np.where(expenses <= max_expenses)
    print(exp_i)

    #print([sum(elt2) for elt1, elt2 in test])
    investment_mix = np.array([invest for invest, invest_cost in [investments, np.multiply(investments,cost)] if sum(invest_cost)<=max_expenses])
    
    profits = np.multiply(investment_mix, profit/100)

    
    
    #end_time = time.time() - start_time
    #print("--- %s seconds ---" % (end_time))
    return investment_mix, profits




def run_while_numpy(cost,profit,max_expenses):
    """
    The function returns the list of possible investments and
    the associated profits according to a brute-force algorithm
    """
    investment_mix, profits = bruteforce_invest_while_numpy(cost,profit,max_expenses)
    return investment_mix, profits





'''
remplacer 1 par cout action
ajouter invest si sum < 500


ou append ([cout action], [0,1])

ne pas tenir compte 0 et 1 
seulement compter depenses et profit action est prise si il y a un profit
'''