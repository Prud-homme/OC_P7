from __future__ import annotations
import numpy as np


def vanilla_bruteforce_without_sale(names, cost, profit, max_expenses):
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

    profits = [sum([expenses[i][j] * profit[j] / 100 for j in range(len(profit))]) for i in range(len(expenses))]
    best_choice = profits.index(max(profits))

    message = f"""Actions à acheter :
{', '.join([names[i] for i in range(len(expenses[best_choice])) if expenses[best_choice][i]>0])}

Gain total d'investissement : {round(profits[best_choice],2)}€"""
    return message


def numpy_bruteforce_without_sale(names,cost, profit, max_expenses):
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

    profits = np.sum(np.multiply(np.array(expenses), profit/100), axis=1)
    best_choice = np.argmax(profits)

    message = f"""Actions à acheter :
{', '.join(names[np.array(expenses[best_choice])>0])}

Gain total d'investissement : {np.round(profits[best_choice],2)}€"""
    return message











def numpy_bruteforce_with_sale(names,cost, profit, max_expenses):
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

    profits = np.sum(np.multiply(np.array(expenses), profit/100), axis=1) + 500 - np.sum(np.array(expenses), axis=1)
    
    best_choice = np.argmax(profits)

    message = f"""Actions à acheter :
{', '.join(names[np.array(expenses[best_choice])>0])}

Gain total d'investissement : {np.round(profits[best_choice],2)}€"""
    return message
    #profits = [[expenses[i][j] * profit[j] for j in range(len(profit))] for i in range(len(expenses))]
    #return profits



def vanilla_bruteforce_with_sale(names,cost, profit, max_expenses):
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

    profits = [sum([expenses[i][j] * profit[j] / 100 for j in range(len(profit))]) + 500 - sum(expenses[i]) for i in range(len(expenses))]
    best_choice = profits.index(max(profits))

    message = f"""Actions à acheter :
{', '.join([names[i] for i in range(len(expenses[best_choice])) if expenses[best_choice][i]>0])}

Gain total d'investissement : {round(profits[best_choice],2)}€"""
    return message






