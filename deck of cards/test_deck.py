import unittest
from Deck import Deck, Card
from random import randint


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Heart", "A")

    def test_card(self):
        self.assertEqual(self.card.suit, "Heart")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        self.assertEqual(self.card.__repr__(), f"{self.card.value} of {self.card.suit}")

class DeckTests(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_repr(self):
        self.assertEqual(self.deck.__repr__(), f"Deck of {len(self.deck.cards)} cards")

    def test_num_card(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_card(self):
        before_deal = len(self.deck.cards)
        self.deck.deal_card()
        after_deal = len(self.deck.cards)
        self.assertEqual(before_deal-after_deal, 1)

    def test_deal_hand(self):
        before_deal = len(self.deck.cards)
        self.deck.deal_hand(14)
        after_deal = len(self.deck.cards)
        self.assertEqual(before_deal - after_deal, 14)

    def test_shuffle(self):
        num = randint(0, 51)
        card_before = self.deck.cards[num]
        self.deck.shuffle()
        card_after = self.deck.cards[num]
        self.assertNotEqual(card_after, card_before)

    def test_count(self):
        before_deal = len(self.deck.cards)
        self.deck.deal_hand(10)
        after_deal = len(self.deck.cards)
        self.assertEqual(before_deal - after_deal, 10)


if __name__ == '__main__':
    unittest.main()
