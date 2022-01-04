from __future__ import annotations


def optimized_invest(
    actions: list[tuple[str, int, int]],
    investment_mix: list[list[int]],
    profits: list[int],
    node: int,
    wallet: int,
    investment: list[int],
    profit_obtained: int,
) -> None:
    """
    The function recursively calculates the set of investments whose expenditure
    does not exceed a maximum value as well as the associated profits.
    Returns these two data as a list.
    """
    if node >= len(actions):
        investment_mix.append(investment)
        profits.append(profit_obtained)

    else:
        action_cost = actions[node][1]

        if wallet - action_cost > 0:
            action_profit = actions[node][2]
            profit = action_cost * action_profit / 100
            investment_1 = investment.copy()
            investment_1.append(1)
            optimized_invest(
                actions,
                investment_mix,
                profits,
                node + 1,
                wallet - action_cost,
                investment_1,
                profit_obtained + profit,
            )

        investment_0 = investment.copy()
        investment_0.append(0)
        optimized_invest(
            actions,
            investment_mix,
            profits,
            node + 1,
            wallet,
            investment_0,
            profit_obtained,
        )


def run(
    actions: list[tuple[str, int, int]], max_expenses: int
) -> tuple[list[list[int]], list[int]]:
    """
    The function returns the list of possible investments and the associated profits
    according to an algorithm optimized by the use of recursion.
    """
    profits = []
    investment_mix = []

    node = 0
    wallet = max_expenses
    investment = []
    profit_obtained = 0
    optimized_invest(
        actions, investment_mix, profits, node, wallet, investment, profit_obtained
    )
    return investment_mix, profits
