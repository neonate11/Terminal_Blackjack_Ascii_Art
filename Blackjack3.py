import os #For the ability to clear terminal on windows or linux
import random
import platform #For the ability to check the OS
import time
#############################################################################################################################################################################################
##################################### CUSTOM CLASS SETUP ####################################### CUSTOM CLASS SETUP##########################################################################
#############################################################################################################################################################################################
class Hand:
    def __init__(self):
        self.cards = [] #the cards in a hand, starting empty
        self.double = False
    def deal_card(self, deck):  #ability of the hand class to be dealt a card
        card=deck.pop()
        self.cards.append(card)
    def card1(self): #This will return the rank of the first card in a hand(eg return 10)
        return (self.cards[0].split(' ')[0])
    def card2(self): #This will return the rank of the second card in a hand(eg return 10)
        return (self.cards[1].split(' ')[0])
    def check_for_split_option(self):  #This returns true if you have the option to split
        split = 'no'
        if len(self.cards) == 2:  #Make sure the player only has two cards
            if  self.card1() == self.card2():  #See if the cards are the same
                split = 'same_card'
            elif self.card1() in ['K', 'Q', 'J','10'] and self.card2() in ['K', 'Q', 'J','10']: #see if both cards are 10 value cards
                split = 'different_cards'
        return split
    def calculate_value(self):  #ability of the hand class to calculate it's value
        value = 0
        num_aces = 0
        for i in self.cards:
            rank = i.split(' ')[0]
            if rank == 'A':
                num_aces += 1
                value += 11
            elif rank in ['K', 'Q', 'J']:
                value += 10
            else:
                value += int(rank)
        # Adjust for Aces
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    def num_aces(self): #return the number of aces in a hand
        number_aces = 0
        for i in self.cards:
            rank = i.split(' ')[0]
            if rank == 'A':
                number_aces += 1
        return number_aces
    def doubleddown(self): #Remember if you doubled down
        self.double = True
    def if_doubledown(self): #Return whether you doubled down
        return self.double
#############################################################################################################################################################################################
##################################### GAMEPLAY AND USER INPUT FUNCTIONS ####################################### GAMEPLAY AND USER INPUT FUNCTIONS############################################
#############################################################################################################################################################################################
#Function to clear terminal
def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
clear_terminal() #Try and Get Screen blank asap

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
            
#Function for accepting a bet from the player
def make_bet():
    bet = 0
    i = num_hands
    clear_terminal()
    error_spacing = ''
    error_message = ''
    while True:
        draw_dealer_hand(0,1) #draw the player bank
        text_box(f'You are playing {i} hands.',"How much would you like to bet per hand?",' ','(You will be unable to split or double down','if you don\'t have money leftover)',error_spacing,error_message)
        bet = input(f'{left_space}                            $')   #the set amount of spaces is to account for half of the text box width
        if not bet.isdigit():
            error_spacing = ' '
            error_message = 'Bet must be a positive, whole number'
            clear_terminal()
        elif int(bet) > player_bank:
            error_spacing = ' '
            error_message = 'Bet exceeds available funds'
            clear_terminal()
        elif int(bet) > 1000:
            error_spacing = ' '
            error_message = 'Bet above table maximum ($1000)'
            clear_terminal()
        elif (int(bet)*i) > player_bank:
            error_spacing = ' '
            error_message = 'Amount bet across all hands exceeds available funds'
            clear_terminal()
        elif int(bet) < 10:
            error_spacing = ' '
            error_message = 'Bet below table minimum ($10)'
            clear_terminal()
        else:
            return int(bet)

#Function for determining number of starting hands:
def starting_hands():
    if player_bank >= 20: #Player can't play two hands if they don't have at least $20
        error_spacing = ''
        error_message = ''
        error_message2 = ''
        while True:
            draw_dealer_hand(0,1)
            text_box('How many hands would you like to play this round?','The table maximum is starting five hands.',error_spacing,error_message,error_message2)
            number_hands = input(input_pointer_with_spacing)
            if not number_hands.isdigit() or (int(number_hands) < 1) or (int(number_hands) > 5):
                error_spacing = ' '
                error_message = 'Please provide an integer from 1 to 5.'
                error_message2 = ''
                clear_terminal()
            elif int(number_hands) * 10 > player_bank:
                error_spacing = ' '
                error_message = 'You can\'t afford to play that many hands'
                error_message2 = 'The table minimum bet is $10'
                clear_terminal()
            else:
                break
        return(int(number_hands))

 #this function will adjust the player bank if they won money
