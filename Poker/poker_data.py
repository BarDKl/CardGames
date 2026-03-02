from CardsBase.card_data import BaseDeck, Card
from collections import Counter
from copy import copy


class PokerDeck(BaseDeck):
    def build_deck(self):
        ranks = [f"{i}" for i in range(2, 11)] + \
            ["Jack", "Queen", "King", "Ace"]
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        return [Card(rank, suit) for rank in ranks for suit in suits]


class SetChecks:

    @staticmethod
    def check_highcard(cards: list[Card]):
        return max(cards)

    @staticmethod
    def sort_ranks(cards: list[Card]):
        return sorted(cards, key=lambda c: int(c.rank), reverse=True)
    
    @staticmethod
    def find_sets(cards: list[Card]):
        counts = Counter(card.rank for card in cards)
        ranks_sorted = sorted([rank for rank, count in counts.items() if count > 1], key=lambda r: int(r), reverse=True)

        if not ranks_sorted:
            return []
        return [[card for card in cards if card.rank == rank] for rank in ranks_sorted]

    @staticmethod
    def check_pair(cards: list[Card]):
        sets = SetChecks.find_sets(cards)
        result = [set for set in sets if len(set) == 2]
        return result[0] if result else []

    @staticmethod
    def check_twopair(cards: list[Card]):
        sets = SetChecks.find_sets(cards)
        result = [set for set in sets if len(set) == 2]
        return result[0] + result[1] if len(result) > 1 else []

    @staticmethod
    def check_three(cards: list[Card]):
        sets = SetChecks.find_sets(cards)
        result = [set for set in sets if len(set) == 3]
        return result[0] if result else []
    
    @staticmethod
    def check_straight(cards: list[Card]):
        cards_sorted = sorted(cards, key=lambda c: int(c.rank), reverse=False)
        straight: list[Card] = []
        for card in cards_sorted:
            if not straight:
                straight.append(card)
            else:
                if int(card.rank) == int(straight[-1].rank) + 1:
                    straight.append(card)
                elif int(card.rank) != int(straight[-1].rank):
                    straight = [card]
        if len(straight) >= 5:
            return straight[-5:]
        else:
            return []
    
