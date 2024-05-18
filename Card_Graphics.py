import random

class Hand:
    def __init__(self):
        self.cards = [] #the cards in a hand, starting empty
    def deal_card(self, deck):  #ability of the hand class to be dealt a card
        card=deck.pop()
        self.cards.append(card)
    def card1(self): #This will return the rank of the first card in a hand(eg return 10)
        return (self.cards[0].split(' ')[0])
    def card2(self): #This will return the rank of the second card in a hand(eg return 10)
        return (self.cards[1].split(' ')[0])
    
#Makes the Deck
def make_deck():
    suits = ['\u2663', '\u2665', '\u2666', '\u2660']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for i in range(6): #Use 6 Decks
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} {suit}')
    random.shuffle(deck)
    random.shuffle(deck)
    return deck

def return_card(card,double):
   rank = card.split(' ')[0]
   suit = card.split(' ')[1]
   card_graphic = [\
      '╭─────────╮',\
      '│error    │',\
      '│    error│',\
      '│error    │',\
      '│    error│',\
      '│error    │',\
      '╰─────────╯']
   if not double:
      if rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
         if rank == '2':
            card_graphic = [\
            '╭─────────╮',\
            '│2   {}    │'.format(suit),\
            '│         │',\
            '│         │',\
            '│         │',\
            '│    {}   2│'.format(suit),\
            '╰─────────╯']
         elif rank == '3':
            card_graphic = [\
            '╭─────────╮',\
            '│3   {}    │'.format(suit),\
            '│         │',\
            '│    {}    │'.format(suit),\
            '│         │',\
            '│    {}   3│'.format(suit),\
            '╰─────────╯']
         elif rank == '4':
            card_graphic = [\
            '╭─────────╮',\
            '│4 {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│         │',\
            '│         │',\
            '│  {}   {} 4│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '5':
            card_graphic = [\
            '╭─────────╮',\
            '│5 {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│    {}    │'.format(suit),\
            '│         │',\
            '│  {}   {} 5│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '6':
            card_graphic = [\
            '╭─────────╮',\
            '│6 {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│  {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│  {}   {} 6│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '7':
            card_graphic = [\
            '╭─────────╮',\
            '│7 {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│  {}   {} 7│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '8':
            card_graphic = [\
            '╭─────────╮',\
            '│8 {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {} 8│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '9':
            card_graphic = [\
            '╭─────────╮',\
            '│9 {}   {}  │'.format(suit,suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│  {}   {} 9│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '10':
            card_graphic = [\
            '╭─────────╮',\
            '│10 {} {}   │'.format(suit,suit),\
            '│  {} {} {}  │'.format(suit,suit,suit),\
            '│         │',\
            '│  {} {} {}  │'.format(suit,suit,suit),\
            '│   {} {} 10│'.format(suit,suit),\
            '╰─────────╯']
      elif rank in ('J','Q','K'):
         card_graphic = [\
         '╭─────────╮',\
         '│{}┌─────┐ │'.format(rank),\
         '│{}│▓▓▒▒▓│ │'.format(suit),\
         '│ │░░░░░│ │',\
         '│ │▓▒▒▓▓│{}│'.format(suit),\
         '│ └─────┘{}│'.format(rank),\
         '╰─────────╯']
      elif rank == 'A':
         if card == 'A ♥':
            card_graphic = [\
            '╭─────────╮',\
            '│A  _ _   │',\
            '│♥ ( V )  │',\
            '│   \ /   │',\
            '│    V   ♥│',\
            '│        A│',\
            '╰─────────╯']
         elif card == 'A ♦':
            card_graphic = [\
            '╭─────────╮',\
            '│A   ^    │',\
            '│♦ /   \  │',\
            '│  \   /  │',\
            '│    v   ♦│',\
            '│        A│',\
            '╰─────────╯']
         elif card == 'A ♠':
            card_graphic = [\
            '╭─────────╮',\
            '│A   .    │',\
            '│♠  / \   │',\
            '│  (_._)  │',\
            '│    |   ♠│',\
            '│        A│',\
            '╰─────────╯']
         elif card == 'A ♣':
            card_graphic = [\
            '╭─────────╮',\
            '│A   _    │',\
            '│♣  ( )   │',\
            '│  (_\'_)  │',\
            '│    |   ♣│',\
            '│        A│',\
            '╰─────────╯']
      elif card == 'back side':
         card_graphic = [\
         '╭─────────╮',\
         '│⚜ ⚜ ⚜ ⚜  │',\
         '│ ⚜ ⚜ ⚜ ⚜ │',\
         '│⚜ ⚜ ⚜ ⚜  │',\
         '│ ⚜ ⚜ ⚜ ⚜ │',\
         '│⚜ ⚜ ⚜ ⚜  │',\
         '╰─────────╯']
      elif card == 'shoe card':
         card_graphic = [\
         '▗▄▄▄▄▄▄▄▄▄',\
         '▐█████████',\
         '▐█████████',\
         '▐█████████',\
         '▐█████████',\
         '▐█████████',\
         '▝▀▀▀▀▀▀▀▀▀']
      return card_graphic
   elif double:
      if rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10'):
         if rank == '2':
            card_graphic = [\
            '╭─────────╮',\
            '│2   {}    │'.format(suit),\
            '│         │',\
            '│         │',\
            '│         │',\
            '│    {}   2│'.format(suit),\
            '╰─────────╯']
         elif rank == '3':
            card_graphic = [\
            '╭─────────╮',\
            '│3   {}    │'.format(suit),\
            '│         │',\
            '│    {}    │'.format(suit),\
            '│         │',\
            '│    {}   3│'.format(suit),\
            '╰─────────╯']
         elif rank == '4':
            card_graphic = [\
            '╭─────────╮',\
            '│4 {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│         │',\
            '│         │',\
            '│  {}   {} 4│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '5':
            card_graphic = [\
            '╭─────────╮',\
            '│5 {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│    {}    │'.format(suit),\
            '│         │',\
            '│  {}   {} 5│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '6':
            card_graphic = [\
            '╭─────────╮',\
            '│6 {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│  {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│  {}   {} 6│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '7':
            card_graphic = [\
            '╭─────────╮',\
            '│7 {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│         │',\
            '│  {}   {} 7│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '8':
            card_graphic = [\
            '╭─────────╮',\
            '│8 {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {} 8│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '9':
            card_graphic = [\
            '╭─────────╮',\
            '│9 {}   {}  │'.format(suit,suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│    {}    │'.format(suit),\
            '│  {}   {}  │'.format(suit,suit),\
            '│  {}   {} 9│'.format(suit,suit),\
            '╰─────────╯']
         elif rank == '10':
            card_graphic = [\
            '╭─────────╮',\
            '│10 {} {}   │'.format(suit,suit),\
            '│  {} {} {}  │'.format(suit,suit,suit),\
            '│         │',\
            '│  {} {} {}  │'.format(suit,suit,suit),\
            '│   {} {} 10│'.format(suit,suit),\
            '╰─────────╯']
      elif rank in ('J','Q','K'):
         card_graphic = [\
         '╭─────────╮',\
         '│{}┌─────┐ │'.format(rank),\
         '│{}│▓▓▒▒▓│ │'.format(suit),\
         '│ │░░░░░│ │',\
         '│ │▓▒▒▓▓│{}│'.format(suit),\
         '│ └─────┘{}│'.format(rank),\
         '╰─────────╯']
      elif rank == 'A':
         if card == 'A ♥':
            card_graphic = [\
            '╭─────────╮',\
            '│A  _ _   │',\
            '│♥ ( V )  │',\
            '│   \ /   │',\
            '│    V   ♥│',\
            '│        A│',\
            '╰─────────╯']
         elif card == 'A ♦':
            card_graphic = [\
            '╭─────────╮',\
            '│A   ^    │',\
            '│♦ /   \  │',\
            '│  \   /  │',\
            '│    v   ♦│',\
            '│        A│',\
            '╰─────────╯']
         elif card == 'A ♠':
            card_graphic = [\
            '╭─────────╮',\
            '│A   .    │',\
            '│♠  / \   │',\
            '│  (_._)  │',\
            '│    |   ♠│',\
            '│        A│',\
            '╰─────────╯']
         elif card == 'A ♣':
            card_graphic = [\
            '╭─────────╮',\
            '│A   _    │',\
            '│♣  ( )   │',\
            '│  (_\'_)  │',\
            '│    |   ♣│',\
            '│        A│',\
            '╰─────────╯']
      elif card == 'back side':
         card_graphic = [\
         '╭─────────╮',\
         '│⚜ ⚜ ⚜ ⚜  │',\
         '│ ⚜ ⚜ ⚜ ⚜ │',\
         '│⚜ ⚜ ⚜ ⚜  │',\
         '│ ⚜ ⚜ ⚜ ⚜ │',\
         '│⚜ ⚜ ⚜ ⚜  │',\
         '╰─────────╯']


deck = make_deck()
example_hand = Hand()
example_hand.deal_card(deck)
example_hand.deal_card(deck)
example_hand.deal_card(deck)
example_hand.deal_card(deck)
card1 = example_hand.cards[0]
card2 = example_hand.cards[1]
card3 = example_hand.cards[2]
card4 = example_hand.cards[3]
graphic1 = return_card(card1,False)
graphic2 = return_card(card2,False)
graphic3 = return_card(card3,False)
graphic4 = return_card(card4,False)
for i in graphic1:
   print(i)
for z in graphic2:
   print(z)
for n in graphic3:
   print(n)
for x in graphic4:
   print(x)
#Queens work, Kings work, Aces work