import unittest
from Poker.poker_data import SetChecks
from CardsBase.card_data import Card


class TestChecks(unittest.TestCase):
    
    def test_sets(self):
        test_deck = [Card('10', 'Diamond'), Card('10', 'Heart'), Card('9', 'Diamond'), 
                     Card('9', 'Heart'), Card('8', 'Diamond'), Card('8', 'Heart'), Card('8', 'Spade')]
        expected = [[Card('10', 'Diamond'), Card('10', 'Heart')], [Card('9', 'Diamond'), 
                     Card('9', 'Heart')], [Card('8', 'Diamond'), Card('8', 'Heart'), Card('8', 'Spade')]]
        self.assertEqual(SetChecks.find_sets(test_deck), expected)

    def test_pair(self):
        test_deck = [Card('10', 'Diamond'), Card('10', 'Heart'), Card('9', 'Diamond'), 
                     Card('9', 'Heart'), Card('8', 'Diamond'), Card('8', 'Heart'), Card('8', 'Spade')]
        expected = [Card('10', 'Diamond'), Card('10', 'Heart')]
        self.assertEqual(SetChecks.check_pair(test_deck), expected)
    
    def test_twopair(self):
        test_deck = [Card('10', 'Diamond'), Card('10', 'Heart'), Card('9', 'Diamond'), 
                     Card('9', 'Heart'), Card('8', 'Diamond'), Card('8', 'Heart'), Card('8', 'Spade')]
        expected = [Card('10', 'Diamond'), Card('10', 'Heart'), Card('9', 'Diamond'), 
                     Card('9', 'Heart')]
        self.assertEqual(SetChecks.check_twopair(test_deck), expected)

    def test_three(self):
        test_deck = [Card('10', 'Diamond'), Card('10', 'Heart'), Card('9', 'Diamond'), 
                     Card('9', 'Heart'), Card('8', 'Diamond'), Card('8', 'Heart'), Card('8', 'Spade')]
        expected = [Card('8', 'Diamond'), Card('8', 'Heart'), Card('8', 'Spade')]
        self.assertEqual(SetChecks.check_three(test_deck), expected)

    def test_straight1(self):
        test_deck = [Card('2', 'Diamond'), Card('3', 'Heart'), Card('4', 'Diamond'), 
                     Card('5', 'Heart'), Card('6', 'Diamond'), Card('7', 'Heart'), Card('8', 'Spade')]
        expected = [Card('4', 'Diamond'), Card('5', 'Heart'), Card('6', 'Diamond'), Card('7', 'Heart'), Card('8', 'Spade')]
        self.assertEqual(SetChecks.check_straight(test_deck), expected)

    def test_straight2(self):
        test_deck = [Card('2', 'Diamond'), Card('3', 'Heart'), Card('4', 'Diamond'), 
                     Card('5', 'Heart'), Card('5', 'Diamond'), Card('7', 'Heart'), Card('8', 'Spade')]
        expected = []
        self.assertEqual(SetChecks.check_straight(test_deck), expected)

if __name__ == '__main__':
    unittest.main()
