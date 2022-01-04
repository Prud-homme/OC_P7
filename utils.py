from __future__ import annotations
import csv


def get_data(csvfile: str) -> list[tuple[str, float, float]]:
    """
    Return a list of tuples where each tuple contains
    the name of a stock, its price and its profit percentage.
    The first line of the csv file is ignored.
    """
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append((row[0], float(row[1]), float(row[2])))
    return data


def sort_by_profit(profits: list[int]) -> list[int]:
    """
    The function zips the list of profits with a list of indexes of the same size.
    A sorting by descending order of the profits is done on this zip.
    The index list allows to keep track of the sorting.
    The list of sorted indexes is returned.
    """
    indexs = list(range(len(profits)))
    zipped = zip(profits, indexs)
    sorted_by_profit = sorted(zipped, reverse=True)
    tuples = zip(*sorted_by_profit)
    sort_profits, sort_choices = [list(elt) for elt in tuples]
    return sort_choices


def display_investment(
    actions: list[tuple[str, int, int]],
    profits: list[int],
    investment_mix: list[list[int]],
) -> str:
    """
    Return a string containing the actions to take in order to
    maximize the profit and the profit obtained.
    """
    best_choice = sort_by_profit(profits)[0]
    chaine = [
        f"Action {actions[i][0]}"
        for i in range(len(actions))
        if investment_mix[best_choice][i] == 1
    ]

    message = f"""Actions à acheter :
{', '.join(chaine)}

Gain total d'investissement : {round(profits[best_choice], 2)}€"""
    return message


def display_distributions(
    actions: list[tuple[str, int, int]],
    profits: list[int],
    investment_mix: list[list[int]],
    nb: int,
) -> str:
    """
    Return a string containing the actions to take in order to
    maximize the profit and the profit obtained.
    """
    if nb > len(investment_mix):
        return None
    best_choices = sort_by_profit(profits)[:nb]
    investments = [investment_mix[choice] for choice in best_choices]
    distributions = [sum(x) for x in zip(*investments)]
    chaine = [
        f"{actions[i]} : {round(distributions[i]/nb*100,1)}"
        for i in range(len(actions))
    ]

    return "\n".join(chaine)


def conditions_remove(
    actions: list[tuple[str, int, int]]
) -> list[tuple[str, int, int]]:
    """
    Generates a new action list where for each action, it must yield
    more than 5% or more than 10% if its cost is greater than 100
    """
    new_actions = []
    for i in range(len(actions)):
        action_cost = actions[i][1]
        action_profit = actions[i][2]
        if action_profit > 5 or action_profit > 10 and action_cost > 100:
            new_actions.append(actions[i])

    return new_actions
