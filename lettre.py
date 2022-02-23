
def mystere (phrase):
    c = 0
    lng = len(phrase)
    for i in range(0, lng-1):
        if ord(phrase[i])== 32:
            c = c + 1
    return print(c)



def mystere_plus (phrase):
    c = 0
    m = 0
    lng = len(phrase)
    for i in range(0, lng-1):
        if ord(phrase[i])== 32:
            c = c + 1
            m = m + 1
    nbr_mots = m + 1
    return print(c, "\nIl y a", nbr_mots, "mots")

mystere_plus("Bonne journée à tous")

