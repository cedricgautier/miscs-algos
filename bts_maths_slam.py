def somme_div():
    n = int(input("Choisis un entier N : "))
    diviseurs = []
    for i in range(1,n+1):
        if n % i == 0:
            diviseurs.append(i)        
    
    som_diviseur = sum(diviseurs)
    return som_diviseur
    

def somme_div_op(n):
    diviseurs = []
    for i in range(1,n+1):
        if n % i == 0:
            diviseurs.append(i)        
    
    som_diviseur = sum(diviseurs)
    print(som_diviseur)
    return som_diviseur
    
    
def pseudo_aim():
    a = int(input("Choisis un entier A: "))
    b = int(input("Choisis un entier B: "))
    somme_a = somme_div_op(a)
    somme_b = somme_div_op(b)
    if somme_a ==somme_b:
        check = True
    else:
        check = False
        print(check)
        return check
    
    

def pseudo_aim_op(a, b):
    somme_a = somme_div_op(a)
    somme_b = somme_div_op(b)
    if somme_a ==somme_b:
        check = True
    else:
        check = False
        print(check)
        return check
    
    
def ranger_pseudo_aim():
    start = 0
    end = 100
    for k in range (start, end):
        this = pseudo_aim_op(k, k)