def payout_player(player_bank): 
    for i, hand in enumerate(all_player_hands):
        payout = 2 * bet_per_hand
        if hand.if_doubledown():
            payout = 4*bet_per_hand
        if hand.calculate_value() > 21:                             #Player Busted                                            
            pass
        elif len(hand.cards) == 5:                                  #The Player got 5 cards without busting:    
            player_bank += payout
        elif hand.calculate_value() == nate_hand.calculate_value(): #The Player and Dealer Pushed
            player_bank += .5 * payout
        elif nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2: #Dealer Blackjack
            pass
        elif hand.calculate_value() == 21 and len(hand.cards) == 2:  #Player Blackjack
            player_bank += ((1.5 * bet_per_hand) + bet_per_hand)
        elif nate_hand.calculate_value() > 21:                       #Dealer Busted
            player_bank += payout
        elif hand.calculate_value() > nate_hand.calculate_value():   #The Players total was higher:
            player_bank += payout
        elif hand.calculate_value() < nate_hand.calculate_value():   #The Dealer Total was higher:
            pass
    return player_bank

#Function for asking the user a yes or no question
def yes_no_question(*args):   #the last input to yes_no has to be a 0 for no error or 1 for error
    error_spacing = ''
    error_message = ''
    if args[-1] == 1:
        error_spacing = ' '
        error_message = 'Please respond with y or n.'
    text_box(*args[:-1],error_spacing,error_message) 
    print('\n')
    #print(len(nate_hand.cards),nate_hand.calculate_value())    #DEBUGGING DEBUGGING DEBUGGING DEBUGGING DEBUGGING
    answer = input(input_pointer_with_spacing)
    if answer.isalpha() and (answer.lower() == 'y' or answer.lower() == 'n' or answer == 'DEBUG'):
        return answer.lower()
    else:
        return 'bad_input'

#Function for asking the user when they would like to be asked to double down
def ask_when_to_double():
    error_spacing = ''
    error_message = ''
    while True:
        draw_dealer_hand(0,1)
        text_box('When would you like to be asked to double down?',' ','A: for every hand','B: your count is hard 9-11','C: your count is hard 9-11 or soft 16-18','D: never',error_spacing,error_message)
        when_double = input(input_pointer_with_spacing)
        if when_double.isalpha() and when_double.lower() in ['a','b','c','d']:
            return(when_double.lower())
        else:
            error_spacing = ' '
            error_message = 'Please respond with A, B, C, or D'
            clear_terminal()

#Function for asking the user if they want to double down on a specific hand
def double_hand(i,player_bank):
    draw_entire_game(1,i,0)
    decision = yes_no_question(f"Would you like to double down on your{ordinals[i]} hand?",0)
    while decision =='bad_input':
        draw_entire_game(1,i,0)
        decision = yes_no_question(f"Would you like to double down on your{ordinals[i]} hand?",1)
    if decision == 'y':
        player_bank -= bet_per_hand
        hand.doubleddown()
        hand.deal_card(deck)
    return player_bank
#############################################################################################################################################################################################
##################################### GRAPHICS FUNCTIONS ####################################### GRAPHICS FUNCTIONS##########################################################################
#############################################################################################################################################################################################
#Function to draw the top of the board (either just player bank or player bank and the dealer's hands)
def draw_dealer_hand(hide,just_bank): 
    clear_terminal()
    lines= []
    length_money = len(str(player_bank))
    odd = length_money % 2
    lines.append('┌───────────┐' + (dealer_spacing-13)*' ')
    lines.append('│Your Chips:│' + (dealer_spacing-13)*' ')
    if odd: 
        half_space = int((9-length_money)/2) * ' '
        Bank_three_string = f'│{half_space}${player_bank} {half_space}│'
        lines.append(Bank_three_string + ((dealer_spacing-13)*' '))
    else:
        half_space = int((10-length_money)/2) * ' '
        Bank_three_string= f'│{half_space}${player_bank}{half_space}│'
        lines.append(Bank_three_string + ((dealer_spacing-13)*' '))
    lines.append('└───────────┘' + (dealer_spacing-13)*' ')
    if just_bank: #if just drawing the bank
        for i in lines:
            print(i)
        print('\n'*24)
    else:   #if drawing the bank and the dealer's cards
        for i in range(4,7):
            lines.append(dealer_spacing*' ') #Add spaces before the 6th and 7th lines of the cards that don't have the bank to their left
        num_cards_to_print = len(nate_hand.cards)
        if hide: 
            num_cards_to_print = 1
        for card in nate_hand.cards[:num_cards_to_print]:  # Iterate over the cards to print
            rank = card[0]
            rank2 = card[1]
            suit = card[-1]
            if rank2.isdigit(): #If the card is a 10, need to print the second integer (0) and delete the extra space
                left_data = rank + rank2 + suit
                right_data = rank + rank2 + suit
            else:
                left_data = rank + suit + ' '
                right_data = ' ' + rank + suit
            lines[0] += '┌─────────┐'
            lines[1] += '│{}      │'.format(left_data)
            lines[2] += '│         │'
            lines[3] += '│    {}    │'.format(suit)
            lines[4] += '│         │'
            lines[5] += '│      {}│'.format(right_data)
            lines[6] += '└─────────┘'
        if hide and len(nate_hand.cards)>1: #Don't print a hidden card before one is dealt
            lines[0] += '┌─────────┐'
            lines[1] += '│ ▓▓▓▓▓▓▓ │'
            lines[2] += '│ ▓▓▓▓▓▓▓ │'
            lines[3] += '│ ▓▓▓▓▓▓▓ │'
            lines[4] += '│ ▓▓▓▓▓▓▓ │'
            lines[5] += '│ ▓▓▓▓▓▓▓ │'
            lines[6] += '└─────────┘'
        for i in lines:
            print(i)

