# coding=UTF-8

class Card:
    def __init__(self, rank, suit, hard, soft):
        self.suit = suit
        self.rank = rank
        self.hard = hard
        self.soft = soft

class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)

class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__('A', suit, 1, 11)

class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit, 10, 10)


