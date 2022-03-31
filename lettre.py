
def mystere (phrase):
    """
    The function counts the number of spaces in a string
    
    :param phrase: the phrase to be analyzed
    :return: The number of spaces in the phrase.
    """
    c = 0
    lng = len(phrase)
    for i in range(0, lng-1):
        if ord(phrase[i])== 32:
            c = c + 1
    return print(c)



def mystere_plus (phrase):
    """
    The function mystere_plus takes a string as an argument and returns the number of spaces and the
    number of words in the string
    
    :param phrase: the string to be analyzed
    :return: The number of spaces and the number of words.
    """
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

