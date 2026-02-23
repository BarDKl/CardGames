from CardsBase.card_data import Card, BaseHand
from poker_data import PokerDeck


class TH_Hand(BaseHand):
    def build_hand(self, deck: PokerDeck):
        return deck.take_cards(2)


class TH_Table():
    def __init__(self, deck: PokerDeck):
        self.cards: list[Card] = deck.take_cards(5)
        self.pointer: int = 0
    
    def __repr__(self):
        return f"{self.cards[:self.pointer]}"

    def show_cards(self, n:int):
        self.pointer += n
        return f"{self.cards[ : self.pointer]}"
    

class TH_game():
    def __init__(self, deck: PokerDeck , n_players: int):
        self.deck: PokerDeck = deck
        self.deck.shuffle()
        self.hands: list[TH_Hand] = [TH_Hand(deck) for _ in range(n_players)]
        self.table: TH_Table = TH_Table(deck)
    
    def play(self):
        self.deck.shuffle()
        for i in range(len(self.hands)):
            print(f"Hand{i+1}: {self.hands[i]}")
        print(f"Table: {self.table.show_cards(5)}")

    
