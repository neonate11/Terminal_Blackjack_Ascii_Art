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


print('This is an update line to test if I can commit to the repository')

print('This is a secondn update line to test if I can commit to the repository')

def return_card(card,double):
   rank,suit = card.split()

   card_graphics = {
      '2': {
         'not_double': [
            '╭─────────╮',
            f'│2   {suit}    │',
            '│         │',
            '│         │',
            '│         │',
            f'│    {suit}   2│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│           2 │',
           f'│ {suit}         {suit} │',
            '│ 2           │',
            '╰─────────────╯']},
      '3': {
         'not_double': [
            '╭─────────╮',
            f'│3   {suit}    │',
            '│         │',
            f'│    {suit}    │',
            '│         │',
            f'│    {suit}   3│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│           3 │',
            f'│ {suit}    {suit}    {suit} │',
            '│ 3           │',
            '╰─────────────╯']},
      '4': {
         'not_double': [
            '╭─────────╮',
            f'│4 {suit}   {suit}  │',
            '│         │',
            '│         │',
            '│         │',
            f'│  {suit}   {suit} 4│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│           3 │',
            f'│ {suit}    {suit}    {suit} │',
            '│ 3           │',
            '╰─────────────╯']},
      '5': {
         'not_double': [
            '╭─────────╮',
            f'│5 {suit}   {suit}  │',
            '│         │',
            f'│    {suit}    │',
            '│         │',
            f'│  {suit}   {suit} 5│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}     {suit} 5 │',
            f'│      {suit}      │',
            f'│ 5 {suit}     {suit}   │',
            '╰─────────────╯']},
      '6': {
         'not_double': [
            '╭─────────╮',
            f'│6 {suit}   {suit}  │',
            '│         │',
            f'│  {suit}   {suit}  │',
            '│         │',
            f'│  {suit}   {suit} 6│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}  {suit}  {suit} 6 │',
            '│             │',
            f'│ 6 {suit}  {suit}  {suit}   │',
            '╰─────────────╯']},
      '7': {
         'not_double': [
            '╭─────────╮',
            f'│7 {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit}  │',
            '│         │',
            f'│  {suit}   {suit} 7│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}  {suit}  {suit} 7 │',
            f'│       {suit}     │',
            f'│ 7 {suit}  {suit}  {suit}   │',
            '╰─────────────╯']},
      '8': {
         'not_double': [
            '╭─────────╮',
            f'│8 {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit} 8│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}  {suit}  {suit} 8 │',
            f'│    {suit}   {suit}    │',
            f'│ 8 {suit}  {suit}  {suit}   │',
            '╰─────────────╯']},
      '9': {
         'not_double': [
            '╭─────────╮',
            f'│9 {suit}   {suit}  │',
            f'│  {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit}  │',
            f'│  {suit}   {suit} 9│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit} {suit} {suit} {suit} 9 │',
            f'│      {suit}      │',
            f'│ 9 {suit} {suit} {suit} {suit}   │',
            '╰─────────────╯']},
      '10': {
         'not_double': [
            '╭─────────╮',
            f'│10 {suit} {suit}   │',
            f'│  {suit} {suit} {suit}  │',
            '│         │',
            f'│  {suit} {suit} {suit}  │',
            f'│   {suit} {suit} 10│',
            '╰─────────╯'],
         'double': [
             '╭─────────────╮',
            f'│   {suit} {suit} {suit} {suit} 10│',
            f'│     {suit} {suit}     │',
            f'│10 {suit} {suit} {suit} {suit}   │',
            '╰─────────────╯']},
      'face': {
         'not_double': [
            '╭─────────╮',
            f'│{rank} ▓▓▒▒▓▓ │',
            f'│{suit} ░░░░░░ │',
            '│ ▒░░░░░▒ │',
            f'│ ░░░░░░ {suit}│',
            f'│ ▓▓▒▒▓▓ {rank}│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│  ▓░░▒░░░▓ {suit}{rank}│',
            '│  ▒▒░░░░░▒▒  │',
            f'│{rank}{suit} ▓░░░▒░░▓  │',
            '╰─────────────╯']},
      'A ♥': {
         'not_double': [
            '╭─────────╮',
            '│A  _ _   │',
            '│♥ ( V )  │',
            '│   \ /   │',
            '│    V   ♥│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│      ⌢  ♥ A │',
            '│    ≺   ⧼    │',
            '│ A ♥  ⌣      │',
            '╰─────────────╯']},
      'A ♦': {
         'not_double': [
            '╭─────────╮',
            '│A   ^    │',
            '│♦ /   \  │',
            '│  \   /  │'
            '│    v   ♦│'
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│      ^  ♦ A │',
            '│   <     >   │',
            '│ A ♦  ⌵      │',
            '╰─────────────╯']},
      'A ♠': {
         'not_double': [
            '╭─────────╮',
            '│A   ߍ    │',
            '│♠  / \   │',
            '│  (_._)  │',
            '│    |   ♠│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│      ⌢  ♠ A │',
            '│    ─│   >   │',
            '│ A ♠  ⌣      │',
            '╰─────────────╯']},
      'A ♣': {
         'not_double': [
            '╭─────────╮',
            '│A   _    │',
            '│♣  ( )   │',
            '│  (_\'_)  │',
            '│    |   ♣│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│         ♣ A │',
            '│    ─8o      │',
            '│ A ♣         │',
            '╰─────────────╯']},
      'back side': {
         'not_double': [
            '╭─────────╮',
            '│⚜ ⚜ ⚜ ⚜  │',
            '│ ⚜ ⚜ ⚜ ⚜ │',
            '│⚜ ⚜ ⚜ ⚜  │',
            '│ ⚜ ⚜ ⚜ ⚜ │',
            '│⚜ ⚜ ⚜ ⚜  │',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│ ⚜ ⚜ ⚜ ⚜ ⚜ ⚜ │',
            '│  ⚜ ⚜ ⚜ ⚜ ⚜  │',
            '│ ⚜ ⚜ ⚜ ⚜ ⚜ ⚜ │',
            '╰─────────────╯']},
      'shoe card': {
         'not_double': [
            '▗▄▄▄▄▄▄▄▄▄',
            '▐█████████',
            '▐█████████',
            '▐█████████',
            '▐█████████',
            '▐█████████',
            '▝▀▀▀▀▀▀▀▀▀'],
         'double': ['this card is not needed']}}
   
   if rank in card_graphics: #number Cards
       if double:
           return card_graphics[rank]['double']
       else:
           return card_graphics[rank]['not_double']
   elif card in card_graphics: #Aces, Reverse, and Shoe Card
       if double:
           return card_graphics[card]['double']
       else:
           return card_graphics[card]['not_double']
   elif rank in ('J','Q','K'):
       if double:
           return card_graphics['face']['double']
       else:
           return card_graphics['face']['not_double']
   else: 
       if double:
           return [
      '╭─────────────╮',
      '│error        │',
      '│        error│',
      '│error        │',
      '╰─────────────╯']   
       else:
           return [
      '╭─────────╮',
      '│error    │',
      '│    error│',
      '│error    │',
      '│    error│',
      '│error    │',
      '╰─────────╯']
       
deck = make_deck()
example_hand = Hand()
example_hand.deal_card(deck)
example_hand.deal_card(deck)
example_hand.deal_card(deck)
example_hand.deal_card(deck)
example_hand.deal_card(deck)
example_hand.deal_card(deck)
card1 = example_hand.cards[0]
card2 = example_hand.cards[1]
card3 = example_hand.cards[2]
card4 = example_hand.cards[3]
card5 = example_hand.cards[4]
card6 = example_hand.cards[5]
graphic1 = return_card(card1,False)
graphic2 = return_card(card2,False)
graphic3 = return_card(card3,False)
graphic4 = return_card(card4,True)
graphic5 = return_card(card5,True)
graphic6 = return_card(card6,True)
for i in graphic1:
   print(i)
for z in graphic2:
   print(z)
for n in graphic3:
   print(n)
for x in graphic4:
   print(x)
for k in graphic5:
   print(k)
for j in graphic6:
   print(j)