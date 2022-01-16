from __future__ import annotations


def obtain_possible_investment(costs: list[float], wallet: float) -> list[list[float]]:
    """
    Generates the set of possible investments for different shares within a maximum expenditure.
    We have the cost of each action as well as the maximum amount that should not be exceeded.
    It returns a list where each element is a list of floats that correspond to the purchase cost of the shares.
    """
    nb_shares = len(costs)
    action_i = 0

    expenses = [[]]

    index = 0
    choice = 0
    new_expenses = []
    while action_i < nb_shares:

        new_expense = expenses[index].copy()
        cost_i = choice * costs[action_i]

        if sum(new_expense) + cost_i <= wallet:
            new_expense.append(cost_i)
            new_expenses.append(new_expense)

        if choice == 1:
            choice -= 1
            index += 1
        else:
            choice += 1

        if index == len(expenses):
            action_i += 1
            index = 0
            expenses = new_expenses
            new_expenses = []

    return expenses


def bruteforce(
    names: list[str], costs: list[float], profits: list[float], wallet: float
) -> str:
    """
    Calls obtain_possible_investment() to calculate itteratively the set of feasible investments
    and, after finding the best investment among this list, generates a printable message
    containing the profit obtained and the name of the shares to buy for this investment
    """
    expenses = obtain_possible_investment(costs, wallet)

    investment_earnings = [
        sum([expenses[i][j] * profits[j] / 100 for j in range(len(profits))])
        for i in range(len(expenses))
    ]

    best_choice = investment_earnings.index(max(investment_earnings))
    return f"""[Meilleur investissement] Gain de \x1b[35m{round(investment_earnings[best_choice],2)}€\x1b[0m pour l'achat de:
\x1b[32m{', '.join([names[i] for i in range(len(expenses[best_choice])) if expenses[best_choice][i]>0])}\x1b[0m"""
