from __future__ import annotations
import csv
import gc

def get_data(csvfile: str) -> list[tuple[str, float, float]]:
    """
    Return three list that contains the name of a stock, its price and its profit percentage.
    The first line of the csv file is ignored.
    """
    names, costs, profits = [], [], []
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row[0])>0 and float(row[1]) > 0 and float(row[2]) > 0:
                names.append(row[0])
                costs.append(float(row[1]))
                profits.append(float(row[2]))
    return names, costs, profits


def extract_best_shares(names: list[str], costs: list[float], profits: list[float], nb_shares: int=-1) -> tuple[list[str], list[float], list[float]]:
    """
    After having zipped the three lists provided as input, we sort by decreasing order of profits
    and return them by keeping only a certain number of elements
    """
    if nb_shares<len(names) and nb_shares>0:
        zipped = zip(profits, costs, names)
        sorted_desc = sorted(zipped, reverse=True)
        profits, costs, names = [list(elt)[:nb_shares] for elt in zip(*sorted_desc)]
    return names, costs, profits


def get_shares(csvfile:str, nb_shares:int=-1):
    """
    We recover from a csv a number of actions returned in the form of three lists (names, costs, profits)
    We free the non-referenced memory
    """
    names, costs, profits = get_data(csvfile)
    names, costs, profits = extract_best_shares(names, costs, profits, nb_shares)
    gc.collect()
    return names, costs, profits