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
    """
    This function is used to create a list of cards that will be used in the game.
        It takes the number of cards that the user wants to play with.
        It then checks if the number of cards is an even number.
        If it is not an even number, it will ask the user to pick an even number.
        It will then return the number of cards that the user wants to play with.
    :return: The number of cards that the user wants to play with.
    """
    numberOfCards  = int(input("Please choose the number of cards to have. Please pick a pair number\nWrite Here : "))
    cardNotifier = print(f"You have {numberOfCards} cards.")
    pair = numberOfCards % 2 
    while pair != 0:
        print(False, "You have an chosen an odd number")
        numberOfCards  = int(input("Please choose the number of cards to have. Please pick a pair number\nWrite Here : "))
        pair = numberOfCards % 2 
    return numberOfCards

def CreatePack(numberOfCards):
    """
    Create a pack of cards
    
    :param numberOfCards: the number of cards in the deck
    :return: A list of integers from 1 to the number of cards.
    """
    deck = []
    for card in range (1, numberOfCards+1):
        deck.append(card)
    return deck

def randomizePack(deck):
    """
    This function takes a deck of cards and returns a list of the cards in a randomized order
    
    :param deck: the deck of cards you want to randomize
    :return: A list of integers.
    """
    cards_listed = []
    while len(cards_listed) != len(deck):
        randomized_card = random.randint(1, len(deck))
        if randomized_card not in cards_listed:
            cards_listed.append(randomized_card)
    return cards_listed

def distributeCards(shuffleddeck):
    """
    Given a shuffled deck of cards, distribute the cards into two decks, one for each player.
    
    :param shuffleddeck: the deck of cards to be distributed
    :return: A tuple of two lists.
    """
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
    """
    The function takes two decks as input and compares them card by card. 
    If the card in deck one is greater than the card in deck two, the function appends the card in deck
    one to the winner's deck. 
    If the card in deck two is greater than the card in deck one, the function appends the card in deck
    two to the winner's deck. 
    The function continues to compare the cards until all the cards in one of the decks are used up. 
    The function then returns the winner's deck
    
    :param deck_playerone: the deck of cards that Player One will be dealt
    :param deck_playertwo: the deck of cards that Player Two has
    """
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
    """
    This function creates a deck of cards, shuffles it, and distributes the cards to two players
    """
    start_time = time.time()
    size = SizeCreator()
    pack = CreatePack(size)
    shuffle = randomizePack(pack)
    deck_playerone, deck_playertwo = distributeCards(shuffle)
    winnerchecker(deck_playerone, deck_playertwo)
    print("\n--- %s seconds ---" % (time.time() - start_time))

main()