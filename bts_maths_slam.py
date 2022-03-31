def somme_div():
    """
    The function `somme_div` takes an integer `n` as input and returns the sum of all the integers
    between 1 and `n` that divide `n` without a remainder
    :return: The sum of the divisors of n
    """
    n = int(input("Choisis un entier N : "))
    diviseurs = []
    for i in range(1,n+1):
        if n % i == 0:
            diviseurs.append(i)        
    
    som_diviseur = sum(diviseurs)
    return som_diviseur
    

def somme_div_op(n):
    """
    The function returns the sum of all the divisors of a given number
    
    :param n: The number you want to find the sum of its divisors
    :return: The sum of the divisors of n
    """
    diviseurs = []
    for i in range(1,n+1):
        if n % i == 0:
            diviseurs.append(i)        
    
    som_diviseur = sum(diviseurs)
    print(som_diviseur)
    return som_diviseur
    
    
def pseudo_aim():
    """
    Pseudo_aim() is a function that takes two integers as input and returns a boolean value
    :return: The boolean value of check.
    """
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
    """
    # Python
    def pseudo_aim_op(a, b):
        somme_a = somme_div_op(a)
        somme_b = somme_div_op(b)
        if somme_a ==somme_b:
            check = True
        else:
            check = False
            print(check)
            return check
    
    :param a: The first number in the range
    :param b: The number you want to check
    :return: a boolean value.
    """
    somme_a = somme_div_op(a)
    somme_b = somme_div_op(b)
    if somme_a ==somme_b:
        check = True
    else:
        check = False
        print(check)
        return check
    
    
def ranger_pseudo_aim():
    """
    The function pseudo_aim_op takes two arguments, k and k, and returns the value of the function
    pseudo_aim_op(k, k)
    """
    start = 0
    end = 100
    for k in range (start, end):
        this = pseudo_aim_op(k, k)