#Function to draw all player hands
def draw_all_player_hands(location):
    lines = []
    linestoprint = []
    for i in range(15):
        lines.append('')
        linestoprint.append('')
    spacing = int((screen_width-(len(all_player_hands)*23))/(len(all_player_hands)+1))
    for z, hand in enumerate(reversed(all_player_hands)):
        left_edge_data = [] #For left edge data, space is on right
        right_edge_data = [] #For right edge data, space is on left
        covered_data = [] #if a 10 is underneath another card, don't print the suit
        suits = [] #just for printing the middle part of card
        for card in hand.cards:
            rank=card[0]
            rank2 = card[1]
            suit=card[-1]
            suits.append(suit)
            if rank2.isdigit(): #If the hidden card is a 10, need the 10 to not print its suit
                left_edge_data.append(rank+rank2+suit)
                right_edge_data.append(rank+rank2+suit)
                covered_data.append(rank+rank2)
            else: #If the card is not a 10, need an extra space for the top cards, and for the hidden non 10 card to print its suit
                left_edge_data.append(rank+suit+' ')
                right_edge_data.append(' '+rank+suit)
                covered_data.append(rank+suit)    
        lines[0]='                       '
        lines[1]='                       '
        lines[2]='                       '
        lines[3]='                       '
        lines[4]='                       '
        lines[5]='                       '
        lines[6]='                       '
        lines[7]='                       '
        lines[8]='                       '
        lines[9]='                       '
        lines[10]='                       '
        lines[11]='                       '
        lines[12]='                       '
        lines[13]='                       '
        lines[14]='                       '
        if len(hand.cards) >= 1:
            lines[8]='┌─────────┐            '
            lines[9]='│{}      │            '.format(left_edge_data[0])
            lines[10]='│         │            '
            lines[11]='│    {}    │            '.format(suits[0])
            lines[12]='│         │            '
            lines[13]='│      {}│            '.format(right_edge_data[0])
            lines[14]='└─────────┘            '
        if len(hand.cards) >= 2:
            lines[6]  = '   ┌─────────┐         '
            lines[7]  = '   │{}      │         '.format(left_edge_data[1])
            lines[8]  = '┌──│         │         '
            lines[9]  = '│{}│    {}    │         '.format(covered_data[0],suits[1])
            lines[10] = '│  │         │         '
            lines[11] = '│  │      {}│         '.format(right_edge_data[1])
            lines[12] = '│  └─────────┘         '
        if hand.if_doubledown():
            lines[4]  = '       ┌─────────────┐ '
            lines[5]  = '       │          {}│ '.format(right_edge_data[2])
            lines[6]  = '   ┌───│      {}      │ '.format(suits[2])
            lines[7]  = '   │{} │{}          │ '.format(covered_data[1],left_edge_data[2])
            lines[8]  = '┌──│   └─────────────┘ '
        elif not hand.if_doubledown():
            if len(hand.cards) >= 3:
                lines[4]  = '      ┌─────────┐      '
                lines[5]  = '      │{}      │      '.format(left_edge_data[2])
                lines[6]  = '   ┌──│         │      '
                lines[7]  = '   │{}│    {}    │      '.format(covered_data[1],suits[2])
                lines[8]  = '┌──│  │         │      '
                lines[9]  = '│{}│  │      {}│      '.format(covered_data[0],right_edge_data[2])
                lines[10] = '│  │  └─────────┘      '
            if len(hand.cards) >= 4:
                lines[2]  = '         ┌─────────┐   '
                lines[3]  = '         │{}      │   '.format(left_edge_data[3])
                lines[4]  = '      ┌──│         │   '
                lines[5]  = '      │{}│    {}    │   '.format(covered_data[2],suits[3])
                lines[6] = '   ┌──│  │         │   '
                lines[7] = '   │{}│  │      {}│   '.format(covered_data[1],right_edge_data[3])
                lines[8] = '┌──│  │  └─────────┘   '
            if len(hand.cards) >= 5:
                lines[0]  = '            ┌─────────┐'
                lines[1]  = '            │{}      │'.format(left_edge_data[4])
                lines[2]  = '         ┌──│         │'
                lines[3]  = '         │{}│    {}    │'.format(covered_data[3],suits[4])
                lines[4] = '      ┌──│  │         │'
                lines[5] = '      │{}│  │      {}│'.format(covered_data[2],right_edge_data[4])
                lines[6] = '   ┌──│  │  └─────────┘'
        for i in range(0,10): #Add the spacing for these lines
            linestoprint[i]+= ' '*spacing
        for i in range(13,15): #Add the spacing for these lines
            linestoprint[i]+= ' '*spacing
        if location == (len(all_player_hands) -1)-z:      #if we are referring to this hand currently add the cursor (this part also adds the spacing between hands -2 to account for the cursor)
            linestoprint[10]+= ' '*(spacing-2)+'➤ ' #Add the cursor
            linestoprint[11]+= ' '*(spacing-2)+'➤ ' #Add the cursor
            linestoprint[12]+= ' '*(spacing-2)+'➤ ' #Add the cursor
            if Debug:
                linestoprint.append(f'The z value is set to {z} and the current location receved was {location}')
        else:                  #if we aren't referring to this hand currently put just spaces
            linestoprint[10]+= ' '*spacing 
            linestoprint[11]+= ' '*spacing 
            linestoprint[12]+= ' '*spacing 
        for n in range(15):
            linestoprint[n]+=lines[n]
    for i in linestoprint:
        print(i)

