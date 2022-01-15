from __future__ import annotations


def obtain_possible_investment(
    names: list[str],
    costs: list[float],
    profits: list[float],
    node: int,
    wallet: float,
    profit_obtained: float,
    investment_earnings: list[float],
    shares_purchased: list[str],
    all_investments: list[list[str]],
) -> None:
    """
    The function recursively calculates the set of investments whose expenditure
    does not exceed a maximum value as well as the associated profits.
    Returns these two data as a list.
    """
    if node >= len(names):
        investment_earnings.append(profit_obtained)
        all_investments.append(shares_purchased)

    else:
        share_cost = costs[node]
        new_wallet = wallet - share_cost
        if new_wallet >= 0:
            new_profit_obtained = profit_obtained + share_cost * profits[node] / 100

            new_shares_purchased = shares_purchased.copy()
            new_shares_purchased.append(names[node])

            obtain_possible_investment(
                names,
                costs,
                profits,
                node + 1,
                new_wallet,
                new_profit_obtained,
                investment_earnings,
                new_shares_purchased,
                all_investments,
            )

        obtain_possible_investment(
            names,
            costs,
            profits,
            node + 1,
            wallet,
            profit_obtained,
            investment_earnings,
            shares_purchased,
            all_investments,
        )


def printable_result(
    investment_earnings: list[float], all_investments: list[list[str]]
) -> str:
    """Generates a message displaying the stocks to buy to maximize profits"""
    best_choice = investment_earnings.index(max(investment_earnings))

    return f"""[Meilleur investissement] Gain de {round(investment_earnings[best_choice],2)}€ pour l'achat de:
{', '.join(all_investments[best_choice])}"""


def optimized(
    names: list[str], costs: list[float], profits: list[float], wallet: float
) -> str:
    """
    The function returns the list of possible investments and the associated profits
    according to an algorithm optimized by the use of recursion.
    """
    node = 0
    profit_obtained = 0
    investment_earnings = []
    shares_purchased = []
    all_investments = []
    obtain_possible_investment(
        names,
        costs,
        profits,
        node,
        wallet,
        profit_obtained,
        investment_earnings,
        shares_purchased,
        all_investments,
    )
    return printable_result(investment_earnings, all_investments)