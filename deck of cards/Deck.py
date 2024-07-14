from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(value, suit) for value in Deck.values for suit in Deck.suits]

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def _deal(self, number=1):
        dealt_cards = []
        while number > 0 and self.cards:
            dealt_cards.append(self.cards.pop())
            number -= 1

        if not dealt_cards:
            raise ValueError("All cards have been dealt")

        return dealt_cards if len(dealt_cards) > 1 else dealt_cards[0]

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)

    def deal_card(self):
        return self._deal()

    def deal_hand(self, number):
        return self._deal(number)

    def count(self):
        return len(self.cards)
