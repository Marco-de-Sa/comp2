from random import randint

# todo add a class dedicated to handling the cards dealt to the player and by extension detecting what hands they have
# todo add a way to count how many times specific hands have been encountered

class GameDeck:
    def __init__(self):
        spCard = {1: "ace", 2: "jack", 3: "queen", 4: "king"}
        suit = {1: "clubs", 2: "spades", 3: "hearts", 4: "diamonds"}
        deck = [f"{spCard[1]} of {suit[i]}" for i in range(1, 5)]
        for i in range(2, 11):
            for j in range(1, 5):
                deck.append(f"{i} of {suit[j]}")
        for i in range(2, 5):
            for j in range(1, 5):
                deck.append(f"{spCard[i]} of {suit[j]}")
        self.deck = deck
        self.spCard = spCard
        self.suit = suit

    def count_suit(self, target):
        temp = 0
        for i in self.deck:
            if i.split(" ")[1] == target:
                temp += 1
        print(f"There are {temp} cards belonging to {target} remaining in the deck")

    def rejoin(self, hand):
        for i in range(len(hand)): # takes the iterates through the hand indexes
            self.deck.append(hand.pop()) # pops each hand value into the deck

    def deal_cards(self, card_count):
        # todo add a way to sort cards before handing them out
        temp = [] # creates a temporary list
        for i in range(int(card_count)): # converts car_count to an integer and then iterates throughout it
            temp.append(self.deck.pop()) # appends the specified amount(from card_count) to the temp list by popping them from the deck
        return temp # returns the temp list

    def sort_deck(self):
        # wip not ready for use(will work if used however just not in it's final state)
        # todo add a method to sort the cards by suit and not just number
        # todo allow add new methods of sorting from what we have learned so far and let the user choose between them
        tempDeck = []
        for i in range(len(self.deck)):
            if self.deck[i].split(' ')[0] == "ace":
                tempDeck.append(self.deck[i])

        for i in range(2, 11): # to sort card numbers
            for j in range(len(self.deck)):# to get iterate through the deck
                if self.deck[j].split(' ')[0] == str(i):
                    tempDeck.append(self.deck[j])

        for i in range(2, 5):
            for j in range(len(self.deck)):
                if self.deck[j].split(' ')[0] == self.spCard[i]:
                    tempDeck.append(self.deck[j])
        self.deck = tempDeck

    def shuffle(self):
        temp = ""
        for i in range(1000): # iterates the code 1000 times
            ind1, ind2 = randint(0,51), randint(0,51) # randomly generates two indexes that will be swapped later
            # below swaps the two random indexes of the deck variable
            temp = self.deck[ind1]
            self.deck[ind1] = self.deck[ind2]
            self.deck[ind2] = temp

    def to_string(self):
        return f"{self.deck}" # returns the deck as a string

my_hand = GameDeck() # makes a new object of the GameDeck class

my_hand.sort_deck()
print(my_hand.to_string())