#Function to draw bets under their associated hand, this will also print the result of hand within the bet circle
def draw_bets(endgame):
    lines = []
    spacing = int((screen_width-(len(all_player_hands)*23))/(len(all_player_hands)+1)) #This determines appropriate spacing between the bet graphics
    for i in range(6):
        lines.append('')
    for i, hand in enumerate(reversed(all_player_hands)):
        for n in range(6):
            lines[n]+= ' '*spacing
        bet = bet_per_hand
        if hand.if_doubledown():
            bet = bet_per_hand*2
        push_return_amt = bet  #In case player pushes a blackjack you want to return the original bet placed, not how much blackjack would have paid
        if hand.calculate_value() == 21 and len(hand.cards) == 2: 
            bet = bet * 1.5
        bet_spacing = ''
        push_spacing = bet_spacing +(4-len(str(push_return_amt)))* ' '
        bet_spacing += (4-len(str(bet)))* ' '
        value = hand.calculate_value()
        value_spacing = ''
        value_spacing += (3 - len(str(value)))* ' '
        lines[0] += '    =  =               '                 
        lines[5] += '    =  =               '                               
        #these first two scenarios always win or lose so we can print no matter what stage of the game we are in
        if hand.calculate_value() > 21:                                                    #Player Busted 
                lines[1] += ' =        =            '   
                lines[2] += '=  BUSTED  =           '
                lines[3] += '=  -${}{}  =           '.format(bet,bet_spacing)    
                lines[4] += ' =        =            '         
        elif len(hand.cards) == 5:                                                     #The Player got 5 cards without busting: 
                lines[1] += ' =        =            '   
                lines[2] += '=5 no bust =           '
                lines[3] += '=  +${}{}  =           '.format(bet,bet_spacing)     
                lines[4] += ' =        =            '  
        #the dealer's hand has already been revealed, you can now show the results of every hand
        elif endgame:
            if hand.calculate_value() == nate_hand.calculate_value():                 #The Player and Dealer Pushed
                lines[1] += ' =        =            '   
                lines[2] += '=   PUSH   =           '
                lines[3] += '=   ${}{}  =           '.format(push_return_amt,push_spacing)  
                lines[4] += ' =        =            '    
            elif nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2:       #Dealer Blackjack
                lines[1] += ' =        =            ' 
                lines[2] += '=   Lost:  =           '.format(value,value_spacing)
                lines[3] += '=  -${}{}  =           '.format(bet,bet_spacing)
                lines[4] += ' =        =            ' 
            elif hand.calculate_value() == 21 and len(hand.cards) == 2:                 #Player Blackjack
                lines[1] += ' =        =            '   
                lines[2] += '=BLACKJACK!=           '
                lines[3] += '=  +${}{}  =           '.format(bet,bet_spacing)  
                lines[4] += ' =        =            ' 
            elif nate_hand.calculate_value() > 21:                                      #Dealer Busted
                lines[1] += ' =        =            ' 
                lines[2] += '=  Payout: =           '
                lines[3] += '=  +${}{}  =           '.format(bet,bet_spacing)
                lines[4] += ' =        =            '   
            elif hand.calculate_value() > nate_hand.calculate_value():                  #The Players total was higher:
                lines[1] += ' =        =            ' 
                lines[2] += '=  Payout: =           '
                lines[3] += '=  +${}{}  =           '.format(bet,bet_spacing)
                lines[4] += ' =        =            '  
            elif hand.calculate_value() < nate_hand.calculate_value():                  #The Dealer Total was higher:
                lines[1] += ' =        =            ' 
                lines[2] += '=   Lost:  =           '.format(value,value_spacing)
                lines[3] += '=  -${}{}  =           '.format(bet,bet_spacing)
                lines[4] += ' =        =            '   
        #The dealer's cards have not been shown yet    
        else:
            if hand.calculate_value()==21 and len(hand.cards) == 2:                    #The player has blackjack, we don't know if the dealer got blackjack as well
                lines[1] += ' =        =            '   
                lines[2] += '=BLACKJACK!=           '
                lines[3] += '=          =           '
                lines[4] += ' =        =            '  
            elif hand.calculate_value()==21:                                              #The Player has a count of 21 and should not hit anymore
                lines[1] += ' =        =            ' 
                lines[2] += '= Count:{}{}=           '.format(value,value_spacing)
                lines[3] += '=          =           '
                lines[4] += ' =        =            ' 
            else:                                                                      #It is unknow if the player has won or lost at this point
                lines[1] += ' =        =            '   
                lines[2] += '=   Bet:   =           '
                lines[3] += '=   ${}{}  =           '.format(bet,bet_spacing)     
                lines[4] += ' =        =            '    
    for n in lines:
        print(n)     

