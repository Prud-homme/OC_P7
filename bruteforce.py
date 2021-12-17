import time

ACTIONS = [
    (20, 5),
    (30, 10),
    (50, 15),
    (70, 20),
    (60, 17),
    (80, 25),
    (22, 7),
    (26, 11),
    (48, 13),
    (34, 27),
    (42, 17),
    (110, 9),
    (38, 23),
    (14, 1),
    (18, 3),
    (8, 8),
    (4, 12),
    (10, 14),
    (24, 21),
    (114, 18),
]

def action(combinaison):
    somme=0
    gain=0
    for i in range(len(combinaison)):
        somme += ACTIONS[i][0]*combinaison[i]
        gain += ACTIONS[i][0]*ACTIONS[i][1]*combinaison[i]/100
    return somme <= 500, gain

def bruteforce():
    listes=[]
    gains=[]
    for i1 in (0,1):
        for i2 in (0,1):
            for i3 in (0,1):
                for i4 in (0,1):
                    for i5 in (0,1):
                        for i6 in (0,1):
                            for i7 in (0,1):
                                for i8 in (0,1):
                                    for i9 in (0,1):
                                        for i10 in (0,1):
                                            for i11 in (0,1):
                                                for i12 in (0,1):
                                                    for i13 in (0,1):
                                                        for i14 in (0,1):
                                                            for i15 in (0,1):
                                                                for i16 in (0,1):
                                                                    for i17 in (0,1):
                                                                        for i18 in (0,1):
                                                                            for i19 in (0,1):
                                                                                for i20 in (0,1):
                                                                                    combinaison = [i1, i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20]
                                                                                    booleen, gain = action(combinaison)
                                                                                    if booleen:
                                                                                        listes.append(combinaison)
                                                                                        gains.append(gain)
    return listes,gains



def run():
    listes2, gains2 = bruteforce()
    return listes2, gains2

def display(listes, gains):
    indexs = list(range(len(gains)))
    zipped_lists = zip(gains, indexs)
    sorted_pairs = sorted(zipped_lists, reverse=True)
    tuples = zip(*sorted_pairs)
    list1, list2 = [list(tuple) for tuple in tuples]

    chaine = [f"Action {i+1}" for i in range(20) if listes[list2[0]][i] == 1]

    message = f"""
Actions à acheter :
{', '.join(chaine)}

Gain total d'investissement : {round(gains[list2[0]], 2)}€"""
    
    '''
    nb = 2500
    temp = [listes[elt] for elt in list2[:nb]]
    aux = [sum(x) for x in zip(*temp)]
    print([round(x/nb*100,1) for x in aux])
    '''
    return message


def main():
    start_time = time.time()
    listes, gains = run()
    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    print(display(listes, gains))


main()
