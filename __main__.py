import time
import utils
from settings import MAX_EXPENSES, ACTIONS
from algorithms.bruteforce import run_nested_for as run_bruteforce_nested_for
from algorithms.bruteforce import bruteforce_invest_while as run_bruteforce_while
from algorithms.bruteforce import bruteforce_invest_whilev2 as run_bruteforce_whilev2
from algorithms.bruteforce import run_while_numpy as run_bruteforce_whilenp
from algorithms.bruteforce import run_while_thread as run_bruteforce_while_thread
from algorithms.optimized import run as run_optimized


def run(actions):
    for function in [run_bruteforce, run_optimized]:
        start_time = time.time()
        investment_mix, profits = function(actions, MAX_EXPENSES)
        end_time = time.time() - start_time
        print("--- %s seconds ---" % (end_time))
        print(utils.display_investment(actions, profits, investment_mix))

    # print(utils.display_distributions(actions, profits, investment_mix,100))
    '''
    new_actions = utils.conditions_remove(actions)
    start_time = time.time()
    investment_mix, profits = run_optimized(new_actions, MAX_EXPENSES)
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    print(utils.display_investment(new_actions, profits, investment_mix))
    '''


#run(ACTIONS)
'''
actions = utils.get_data("dataset1.csv")
new_actions = utils.conditions_remove(actions)
start_time = time.time()
investment_mix, profits = run_optimized(new_actions, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(utils.display_investment(new_actions, profits, investment_mix))
'''
actions = ACTIONS

'''
start_time = time.time()
investment_mix, profits = run_bruteforce_nested_for(actions, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(utils.display_investment(actions, profits, investment_mix))
'''


start_time = time.time()
investment_mix, profits = run_bruteforce_while(actions, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
start_time = time.time()
print(utils.display_investment(actions, profits, investment_mix))
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
'''
start_time = time.time()
investment_mix, profits = run_bruteforce_while_thread(actions, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(utils.display_investment(actions, profits, investment_mix))
'''

import numpy as np
from utils import get_data_numpy

names, cost, profit = get_data_numpy('dataset.csv')
'''
print(names)
print(cost)
print(profit)
somme = 0
start_time = time.time()
for i in range(len(cost)):
    somme += cost[i] * profit[i]
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(somme)

somme = 0
start_time = time.time()
somme = sum(np.multiply(cost,profit))
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(somme)
'''




start_time = time.time()
profits = run_bruteforce_whilev2(cost,np.array(profit),MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
start_time = time.time()
print(utils.display_investment_np(names, profits))
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))


'''
start_time = time.time()
investment_mix, profits = run_bruteforce_whilenp(cost,profit, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(profits)
print(utils.display_investment(actions, profits, investment_mix))
'''