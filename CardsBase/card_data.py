import abc
import random
from copy import copy
from dataclasses import dataclass
random.seed(1)


@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise ValueError("Cannot compare to non Card object")
        return self.ranking_map[self.rank] > self.ranking_map[self.rank]

    def rank_equals(self, other):
        if not isinstance(other, Card):
            raise ValueError("Cannot compare to non Card object")
        return self.rank == other.rank

    def suit_equals(self, other):
        if not isinstance(other, Card):
            raise ValueError("Cannot compare to non Card object")
        return self.suit == other.suit
class BaseDeck(abc.ABC):
    def __init__(self):
        self.cards: list[Card] = self.build_deck()
        self.free_cards: list[Card] = copy(self.cards)

    @abc.abstractmethod
    def build_deck(self):
        """Should build a deck specific to a given game"""
        pass

    def shuffle(self):
        random.shuffle(self.cards)
        self.free_cards = copy(self.cards)

    def __getitem__(self, position: int):
        return self.cards[position]

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"{self.cards}"

    def take_cards(self, n: int):
        hand = random.sample(self.free_cards, n)
        for card in hand:
            self.free_cards.remove(card)
        return hand
    
class BaseHand(abc.ABC):
    def __init__(self, deck: BaseDeck):
        self.cards = self.build_hand(deck)
    def __repr__(self):
        return f"{self.cards}"

    @abc.abstractmethod
    def build_hand(self, deck: BaseDeck):
        """Should buid a hand from a given deck"""
