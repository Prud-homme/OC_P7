from __future__ import annotations


def obtain_possible_investment(costs: list[float], wallet: float) -> list[list[float]]:
    """
    Generates the set of possible investments for different shares within a maximum expenditure.
    We have the cost of each action as well as the maximum amount that should not be exceeded.
    It returns a list where each element is a list of floats that correspond
    to the purchase cost of the shares.
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

    return [expense for expense in expenses if sum(expense) > 0]


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
        sum([expenses[i][j] * profits[j] for j in range(len(profits))]) / 100
        for i in range(len(expenses))
    ]

    best_invest = investment_earnings.index(max(investment_earnings))
    profit = round(investment_earnings[best_invest], 2)
    shares = "\n".join(
        [
            names[i]
            for i in range(len(expenses[best_invest]))
            if expenses[best_invest][i] > 0
        ]
    )

    return f"""Recommended investment:
{shares}

Total cost: {sum(expenses[best_invest])}€
Total return: {profit}€"""
