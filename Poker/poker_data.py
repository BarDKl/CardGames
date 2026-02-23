from CardsBase.card_data import BaseDeck, Card
from collections import counter

class PokerDeck(BaseDeck):
    def build_deck(self):
        ranks = [f"{i}" for i in range(2,11)] + ["Jack", "Queen", "King", "Ace"]
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        return [Card(rank, suit) for rank in ranks for suit in suits]

class SetChecks:
    def check_highcard(cards: list[Card]):
        return max(cards)
    
    def find_sets(cards: list[Card]):
        counts = counter(Card.ranking_map[card.rank] for card in cards)
        pairs_ranks = [rank_val for rank_val, count in counts.items() if count == 2]
        if not pairs_ranks:
            return False
        else:
            return [[card for card in cards if card.rank == rank] for rank in pairs_ranks]

    def check_pair(self, cards: list[Card]):
        sets = self.find_sets(cards)
        max_pair: list[Card] = []
        for set in sets:
            if len(set) == 2:
                max_pair = max(set, max_pair)
        return max_pair
