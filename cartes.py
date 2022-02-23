import random, time

'''
- Create number of cards, has to be pair
- Shuffle number of cards
- Distribute the number of cards to be 
- Check who has the biggest card in the deck 
-
'''

from pickle import APPEND


def SizeCreator():
    numberOfCards  = int(input("Please choose the number of cards to have. Please pick a pair number\nWrite Here : "))
    cardNotifier = print(f"You have {numberOfCards} cards.")
    pair = numberOfCards % 2 
    while pair != 0:
        print(False, "You have an chosen an odd number")
        numberOfCards  = int(input("Please choose the number of cards to have. Please pick a pair number\nWrite Here : "))
        pair = numberOfCards % 2 
    return numberOfCards

def CreatePack(numberOfCards):
    deck = []
    for card in range (1, numberOfCards+1):
        deck.append(card)
    return deck

def randomizePack(deck):
    cards_listed = []
    while len(cards_listed) != len(deck):
        randomized_card = random.randint(1, len(deck))
        if randomized_card not in cards_listed:
            cards_listed.append(randomized_card)
    return cards_listed

def distributeCards(shuffleddeck):
    deck_playerone = []
    deck_playertwo = []
    print(shuffleddeck)
    for card in shuffleddeck:
        if shuffleddeck.index(card) % 2 == 0:
             deck_playerone.append(card)
        else:
             deck_playertwo.append(card)
    return (deck_playerone, deck_playertwo) 

def winnerchecker(deck_playerone, deck_playertwo):
    turns = len(deck_playertwo)
    print(f"Deck One :", deck_playerone,"Deck Two : ", deck_playertwo, "Number of turns :", turns)
    for turn in range (turns):
        if deck_playerone[turn] > deck_playertwo[turn]:
            deck_playerone.append(deck_playerone[turn])
            deck_playerone.append(deck_playertwo[turn])
            print("Turn "+ str(turn+1) + ", winner is Deck One\n")
        elif deck_playertwo[turn] > deck_playerone[turn]:
            deck_playertwo.append(deck_playerone[turn])
            deck_playertwo.append(deck_playertwo[turn])
            print("Turn " + str(turn+1) + ", winner is Deck Two\n")
        print(deck_playerone,deck_playertwo)
    
            
        

def main():
    start_time = time.time()
    size = SizeCreator()
    pack = CreatePack(size)
    shuffle = randomizePack(pack)
    deck_playerone, deck_playertwo = distributeCards(shuffle)
    winnerchecker(deck_playerone, deck_playertwo)
    print("\n--- %s seconds ---" % (time.time() - start_time))

main()