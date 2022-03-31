from random import randint


def creer_paquet(n):
    """
    Create a list of integers from 1 to n
    
    :param n: the number of cards in the deck
    :return: A list of integers from 1 to n.
    """
    paq = [i for i in range (1, 1, n+1)]
    return paq


def melanger_paquet(p):
    n = len(p)
    for k in range (2*n) :
        i = randint (0, n-1)
        j = randint (0, n-1)
        temp = p[i]
        p[i] = p[j]
        p[j] = temp
    return p
