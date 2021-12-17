import time

# ( <=5% ) ou ( <=10% et +100€ )
ACTIONS = [
#    (20, 5),
    (30, 10),
    (50, 15),
    (70, 20),
    (60, 17),
    (80, 25),
#    (22, 7),
    (26, 11),
    (48, 13),
    (34, 27),
    (42, 17),
#    (110, 9),
    (38, 23),
#    (14, 1),
#    (18, 3),
    (8, 8),
    (4, 12),
    (10, 14),
    (24, 21),
    (114, 18),
]


def parcours(listes, gains, noeud, portefeuille, liste, gain):
    if noeud >= len(ACTIONS):
        listes.append(liste)
        gains.append(gain)

    else:
        cout = ACTIONS[noeud][0]

        if portefeuille - cout > 0:
            benefice = cout * ACTIONS[noeud][1] / 100
            liste_1 = liste.copy()
            liste_1.append(1)
            parcours(listes, gains, noeud + 1, portefeuille - cout, liste_1, gain + benefice)

        liste_0 = liste.copy()
        liste_0.append(0)
        parcours(listes, gains, noeud + 1, portefeuille, liste_0, gain)


def run():
    gains = []
    listes = []

    noeud = 0
    portefeuille = 500
    liste = []
    gain = 0
    parcours(listes, gains, noeud, portefeuille, liste, gain)
    return listes, gains


def display(listes, gains):
    indexs = list(range(len(gains)))
    zipped_lists = zip(gains, indexs)
    sorted_pairs = sorted(zipped_lists, reverse=True)
    tuples = zip(*sorted_pairs)
    list1, list2 = [list(tuple) for tuple in tuples]

    chaine = [f"Action {i+1}" for i in range(len(ACTIONS)) if listes[list2[0]][i] == 1]

    message = f"""
Actions à acheter :
{', '.join(chaine)}

Gain total d'investissement : {round(gains[list2[0]], 2)}€"""
    return message


def main():
    start_time = time.time()
    listes, gains = run()
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    print(display(listes, gains))


main()
