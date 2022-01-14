import time
import utils
from settings import MAX_EXPENSES, ACTIONS
from algorithms.bruteforce import *
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

'''##############
start_time = time.time()
investment_mix, profits = run_bruteforce_while(actions, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
start_time = time.time()
print(utils.display_investment(actions, profits, investment_mix))
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
'''#################



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

'''
start_time = time.time()
investment_mix, profits = run_bruteforce_whilenp(cost,profit, MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(profits)
print(utils.display_investment(actions, profits, investment_mix))
'''
'''

start_time = time.time()
profits = run3(cost,profit,MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
'''








start_time = time.time()
msg = numpy_bruteforce_without_sale(names,cost,profit,MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(msg)
'''
start_time = time.time()
msg = run5(names,cost,profit,MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(msg)
'''





import numpy as np
profit = np.array([1+elt for elt in cost])

'''
start_time = time.time()
msg = run4(names,cost,profit,MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(msg)

start_time = time.time()
msg = run5(names,cost,profit,MAX_EXPENSES)
end_time = time.time() - start_time
print("--- %s seconds ---" % (end_time))
print(msg)
'''
