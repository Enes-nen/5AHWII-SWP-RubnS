import unittest
from poker import count_ranks, evaluate_hand


class TestPokerFunctions(unittest.TestCase):

    def test_count_ranks(self):
        hand = ["A♠", "A♥", "K♦", "10♣", "10♦"]
        result = count_ranks(hand)
        expected = {"A": 2, "K": 1, "10": 2}
        self.assertEqual(result, expected)

    def test_evaluate_hand_full_house(self):
        hand = ["A♠", "A♥", "A♦", "K♣", "K♦"]
        result = evaluate_hand(hand)
        self.assertEqual(result, "Full House")

    def test_evaluate_hand_flush(self):
        hand = ["2♣", "5♣", "9♣", "J♣", "K♣"]
        result = evaluate_hand(hand)
        self.assertEqual(result, "Flush")

    def test_evaluate_hand_straight(self):
        hand = ["6♠", "7♥", "8♦", "9♣", "10♠"]
        result = evaluate_hand(hand)
        self.assertEqual(result, "Straight")


if __name__ == "__main__":
    unittest.main()
