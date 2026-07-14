class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        result = ""
        if (self.value == 1):
            result = "ace of " + self.suit
        elif (self.value == 11):
            result = "jack of " +self.suit
        elif (self.value == 12):
            result = "queen of " +self.suit
        elif (self.value == 13):
            result = "king of " +self.suit
        else:
            result = str(self.value) + " of " +self.suit
        return result
    def __repr__(self):
        return str(self)