#Function for printing information to the user in a formatted box
def text_box(*args):
    print(f'{left_space}┌────────────────────────────────────────────────────┐')
    print(f'{left_space}│                                                    │')
    for arg in args:
        raw_spacing = 52-len(arg) #total box is 54 chars wide, minus edges is 52 spaces available to print on per line
        odd = raw_spacing % 2
        if arg!= '' and odd == False: #I added the functionality where the programmer can input a '' as a placeholder for a potential error message that won't be printed
            half_spacing = int(raw_spacing/2)* ' '
            print(f'{left_space}│{half_spacing}{arg}{half_spacing}│')
        elif arg!= '' and odd == True:
            half_spacing = int((raw_spacing-1)/2)* ' '
            print(f'{left_space}│ {half_spacing}{arg}{half_spacing}│')
    print(f'{left_space}│                                                    │')
    print(f'{left_space}└────────────────────────────────────────────────────┘')

#Function to call all graphics functions
def draw_entire_game(hide,location,endgame):   #leave the all_player_hands and bet_per_hand when you paste just put an integer for hide (1 means hide?) and for location put 'n' for no cursor, and for endgame put a 1 for its the end, a 0 otherwise
    draw_dealer_hand(hide,0)                                      #if you just want to draw the bank you can do draw_dealer_hand(1,1)
    draw_all_player_hands(location)
    draw_bets(endgame) #put a 1 for endgame if the results of the hand should be shown
    print('')
    if Debug:
        print(f'Nate has {len(nate_hand.cards)} cards, the value of his cards is {nate_hand.calculate_value()}')
        for i, hand in enumerate(all_player_hands):
            print(f'Your {i+1} hand has {len(hand.cards)} cards and has a total value of {hand.calculate_value()}')
#############################################################################################################################################################################################
##################################### STARTUP ACTIONS ####################################### STARTUP ACTIONS ###############################################################################
#############################################################################################################################################################################################
#General Variable Setup
player_bank = 100 #Player Starting Cash
ordinals = [' first',' second',' third',' fourth',' fifth',' sixth',' seventh',' eighth',' ninth',' tenth']
highscore_run = False #For remembering if the player has already beat the dealer
most_money = 100 #For printing the player's highscore when they lose or quit
screen_width = os.get_terminal_size()[0] 
screen_height = os.get_terminal_size()[1]

