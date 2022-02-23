def permutlignes(tab = [[1,2,3], [4,5,6],[7,8,9]]):
    # Cette fonction permute les lignes l1 et l2 du tableau tab
    n = len(tab[0])
    for i in range(n):
        temp = tab[0][0]
        tab[0][i] = tab[1][i]
        tab[1][0] = temp
    return tab

print(permutlignes())


