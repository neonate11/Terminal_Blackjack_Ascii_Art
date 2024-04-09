#Make the Deck
import random
suits = ['\u2663', '\u2665', '\u2666', '\u2660']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} {suit}')

#Make a Deal Cards Function
def deal_cards(deck, hand):

    card = deck.pop()
    hand.append(card)

#Make a Calculate Hand Value Function
def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10

    return value

#Setup Player Bank
player_bank = 250

#Make a betting Function
legal_bet = True
def make_bet():
    global bet
    bet = 0
    print(f'Available funds: {player_bank}$')
    bet = int(input('How much would you like to bet? '))
    while legal_bet:
        if bet < 50:
            bet = int(input('Bet below table minimum, how much would you like to bet? '))
            continue
        if bet > player_bank:
            bet = int(input('Bet larger than available funds, how much would you like to bet?'))
            continue
        if bet > 1000:
            bet = int(input('Bet above table maximum, how much would you like to bet? '))
            continue
        if bet >= 50 and bet <= 1000 and bet <= player_bank:
            break
    print('\n','\n','\n','\n','\n','\n','\n','\n')

#Introductory Message
print('\n','\n','\n','\n','\n','\n')
print('Welcome to Nate\'s blackjack table, Nate will hit on 16 and stand on 17, Aces are 11 or 1')
print('Winning bets are paid even money, Blackjack pays 3 to 2')
print('Table min is 50, max is is 1000$, to bankrupt Nate win 5000$')
print('\n','\n','\n','\n','\n','\n','\n')

#Setup Ability to Play Again
playing = True
while playing:
    #Deal the First Two Cards
    make_bet()
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []

    deal_cards(deck, player_hand)
    deal_cards(deck, player_hand)
    deal_cards(deck, dealer_hand)
    deal_cards(deck, dealer_hand)

    #Determine if player can hit or stand
    while True:
        if calculate_hand_value(player_hand) == 21 and calculate_hand_value(dealer_hand) == 21: #Did the player and dealer both get blackjack
            break

        if calculate_hand_value(player_hand) == 21:   #Did the player get blackjack
            break

        if calculate_hand_value(dealer_hand) == 21:   #Did the dealer get blackjack
            break

        if calculate_hand_value(player_hand) > 21:    #Did the player bust
            break
       
        playerdisplay = (', '.join(map(str, player_hand)))  
        print(f'  Your hand: {playerdisplay} = {calculate_hand_value(player_hand)}')
        print(f'Nate\'s hand: {dealer_hand[0]} (facedown)')

        print('')
        print('')
        print('')
        action = input('Do you want to hit or stand? ')

        if action.lower() == 'hit':                   #Does the player want to hit or stand
            deal_cards(deck, player_hand)
            print('\n','\n','\n','\n','\n','\n','\n','\n')
        else:
            print('\n','\n','\n','\n','\n','\n','\n','\n')
            break

    #Make the Dealer hit or Stand
    if calculate_hand_value(player_hand)<21: #The dealer should only hit if the player didn't already get blackjack or bust
        while calculate_hand_value(dealer_hand)<17:
            deal_cards(deck, dealer_hand)
            print('Nate hit')

    #Determine who won
    playerdisplay = (', '.join(map(str, player_hand)))
    dealerdisplay = (', '.join(map(str, dealer_hand)))
    print('')
    print(f'  Your hand: {playerdisplay} = {calculate_hand_value(player_hand)}')
    print(f'Nate\'s hand: {dealerdisplay} = {calculate_hand_value(dealer_hand)}')
    print('')

    if calculate_hand_value(player_hand) == 21 and calculate_hand_value(dealer_hand)==21:
        print('Push')
    elif calculate_hand_value(player_hand) > 21:
        print('You bust','\n')
        player_bank = player_bank - bet
    elif calculate_hand_value(dealer_hand) > 21:
        print('Nate busts, you win!','\n')
        player_bank = player_bank + bet
    elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        print('You win!','\n')
        player_bank = player_bank + bet
    elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
        print('Nate wins, you lose','\n')
        player_bank = player_bank - bet
    else:
        print('Push!','\n')
   
    if player_bank <50:
        print('You\'ve gambled all your money away and can no longer afford the table minimum bet, sorry.','\n')
        print('')
        break

    if player_bank >=5000:
        print('\n','You bankrupted Nate! Thanks for playing!','\n')
        break

    print(f'You have: {player_bank}$','\n')
    playagain = input('Play another hand? [yes or no] ')
    if playagain[0].lower()=='y':
        playing = True
        print('\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n')
    else:
        print('\n','Thanks for playing at Nate\'s blackjack table.','\n')
        print(f'You\'re walking away with: {player_bank}')
        print('')
        break