#Print Boot Screen
print('\n'*int((screen_height-11)/2))
bj_space = int((screen_width-102)/2)* ' '
print(bj_space,'▀█████████▄   ▄█          ▄████████  ▄████████    ▄█   ▄█▄      ▄█    ▄████████  ▄████████    ▄█   ▄█▄')
print(bj_space,'  ███    ███ ███         ███    ███ ███    ███   ███ ▄███▀     ███   ███    ███ ███    ███   ███ ▄███▀')
print(bj_space,'  ███    ███ ███         ███    ███ ███    █▀    ███▐██▀       ███   ███    ███ ███    █▀    ███▐██▀  ')
print(bj_space,' ▄███▄▄▄██▀  ███         ███    ███ ███         ▄█████▀        ███   ███    ███ ███         ▄█████▀   ')
print(bj_space,'▀▀███▀▀▀██▄  ███       ▀███████████ ███        ▀▀█████▄        ███ ▀███████████ ███        ▀▀█████▄   ')
print(bj_space,'  ███    ██▄ ███         ███    ███ ███    █▄    ███▐██▄       ███   ███    ███ ███    █▄    ███▐██▄  ')
print(bj_space,'  ███    ███ ███▌    ▄   ███    ███ ███    ███   ███ ▀███▄     ███   ███    ███ ███    ███   ███ ▀███▄')
print(bj_space,'▄█████████▀  █████▄▄██   ███    █▀  ████████▀    ███   ▀█▀ █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀')
print(bj_space,'             ▀                                   ▀         ▀▀▀▀▀▀                            ▀        ')
time.sleep(2)
clear_terminal()

#Calculate the Spacing and Recalculate some of the same values, in case the player made the screen larger after the initial message was diaplayed
screen_width = os.get_terminal_size()[0] 
screen_height = os.get_terminal_size()[1]
left_space = int((screen_width/2)-28)* ' ' #half of 56 is 28, this is just used for the text boxes I think
dealer_spacing = int((screen_width -36)/2) #used to the left of the dealers hand
top_space = '\n'*27
input_pointer_with_spacing = ((int((screen_width/2)-1)* ' ')+'>')

#Print Introductory Message, Give option to read rules
Debug = False
draw_dealer_hand(1,1)
decision = yes_no_question('Welcome to Nate\'s blackjack table','Your friend Ralph has lent you $100 in chips','Win $2000 to bankrupt Nate','Would you like to read the rules?',0)
while decision == 'bad_input':
    draw_dealer_hand(1,1)
    decision = yes_no_question('Welcome to Nate\'s blackjack table','Your friend Ralph has lent you $100 in chips','Win $2000 to bankrupt Nate','Would you like to read the rules?',1)
if decision == 'debug':
    Debug = True
elif decision == 'y':
    clear_terminal()
    while True:
        print('How to play Blackjack')
        print('     You will be dealt 2 cards, and have to decide if you want to be dealt more cards')
        print('     Get your card total as close to 21 without going over')
        print('     If your total is below 21, but higher than the dealer, you win')
        print('     Aces can count as 11s or 1s, whichever will help you more')
        print('     Totaling 21 with only two cards is called Blackjack')
        print('')
        print('Casino Rules:')
        print('     Nate will hit on 16 and stand on 17')
        print('     You can split your hand into two hands if you have two cards of the same value')
        print('     Before hitting, you can double down on any hand')
        print('     If you double down, your bet is doubled and you will be dealt exactly one more card')
        print('     This table uses 6 decks')
        print('')
        print('Betting:')
        print('     A hand created by splitting will inherit the original hand bet')
        print('     If you double down, the bet associated with that hand is doubled')
        print('     You will not be allowed to split or double down if you can\'t afford to')
        print('     The table minimum bet is $10, the maximum is $500')
        print('     Winning bets are paid even money')
        print('     Blackjack pays 3 to 2')
        print('')
        input("[press enter to continue]")
        break

if Debug:
    when_double = 'c'
else:
    when_double = ask_when_to_double()
