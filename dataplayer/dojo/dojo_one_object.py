# coding=UTF-8

import random

class X:
    pass

print(X.__class__)
print(X.__class__.__base__)

class Card:
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

Club, Diamond, Heart, Spade = Suit('Club','♠'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♣')
Cards = [AceCard('A', Spade), NumberCard('2',Spade), NumberCard('3',Spade)]


def card(rank, suit):
    if rank == 1: return AceCard('A',suit)
    elif 2 <= rank < 11: return NumberCard(str(rank),suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception('Rank out of range.')

deck = [card(rank,suit) for rank in range(1,14)
        for suit in (Club, Diamond, Heart, Spade)]


def card3(rank, suit):
    if rank == 1: return AceCard('A',suit)
    elif 2 <= rank < 11: return NumberCard(str(rank),suit)
    elif rank == 11: return FaceCard('J', suit)
    elif rank == 12: return FaceCard('Q', suit)
    elif rank == 13: return FaceCard('K', suit)
    else:
        raise Exception('Rank out of range.')


def card4(rank, suit):
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)


def card5(rank, suit):
    class_, rank_str = {1: (AceCard,'A'),
                        11: (FaceCard,'J'),
                        12: (FaceCard,'Q'),
                        13: (FaceCard,'K')}.get(rank,(NumberCard,str(rank)))
    return class_(rank_str, suit)


class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {1: (AceCard,'A'),
                                      11: (FaceCard,'J'),
                                      12: (FaceCard,'Q'),
                                      13: (FaceCard,'K')}.get(rank,(NumberCard,str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)

card8 = CardFactory()
deck8 = [card8.rank(r+1).suit(s) for r in range(13)
         for s in (Club, Diamond, Heart, Spade)]

class Deck:
    def __init__(self):
        self._cards = [card8.rank(r+1).suit(s) for r in range(13)
                       for s in (Club, Diamond, Heart, Spade)]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

class Deck2(list):
    def __init__(self):
        super().__init__(card8.rank(r+1).suit(s) for r in range(13)
                         for s in (Club, Diamond, Heart, Spade))
        random.shuffle(self)
