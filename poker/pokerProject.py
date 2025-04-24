from random import randint

class GameDeck:
    def __init__(self):
        spCard = {1: "ace", 2: "jack", 3: "queen", 4: "king"}
        suit = {1: "clubs", 2: "spades", 3: "hearts", 4: "diamonds"}
        deck = [f"{spCard[1]} {suit[i]}" for i in range(1, 5)]
        for i in range(2, 11):
            for j in range(1, 5):
                deck.append(f"{i} {suit[j]}")
        for i in range(2, 5):
            for j in range(1, 5):
                deck.append(f"{spCard[i]} {suit[j]}")
        self.deck = deck

    def count_suit(self, target):
        temp = 0
        for i in self.deck:
            if i.split(" ")[1] == target:
                temp += 1
        print(f"There are {temp} cards belonging to {target} remaining in the deck")

    def rejoin(self, hand):
        for i in range(len(hand)):
            self.deck.append(hand.pop())

    def deal_cards(self, card_count):
        temp = []
        for i in range(int(card_count)):
            temp.append(self.deck.pop())
        return temp

    def sort_deck(self):
        # wip do not use
        tempDeck = []
        for i in range(2, 11): # to sort card numbers
            count = 0
            for j in range(len(self.deck)-1):# to get iterate through the deck
                if self.deck[j].split(' ')[0] == str(i):
                    tempDeck.append(self.deck.pop(j))
                    count+=1
                    j-=1
                if count == 4:
                    count = 0
                    continue
        self.deck = tempDeck

    def shuffle(self):
        temp = ""
        for i in range(1000):
            ind1, ind2 = randint(0,51), randint(0,51)
            temp = self.deck[ind1]
            self.deck[ind1] = self.deck[ind2]
            self.deck[ind2] = temp

    def __str__(self):
        return f"{self.deck}"

my_hand = GameDeck()
my_hand.count_suit("hearts")
print(my_hand.__str__())
my_hand.shuffle()
print(my_hand.__str__())
tem = my_hand.deal_cards(4)
print(tem)
print(my_hand.__str__())
my_hand.rejoin(tem)
print(my_hand.__str__())
my_hand.sort_deck()
print(my_hand.__str__())