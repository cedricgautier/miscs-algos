plato = [[1,2,3], [4,5,6],[7,8,9]]

def tictactoe(plato):
    compt = 0 
    while compt < 9:
        player = compt % 2 + 1
        choose_case = int(input(f"Player {player}, choisissez le numéro d'une case libre : "))
        i = (choose_case - 1) // 3
        j = (choose_case - 1) % 3
        if player == 1:
            plato[i][j] = "X"
        else:
            plato[i][j] = "Y"
        for i in range(3):
            print(plato[i])
        compt +=1
    
    print(plato)

tictactoe(plato)