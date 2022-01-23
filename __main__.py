from __future__ import annotations

from algorithms.bruteforce import bruteforce
from algorithms.optimized import optimized
from utils import get_shares, open_csv, write_results


def run_with_comparision(
    max_expenses: int, names: list[str], costs: list[float], profits: list[float]
) -> None:
    """Compare execution time and memory consumption with bruteforce and optimized algorithms"""
    import time
    import tracemalloc

    print("\n--- Bruteforce ---")
    start_time = time.time()
    tracemalloc.start()
    result = bruteforce(names, costs, profits, max_expenses)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time() - start_time
    print(result)
    print("\x1b[36m--- Résultat obtenu en %s seconds ---" % (end_time))
    print(
        f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB\x1b[0m"
    )

    print("\n--- Optimized ---")
    start_time = time.time()
    tracemalloc.start()
    result = optimized(names, costs, profits, max_expenses)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time() - start_time
    print(result)
    print("\x1b[36m--- Résultat obtenu en %s seconds ---" % (end_time))
    print(
        f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB\x1b[0m"
    )


if __name__ == "__main__":
    import os

    os.system("cls")
    max_expenses = 500
    input(
        """Maximum expense set at 500€.
Press enter and choose a file which contains shares name, cost and profit."""
    )
    csvfile = open_csv()

    names, costs, profits = get_shares(csvfile, max_expenses, 20)
    result = optimized(names, costs, profits, max_expenses)

    textfile = csvfile[:-4] + "_results.txt"
    write_results(textfile, result)

    print(result, f"\nResult export in {textfile}")
