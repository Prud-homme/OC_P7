import time
import utils
from settings import MAX_EXPENSES, ACTIONS
from algorithms.bruteforce import run as run_bruteforce
from algorithms.optimized import run as run_optimized


def run(actions):
    for function in [run_bruteforce, run_optimized]:
        start_time = time.time()
        investment_mix, profits = function(actions, MAX_EXPENSES)
        end_time = time.time() - start_time
        print("--- %s seconds ---" % (end_time))
        print(utils.display_investment(actions, profits, investment_mix))

    # print(utils.display_distributions(actions, profits, investment_mix,100))

    new_actions = utils.conditions_remove(actions)
    start_time = time.time()
    investment_mix, profits = run_optimized(new_actions, MAX_EXPENSES)
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    print(utils.display_investment(new_actions, profits, investment_mix))


run(ACTIONS)
