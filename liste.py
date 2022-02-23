def tab_cours():
    eb = [[1,2,3],[4,5,6]]

    t = [[0 for j in range (4)] for i in range (6)] #Équivalent de cette ligne de code en dessous
    '''Pour i allant de 0 à 5: # <-- [0 for j in range (4)]
            Pour j allant de 0 à 3 : # <-- for i in range (6)
            t[i][0] = 0
    '''

def createTab(n,p):
    "Initialiser un tableau de n lignes et P colones à 0"
    t = [[0 for j in range (p)] for i in range (n)]
    return t


def carre_mag(n):
    i = 0
    j=n//2
    t= createTab(n, n)
    t[i][j] = 1
    for k in range (2, n*n+1):
        i = i -1
        j = j-1
        if j >= 0 and i < 0:
            i = n-1
            t[i][j]= k
        elif i>=0 and j < 0:
            j = n-1
            t[i][j] = k
        elif i>=0 and j>=0 and t[i][j]!=0:
            i=i+2
            j=j+1
            t[i][j]=k
        elif i>=0 and j>=0 and t[i][j]==0:
            t[i][j]=k
        else:
            i=1
            j=0
            t[i][j]=k
    return t
'''
tab = carre_mag(5)
for lines in tab:
    print (lines)
''' 
def carrecroissant(n):
    t= createTab(n, n)
    k = 0
    for i in range (0,n):
        for j in range (0,n):
            k = k+1
            t[i][j] =k
    return t

tab = carrecroissant(5)
for lines in tab:
    print(lines)

def somPrev(n):
    s = n*(1+n**2)/2
    return s

def permutcol(t,c1,c2):
    '''Permut de permuter les colonnes C1 et C2 du tableau t en parcourant les 2 colonnes'''
    n = len(t)
    for i in range (n):
        temp = t[i][c1]
        t[i][c1] = t[i][c2]
        t[i][c2] = temp
    return temp


def permutlignes(t,l1,l2):
    '''Permut de permuter les lignes l1 et l2 du tableau t en parcourant les 2 colonnes'''
    p = len(t)
    for i in range (n):
        temp = t[i][l1]
        t[i][l1] = t[i][l2]
        t[i][l2] = temp
    return temp