#############################################################################################################################################################################################
##################################### GAMEPLAY LOOP ####################################### GAMEPLAY LOOP ###################################################################################
#############################################################################################################################################################################################
playing = True
while playing:
    clear_terminal()
    deck = make_deck()  
    previous_bank = player_bank
    all_player_hands = []

    #Give PLayer Option of How Many Hands to Start with
    if Debug:
        num_hands = 8
    else:
        num_hands = starting_hands()
                  
    #Find out how much the player wants to bet
    if Debug:
        bet_per_hand = 10
    else:
        bet_per_hand = make_bet() 
    for i in range(num_hands):
        player_bank -= bet_per_hand

    #Dealing Animation Section###########################################
    if Debug:
        nate_hand = Hand()
        nate_hand.deal_card(deck)
        nate_hand.deal_card(deck)
        for i in range(num_hands):
            all_player_hands.append(Hand())
            all_player_hands[i].deal_card(deck)
            all_player_hands[i].deal_card(deck)

    else:
        hand_counter = num_hands
        nate_hand = Hand()
        for i in range(hand_counter):
            all_player_hands.append(Hand())
        draw_entire_game(1,'n',0) #draw a blank board with no cards that is shown for a second
        time.sleep(.75)

        #Deal the first card to each of the player's hands
        for i in range(hand_counter):
            all_player_hands[i].deal_card(deck)
            draw_entire_game(1,'n',0)
            time.sleep(.75)
        
        #Deal the dealer's first card
        nate_hand.deal_card(deck)
        draw_entire_game(1,'n',0)
        time.sleep(.75)

        #Deal the second card to each of the player's hands
        for i in range(hand_counter):
            all_player_hands[i].deal_card(deck)
            draw_entire_game(1,'n',0)
            time.sleep(.75)

        #Deal Nate's second card
        nate_hand.deal_card(deck)
        draw_entire_game(1,'n',0)

    #Don't Give Option to Split, Double Down, or hit if they dealer was dealt blackjack
    if nate_hand.calculate_value() != 21: 
    
        #Give Player Option to Split
        for i, hand in enumerate(all_player_hands):
            if player_bank >= bet_per_hand and (hand.check_for_split_option() != 'no'):
                if hand.check_for_split_option() == 'same_card':
                    card = hand.card1()
                    if card == 'A':
                        card = 'Ace'
                    elif card == 'K':
                        card = 'King'
                    elif card == 'Q':
                        card = 'Queen'
                    elif card == 'J':
                        card = 'Jack'
                    else:
                        card += '\''
                    question_string = f'Do you want to split your {card}s?'
                elif hand.check_for_split_option() == 'different_cards':
                    question_string = f'Do you want to split your{ordinals[i]} hand?'
                draw_entire_game(1,i,0)
                decision = yes_no_question(question_string,0)
                while decision == 'bad_input':
                    draw_entire_game(1,i,0)
                    decision = yes_no_question(question_string,1)
                if decision == 'y':
                    player_bank -= bet_per_hand
                    new_hand_position = len(all_player_hands) #
                    all_player_hands.append(Hand()) #Make the list one longer
                    draw_entire_game(1,'n',0)
                    time.sleep(.75)
                    all_player_hands[new_hand_position].cards.append(hand.cards.pop(0))
                    draw_entire_game(1,'n',0)
                    time.sleep(.75)
                    hand.deal_card(deck) #deal one card to the og hand
                    draw_entire_game(1,'n',0)
                    time.sleep(.75)
                    all_player_hands[new_hand_position].deal_card(deck) #deal one card to the new hand
                              
        #Give Player Option to Double Down
        if player_bank >= bet_per_hand: 
            if when_double == 'a': #Ask to double on every hand
                draw_entire_game(1,'n',0)
                decision = yes_no_question('Would you like to double down on any of your hands?',0)
                while decision == 'bad_input':
                    draw_entire_game(1,'n',0)
                    decision = yes_no_question('Would you like to double down on any of your hands?',1)
                if decision == 'y':
                    for i, hand in enumerate(all_player_hands):
                        if hand.calculate_value() < 21 and player_bank >= bet_per_hand:
                            player_bank = double_hand(i,player_bank)
            elif when_double == 'b': #ask to double down if their total is 9-11
                for i, hand in enumerate(all_player_hands):
                        if hand.calculate_value() in [9,10,11] and player_bank >= bet_per_hand:
                            player_bank = double_hand(i,player_bank)
            elif when_double == 'c': #ask to double down if their total is 9-11 or soft 16-18
                for i, hand in enumerate(all_player_hands):
                        if player_bank >= bet_per_hand:
                            if hand.calculate_value() in [9,10,11] or (hand.calculate_value() in [16,17,18] and hand.num_aces()):
                                player_bank = double_hand(i,player_bank)

        #Give Player Option to Hit
        for i, hand in enumerate(all_player_hands):
            Stand = False
            while hand.calculate_value() < 21 and hand.if_doubledown() == False and Stand == False and len(hand.cards)<5:
                if len(all_player_hands) == 1: #Say this if they only have one hand
                    draw_entire_game(1,'n',0)
                    decision = yes_no_question(f'Would you like to hit?',0)
                    while decision == 'bad_input':
                        draw_entire_game(1,'n',0)
                        decision = yes_no_question(f'Would you like to hit?',1)
                else:                          #Say this if they have multiple hands
                    draw_entire_game(1,i,0)
                    decision = yes_no_question(f'Would you like to hit on your{ordinals[i]} hand?',0)
                    while decision == 'bad_input':
                        draw_entire_game(1,i,0)
                        decision = yes_no_question(f'Would you like to hit on your{ordinals[i]} hand?',1)
                if decision == 'y':
                    hand.deal_card(deck)
                elif decision =='n':     #Player decides to stand
                    Stand = True
       
        #Make the dealer hit if they need to, dispay the animation for the dealing drawing
        dealer_draw = False
        for i in all_player_hands: #Check the player doesn't have all busts or all blackjacks
            if i.calculate_value()<21:
                dealer_draw = True
        draw_entire_game(1,'n',0) #add an animation here for the card flipping
        time.sleep(1)
        draw_entire_game(0,'n',0) #add an animation here for the card flipping
        time.sleep(1)
        if dealer_draw == True:
            while nate_hand.calculate_value()<17:  #Make the Dealer draw cards
                nate_hand.deal_card(deck)
                draw_entire_game(0,'n',0) 
                time.sleep(1)

