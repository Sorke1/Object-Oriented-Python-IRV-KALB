import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8

# Function to get a random card from the deck
def getCard(deckListIn):
    """Pop one card off the top of the deck and return."""
    return deckListIn.pop()

# Function to shuffle the deck
def shuffle(deckListIn):
    """Shuffle the deck and return a shuffled copy."""
    deckListOut = deckListIn.copy()  # Make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

# Initialize starting deck
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # Play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)

    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for _ in range(NCARDS):  # Play one game with this many cards
        answer = input('Will the next card be higher or lower than the ' +
                       currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ')
        answer = answer.casefold()  # Convert answer to lowercase

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if (answer == 'h' and nextCardValue > currentCardValue) or \
           (answer == 'l' and nextCardValue < currentCardValue):
            print('You got it right, it was', 'higher' if answer == 'h' else 'lower')
            score += 20
        else:
            print('Sorry, it was not', 'higher' if answer == 'h' else 'lower')
            score -= 15

        print('Your score is:', score)
        print()

        currentCardRank = nextCardRank
        currentCardSuit = nextCardSuit
        currentCardValue = nextCardValue

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')
