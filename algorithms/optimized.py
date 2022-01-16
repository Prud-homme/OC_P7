from __future__ import annotations

def obtain_possible_investment(
    names: list[str],
    costs: list[float],
    profits: list[float],
    
    wallet: float,
    best_profit: list[float],
    best_investment: list[list[str]],

    node: int,
    profit_obtained: float,
    
    shares_purchased: list[str],
    
) -> None:
    """
    From a list of names, costs and profits of shares and a maximum amount of money (wallet) not to be exceeded,
    the function recursively calculates the best investment by storing the best profit obtained (best_profit)
    with the name of the shares purchased (best_investment).
    node allows to progress in the list of shares.
    profit_obtained stores the profit accumulation during the recursive calculation of an investment.
    shares_purchased stores the names of the shares purchased from an investment.
    """
    if node >= len(names):

        if best_profit[0] is None or profit_obtained >= best_profit[0]:

            best_profit[0] = profit_obtained
            best_investment[0] = shares_purchased.copy()

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
                new_wallet,
                best_profit,best_investment,
                
                
                node + 1,
                new_profit_obtained,
                
                new_shares_purchased,
                
            )

        obtain_possible_investment(
            names,
            costs,
            profits,
            wallet,
            best_profit,best_investment,
            node + 1,
            
            profit_obtained,
            
            shares_purchased,
            
        )


def optimized(
    names: list[str], costs: list[float], profits: list[float], wallet: float
) -> str:
    """
    calls the function to recursively calculate the best investment and generates a printable message containing the profit obtained and the name of the shares to buy
    best_profit and best_investment are lists so that these variables are mutable.
    """
    
    best_profit = [None]
    best_investment = [None]

    node = 0
    profit_obtained = 0
    shares_purchased = []
    
    obtain_possible_investment(
        names,
        costs,
        profits,
        
        wallet,
        best_profit,best_investment,

        node,
        profit_obtained,
        
        shares_purchased,
        
    )

    return f"""[Meilleur investissement] Gain de \x1b[35m{round(best_profit[0],2)}€\x1b[0m pour l'achat de:
\x1b[32m{', '.join(best_investment[0])}\x1b[0m"""