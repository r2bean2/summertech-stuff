from card import card
from random import randint
class deck:
    def __init__(self):
        self.deck = []
        for i in range(1,14):
            for j in range(0,4):
                if j==0:
                    self.deck.append(card("heart", i))
                elif j==1:
                    self.deck.append(card("spade", i))
                elif j==2:
                    self.deck.append(card("club", i))
                else:
                    self.deck.append(card("diamond", i))
    def shuffle(self):
        for i in range(len(self.deck)):
            x = randint(i, len(self.deck)-1)
            temp = self.deck[i]
            self.deck[i] = self.deck[x]
            self.deck[x] = temp

    def draw(self):
        return self.deck.pop()
    def __len__(self):
        return len(self.deck)
    def cheatLook(self, num_look = -1):
        if num_look == -1:
            return self.deck
        else:
            try:
                return self.deck[num_look]
            except:
                return self.deck
    def __str__(self):
        return str(self.deck)
    def __repr__(self):
        return str(self.deck)