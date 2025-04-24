from random import randint

class GameDeck:
    def __init__(self, deck = []):
        spCard = {1: "a", 2: "j", 3: "q", 4: "k"}
        suit = {1: "clubs", 2: "spades", 3: "hearts", 4: "diamonds"}
        deck = [f"a {suit[i]}" for i in range(1, 5)]
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
        cc = 0
        cs = 0
        for i in range(1, len(self.deck)):
            for j in range(i):
                if self.deck[i].split(" ")[0] < self.deck[j].split(" ")[0]:
                    temp = self.deck[i]
                    self.deck[i] = self.deck[j]
                    self.deck[j] = temp
                    cs += 1
                    continue
                cc += 1
        print(f"checked: {cc}")
        print(f"swapped: {cs}")

    def shuffle(self):
        temp = ""
        for i in range(1000):
            ind1, ind2 = randint(0,51), randint(0,51)
            temp = self.deck[ind1]
            self.deck[ind1] = self.deck[ind2]
            self.deck[ind2] = temp

    def to_string(self):
        print(self.deck)

my_hand = GameDeck()
my_hand.count_suit("hearts")
my_hand.to_string()
my_hand.shuffle()
my_hand.to_string()
tem = my_hand.deal_cards(4)
print(tem)
my_hand.to_string()
my_hand.rejoin(tem)
my_hand.to_string()
my_hand.sort_deck()
my_hand.to_string()