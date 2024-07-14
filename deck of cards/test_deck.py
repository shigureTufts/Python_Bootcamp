import unittest
from Deck import Deck


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_num_card(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_card(self):
        pass

    def test_deal_had(self):
        pass

    def test_shuffle(self):
        pass

    def test_count(self):
        pass


if __name__ == '__main__':
    unittest.main()
