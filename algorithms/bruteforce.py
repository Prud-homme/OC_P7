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


def bruteforce_invest(
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
                                                                        for i18 in (
                                                                            0,
                                                                            1,
                                                                        ):
                                                                            for i19 in (
                                                                                0,
                                                                                1,
                                                                            ):
                                                                                for (
                                                                                    i20
                                                                                ) in (
                                                                                    0,
                                                                                    1,
                                                                                ):
                                                                                    investment = [
                                                                                        i1,
                                                                                        i2,
                                                                                        i3,
                                                                                        i4,
                                                                                        i5,
                                                                                        i6,
                                                                                        i7,
                                                                                        i8,
                                                                                        i9,
                                                                                        i10,
                                                                                        i11,
                                                                                        i12,
                                                                                        i13,
                                                                                        i14,
                                                                                        i15,
                                                                                        i16,
                                                                                        i17,
                                                                                        i18,
                                                                                        i19,
                                                                                        i20,
                                                                                    ]
                                                                                    (
                                                                                        valid_expenses,
                                                                                        profit,
                                                                                    ) = invest(
                                                                                        actions,
                                                                                        investment,
                                                                                        max_expenses,
                                                                                    )
                                                                                    if valid_expenses:
                                                                                        investment_mix.append(
                                                                                            investment
                                                                                        )
                                                                                        profits.append(
                                                                                            profit
                                                                                        )
    return investment_mix, profits


def run(actions: list[tuple[str, int, int]], max_expenses: int):
    """
    The function returns the list of possible investments and
    the associated profits according to a brute-force algorithm
    """
    investment_mix, profits = bruteforce_invest(actions, max_expenses)
    return investment_mix, profits
