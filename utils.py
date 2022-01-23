from __future__ import annotations

import csv
from typing import Optional


def get_data(csvfile: str, max_expenses: int) -> list[tuple[str, float, float]]:
    """
    Return three list that contains the name of a stock, its price and its profit percentage.
    The first line of the csv file is ignored.
    """
    names, costs, profits = [], [], []
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[0]
            cost = float(row[1])
            profit = float(row[2])
            if len(name) > 0 and cost > 0 and cost <= max_expenses and profit > 0:
                names.append(name)
                costs.append(cost)
                profits.append(profit)
    return names, costs, profits


def extract_best_shares(
    names: list[str],
    costs: list[float],
    profits: list[float],
    nb_shares: Optional[int] = None,
) -> tuple[list[str], list[float], list[float]]:
    """
    After having zipped the three lists provided as input, we sort by decreasing order of profits
    and return them by keeping only a certain number of elements
    """
    if (
        nb_shares is not None
        and isinstance(nb_shares, int)
        and nb_shares < len(names)
        and nb_shares > 0
    ):
        zipped = zip(profits, costs, names)
        sorted_desc = sorted(zipped, reverse=True)
        profits, costs, names = [list(elt)[:nb_shares] for elt in zip(*sorted_desc)]
    return names, costs, profits


def get_shares(csvfile: str, max_expenses: int, nb_shares: Optional[int] = None):
    """
    We recover from a csv a number of actions returned in the form of three lists (names, costs, profits)
    We free the non-referenced memory
    """
    names, costs, profits = get_data(csvfile, max_expenses)
    names, costs, profits = extract_best_shares(names, costs, profits, nb_shares)
    return names, costs, profits


def write_results(textfile: str, text_to_write: str) -> None:
    """Write investment result in a file"""
    f = open(textfile, "w")
    f.write(text_to_write)
    f.close()


def open_csv():
    """Window (GUI) for open a file"""
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path
