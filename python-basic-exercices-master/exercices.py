"""
Exercices.

Implémentez les méthodes ci-dessous.
Pour executer vos tests il vous faudra utiliser pytest
"""


import math


def htc_to_ttc(htc_cost: float, discount_rate: float = 0) -> float:
    """
    Exercice 1 :
    Calcule le coût TTC d'un produit.
    discount_rate : taux de réduction compris entre 0 et 1
    Taux de taxes : 20.6 %
    Retourne un float arrondi à deux décimales
    """
    if discount_rate < 0 or discount_rate > 1:
        raise Exception
    ttc_cost = round(htc_cost * 1.206 * (1 - discount_rate), 2)
    return ttc_cost


def divisors(value: int = 0):
    """
    Exercice 2 :
    A partir d'un nombre donné,
    retourne ses diviseurs (sans répétition)
    s’il y en a, ou « PREMIER » s’il n’y en a pas.
    """

    """
    PRIME_NUMBER_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                         211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                         307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                         401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                         503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                         601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                         701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                         809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                         907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,]
    """

    divisors_set = []

    initial_value = value

    if value == 0:
        return "All integer numbers different from 0 are divisors of 0"
    elif value == 1:
        return "ONE"
    elif value < 0:
        return "The value should be positive integer"
    else:
        # if the number is 2
        if value == 2:
            return "PREMIER"
        else:
            # number of two's that divide n
            while value % 2 == 0:
                divisors_set.append(2)
                value = value / 2

            # n must be odd at this point
            # so a skip of 2 ( i = i + 2) can be used
            for i in range(3, int(math.sqrt(value)) + 1, 2):
                # while i divides n , print i ad divide n
                while value % i == 0:
                    divisors_set.append(i)
                    value = value / i

            if 2 < value < initial_value:
                divisors_set.append(value)

    if len(divisors_set) == 0:
        return "PREMIER"
    else:
        return set(divisors_set)