#Determine Game Outcome, see if player can/wants to play again
    player_bank = payout_player(player_bank)
    if player_bank > most_money:
        most_money = player_bank
    profit = player_bank - previous_bank

    if profit > 0:
        result = f'You won ${profit} this round!'
    elif profit < 0:
        result = f'You lost ${abs(profit)} this round.' #abs removes the negative sign
    elif profit == 0:
        result = f'You broke even this round across your hands.'

    if nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2:
        dealer_outcome = 'Nate got Blackjack! Womp Womp'
    elif nate_hand.calculate_value() > 21:
        dealer_outcome = 'Nate busted!'
    elif nate_hand.calculate_value() <= 21:
        dealer_outcome = f'Nate got {nate_hand.calculate_value()}.'
    
    if player_bank < 10:
        draw_entire_game(0,'n',1)
        text_box(dealer_outcome,result,'You can no longer afford the table minimum bet.','Ralph is coming to collect on his loan',f'Your maximum chip total was ${most_money}')
        playing = False
    elif player_bank >= 2000 and highscore_run == False:
        draw_entire_game(0,'n',1)
        go_for_highscore = yes_no_question(dealer_outcome,result,'You Bankrupt Nate!','You and Ralph are planning a trip to Spain','Would you like to keep playing for a highscore?',0)
        while go_for_highscore == 'bad_input':
            draw_entire_game(0,'n',1)
            go_for_highscore = yes_no_question(dealer_outcome,result,'You Bankrupt Nate!','You and Ralph are planning a trip to Spain','Would you like to keep playing for a highscore?',1)
        if go_for_highscore == 'n':
            chip_total = f'Your maximum chip total was ${most_money}'
            print(top_space)
            text_box(chip_total,'Thank you for playing at Nate\'s blackjack table!')
            text_box(chip_total,'Thank you for playing at Nate\'s blackjack table!')
            playing = False
        elif go_for_highscore == 'y':
            highscore_run == True
    else:
        draw_entire_game(0,'n',1)
        decision = yes_no_question(dealer_outcome,result,f'Continue playing?',0)
        while decision == 'bad_input':
            draw_entire_game(0,'n',1)
            decision = yes_no_question(dealer_outcome,result,f'Continue playing?',1)
        if decision == 'n':
            clear_terminal()
            chip_total = f'Your maximum chip total was ${most_money}'
            print(top_space)
            text_box(chip_total)
            playing = False

#Make ordinal list unlimited
#splitting limit based on the screen size
#if you split aces you only get one more card(sideways), and if you get blackjack this way it only pays 1 to 1
#Add Insurance
#Add a fun things where if you pay off ralph something cool happens
#make doubled down card hidden until after dealer show
#make all questions like hitting, where if the player only has one hand ask them "do you want to split" instead of do you want to split your first hand
#Right now the cursor replaces nothing, meaning if the screen is narrow enough the cursor will shift certain lines of the display?
#make the bet spacing not a hard coded calculation like it is now
#shorten the cursor logic at the bottom of the main card printing function
#I don't think the bet circles can handle a bet size of four digits right now
#If you split, and make a new splittable hand through the split the game won't ask you if you want to split the created hand (this may depend on it's position)
#if you have exactly $10 left it fucks it up
#if player has all blackjacks dealer doesn't hit, but then at the end of the game it says dealer had like 11 or something it should say You had all blackjacks

#if len(all_player_hands) == 1:
#        ordinals = ['']
#    else:
#        ordinals = [' first',' second',' third',' fourth',' fifth',' sixth',' seventh',' eighth',' ninth',' tenth']

#Nate's Casino Rules for later
     #There is not splitting limit (though the game won't let you have more hands than your screen can display)
     #If you split Aces, you are only allowed to hit once after
     #You are allowed to split any cards of the same value, irregardless of if they are the same rank (eg you can split a J and a Q)