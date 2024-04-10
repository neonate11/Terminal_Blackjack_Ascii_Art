import os #For the ability to clear terminal on windows or linux
import random
import platform #For the ability to check the OS

##################################### Unique Hand Class ###############################################
class Hand:
    def __init__(self):
        self.cards = [] #the cards in a hand, starting empty
        self.bet = 0
        self.double = False
    def deal_card(self, deck):  #ability of the hand class to be dealt a card
        card=deck.pop()
        self.cards.append(card)
    def check_for_split_option(self):  #This returns true if you have the option to split
        split = False
        if len(self.cards) == 2:  #Make sure the player only has two cards
            card1_value = 0
            card2_value = 0
            card1 = self.cards[0].split(' ')[0] #Calculate the value of the first card
            if card1 == 'A':
                card1_value = 11
            elif card1 in ['K', 'Q', 'J']:
                card1_value = 10
            else:
                card1_value = int(card1)
            card2 = self.cards[1].split(' ')[0] #Calculate the value of the second card
            if card2 == 'A':
                card2_value = 11
            elif card2 in ['K', 'Q', 'J']:
                card2_value = 10
            else:
                card2_value = int(card2)
            if  card1_value == card2_value:  #See if the card values are the same
                split = True
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
    def save_bet(self,bet): #save a bet to a specific hand
        self.bet = bet
    def print_bet(self): #return the bet associated with a specific hand
        return self.bet
    def doubleddown(self): #Remember if you doubled down
        self.double = True
    def if_doubledown(self): #Return whether you doubled down
        return self.double
   
##################################### Custom Functions #####################################################

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
    for _ in range(6): #Use 6 Decks
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} {suit}')
    random.shuffle(deck)
    random.shuffle(deck)
    return deck

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

#Function for asking the user a yes or no question
def yes_no_question(*args):
    error_spacing = ''
    error_message = ''
    while True:
        draw_dealer_hand(0,1)
        text_box(*args,error_spacing,error_message)
        print('\n')
        answer = input((int((screen_width/2)-1)* ' ')+'>')
        if answer.isalpha() and (answer.lower() == 'y' or answer.lower() == 'n'):
            return answer.lower()
        else:
            error_spacing = ' '
            error_message = 'Please respond with y or n.'
            clear_terminal()
             
#Function for accepting a bet from the player
def make_bet():
    bet = 0
    i = len(all_player_hands)
    clear_terminal()
    error_spacing = ''
    error_message = ''
    while True:
        draw_dealer_hand(0,1) #draw the player bank
        text_box(f'You are playing {i} hands.',"How much would you like to bet per hand?",'','(You will be unable to split or double down','if you don\'t have enough money leftover)',error_spacing,error_message)
        pointer_string = f'{left_space}                            $'  #the set amount of spaces is to account for half of the text box width
        bet = input(pointer_string)
        if not bet.isdigit():
            error_spacing = ' '
            error_message = 'Bet must be a positive, whole number'
            clear_terminal()
        elif int(bet) > player_bank:
            error_spacing = ' '
            error_message = 'Bet exceeds available funds'
            clear_terminal()
        elif int(bet) > 500:
            error_spacing = ' '
            error_message = 'Bet above table maximum ($500)'
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
        while True:
            draw_dealer_hand(0,1)
            text_box('How many hands would you like to play this round?','The table maximum is starting five hands.',error_spacing,error_message)
            number_hands = input(input_pointer_with_spacing)
            if not number_hands.isdigit() or (int(number_hands) < 1) or (int(number_hands) > 5):
                error_spacing = ' '
                error_message = 'Please provide an integer from 1 to 5.'
                clear_terminal()
            elif int(number_hands) * 10 > player_bank:
                error_spacing = ' '
                error_message = 'You can\'t afford to play that many hands with a $10 min bet'
                clear_terminal()
            else:
                break
        if int(number_hands) >=2:
            second_hand = Hand()
            all_player_hands.append(second_hand)
            second_hand.deal_card(deck)
            second_hand.deal_card(deck)
        if int(number_hands) >=3:
            third_hand = Hand()
            all_player_hands.append(third_hand)
            third_hand.deal_card(deck)
            third_hand.deal_card(deck)
        if int(number_hands) >=4:
            fourth_hand = Hand()
            all_player_hands.append(fourth_hand)
            fourth_hand.deal_card(deck)
            fourth_hand.deal_card(deck)
        if int(number_hands) ==5:
            fifth_hand = Hand()
            all_player_hands.append(fifth_hand)
            fifth_hand.deal_card(deck)
            fifth_hand.deal_card(deck)
          
#Function to Determine the outcome of the game
def determine_outcome(player_bank,bet_per_hand):
    if len(all_player_hands) == 1:
        ordinals = ['']
    else:
        ordinals = [' first',' second',' third',' fourth',' fifth',' sixth',' seventh',' eighth',' ninth',' tenth']
    for i, hand in enumerate(all_player_hands):
        bet_per_hand_with_double = bet_per_hand
        if hand.if_doubledown():
            bet_per_hand_with_double = 2*bet_per_hand #Double bet per hand if they doubled down
        #The Player Busted:
        if hand.calculate_value() > 21:                                                   
            print(f'Your{ordinals[i]} hand busted, you lost ${bet_per_hand_with_double}')
        #The Player and Dealer Tied:
        elif hand.calculate_value() == nate_hand.calculate_value():
            print(f'Your{ordinals[i]} hand was a push, you got your bet back')
            player_bank += bet_per_hand_with_double
        #The Dealer got Blackjack:
        elif nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2:
            print(f'Nate beat your{ordinals[i]} hand with Blackjack, you lost ${bet_per_hand_with_double}')
        #The Player got BLackjack:
        elif hand.calculate_value() == 21 and len(hand.cards) == 2:
            print(f'Your{ordinals[i]} hand got Blackjack! You won ${1.5*bet_per_hand_with_double}')
            player_bank += 2*(1.5*bet_per_hand_with_double)
        #The Player got 5 cards without busting:
        elif len(hand.cards) == 5:                                                         
            print(f'You have five cards and didn\'t bust, you won ${bet_per_hand_with_double}!')
            player_bank += 2*(bet_per_hand_with_double)
        #The Dealer Busted:
        elif nate_hand.calculate_value() > 21:
            print(f'Nate busts, your{ordinals[i]} hand won ${bet_per_hand_with_double}!')
            player_bank += 2* (bet_per_hand_with_double)
        #The Dealer total was higher:
        elif hand.calculate_value() > nate_hand.calculate_value():
            print(f'Your{ordinals[i]} hand beat Nate! You won ${bet_per_hand_with_double}')
            player_bank += 2*(bet_per_hand_with_double)
        #The Player total was higher:
        elif hand.calculate_value() < nate_hand.calculate_value():
            print(f'Nate beat your{ordinals[i]} hand, you lost ${bet_per_hand_with_double}')
    return player_bank

##################################### GRAPHICS #####################################################

#Function to draw the top of the board (either just player bank or player bank and the dealer's hands)
def draw_dealer_hand(hide,just_bank): 
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
            suit = card[-1]
            formatted_data = rank + suit
            lines[0] += '┌─────────┐'
            lines[1] += '│{}       │'.format(formatted_data)
            lines[2] += '│         │'
            lines[3] += '│    {}    │'.format(suit)
            lines[4] += '│         │'
            lines[5] += '│       {}│'.format(formatted_data)
            lines[6] += '└─────────┘'
        if hide:
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
def draw_all_player_hands(all_player_hands,location):
    #make empty lists for the final printing list, and list of correct characters to append per hand
    lines = []
    linestoprint = []
    for i in range(15):
        lines.append('')
        linestoprint.append('')
    spacing = int((screen_width-(len(all_player_hands)*23))/(len(all_player_hands)+1))
    for z, hand in enumerate(all_player_hands):
        left_edge_data = [] #For left edge data, space is on right
        right_edge_data = [] #For right edge data, space is on left
        covered_data = [] #if a 10 is underneath another card, don't print the suit
        suits = [] #just for printing the middle part of card
        for card in hand.cards:
            rank=card[0]
            rank2 = card[1]
            suit=card[-1]
            suits.append(suit)
            if rank2.isdigit(): #If the card is a 10, need to print the second integer (0) and delete the extra space
                left_edge_data.append(rank+rank2+suit)
                right_edge_data.append(rank+rank2+suit)
                covered_data.append(rank+rank2)
            else: #If the card is not a 10, need an extra space
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
        if location == z:      #if we are referring to this hand currently add the cursor (this part also adds the spacing between hands -2 to account for the cursor)
            linestoprint[10]+= ' '*(spacing-2)+'➤ ' #Add the cursor
            linestoprint[11]+= ' '*(spacing-2)+'➤ ' #Add the cursor
            linestoprint[12]+= ' '*(spacing-2)+'➤ ' #Add the cursor
        else:                  #if we aren't referring to this hand currently put just spaces
            linestoprint[10]+= ' '*spacing 
            linestoprint[11]+= ' '*spacing 
            linestoprint[12]+= ' '*spacing 
        for n in range(15):
            linestoprint[n]+=lines[n]
           

    #Add the correct line for the current hand to the final output list
    for i in linestoprint:
        print(i)

#Function to draw bets under their associated hand
def draw_bets(all_player_hands,bet_per_hand):
    lines = []
    spacing = int((screen_width-(len(all_player_hands)*23))/(len(all_player_hands)+1)) #This determines appropriate spacing between the bet graphics
    for i in range(6):
        lines.append('')
    for i, hand in enumerate(all_player_hands):
        for i in range(6):
            lines[i]+= ' '*spacing
        bet = bet_per_hand
        if hand.if_doubledown():
            bet = bet_per_hand*2
        bet_spacing = '  '
        if len(str(bet_per_hand)) == 3:
            bet_spacing = ' '
        elif len(str(bet_per_hand)) == 4:
            bet_spacing = ''
        lines[0] += '    =  =               '                  
        lines[1] += ' =        =            ' 
        lines[2] += '=   Bet:   =           '
        lines[3] += '=   ${}{}  =           '.format(bet,bet_spacing)                
        lines[4] += ' =        =            '                       
        lines[5] += '    =  =               '
    for i in lines:
        print(i)     

#Function to call all graphics functions
def draw_entire_game(all_player_hands,bet_per_hand,hide,location):
    clear_terminal()
    draw_dealer_hand(hide,0)
    draw_all_player_hands(all_player_hands,location)
    draw_bets(all_player_hands,bet_per_hand)

##################################### actions to only do once on startup ######################################
#General Variable Setup
player_bank = 100 #Player Starting Cash
ordinals = [' first',' second',' third',' fourth',' fifth',' sixth',' seventh',' eighth',' ninth',' tenth']
highscore_run = False #For remembering if the player has already beat the dealer
most_money = 100 #For printing the player's highscore when they lose or quit
screen_width = os.get_terminal_size()[0] #0 is the width, 1 is the height
screen_height = os.get_terminal_size()[1]
left_space = int((screen_width/2)-28)* ' ' #half of 56 is 28, this is just used for the text boxes I think
dealer_spacing = int((screen_width -36)/2) #used to the left of the dealers hand
top_space = '\n'*27

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
print('')
print(bj_space,'                                       [press enter to continue]')
input()
clear_terminal()

#Print Introductory Message, Give option to read rules
see_rules = yes_no_question('Welcome to Nate\'s blackjack table','Your friend Ralph has lent you $100 in chips','Win $2000 to bankrupt Nate','Would you like to read the rules?')
if see_rules == 'y':
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
   
############################################ the game loop ############################################
playing = True
while playing:
    clear_terminal()
    deck = make_deck()  
    all_player_hands = []
    first_hand = Hand()
    all_player_hands.append(first_hand)
    nate_hand = Hand()
    first_hand.deal_card(deck)
    nate_hand.deal_card(deck)
    first_hand.deal_card(deck)
    nate_hand.deal_card(deck)

    #determining spacing between hands and bets
    num_hands = len(all_player_hands)
           
    #Give PLayer Option of How Many Hands to Start with
    starting_hands()
                  
    #Find out how much the player wants to bet
    total_bet_this_round = 0 
    bet_per_hand = make_bet() #Take Player's Initial Bet
    for i, hand in enumerate(all_player_hands):
        total_bet_this_round += bet_per_hand #Sum the total amount bet so far
        player_bank -= bet_per_hand

    dealing = True #Setup Game Phase where cards are dealt
    while dealing:
        if nate_hand.calculate_value() == 21: #Don't Deal Cards if Dealer already got Blackjack
            dealing = False

        #Give Player Option to Split
        for i, hand in enumerate(all_player_hands):
            if player_bank >= bet_per_hand and hand.check_for_split_option():
                draw_entire_game(all_player_hands,bet_per_hand,1,i)
                decision = yes_no_question(f'Would you like to split your{ordinals[i]} hand?')
                if decision == 'y':
                    total_bet_this_round += bet_per_hand #deduct another bet from the player bank
                    player_bank -= bet_per_hand
                    new_hand_position = len(all_player_hands) #
                    all_player_hands.append(Hand()) #Make the list one longer
                    all_player_hands[new_hand_position].cards.append(hand.cards.pop(0))
                    hand.deal_card(deck) #deal one card to the og hand
                    all_player_hands[new_hand_position].deal_card(deck) #deal one card to the new hand
                               
        #Give Player Option to Double Down
        if player_bank >= bet_per_hand:
            draw_entire_game(all_player_hands,bet_per_hand,1,'n')
            text_box('Would you like to double down on any of your hands?','[y or n]')
            decision = yes_no_question(input_pointer_with_spacing)
            if decision == 'y':
                for i, hand in enumerate(all_player_hands):
                    if hand.calculate_value() < 21 and player_bank >= (total_bet_this_round + bet_per_hand):
                        draw_entire_game(all_player_hands,bet_per_hand,1,i)
                        question_string = f"Would you like to double down on your{ordinals[i]} hand?"
                        text_box(question_string,'[yes or no]')
                        decision = yes_no_question(input_pointer_with_spacing)
                        if decision == 'y':
                            total_bet_this_round += bet_per_hand
                            player_bank -= bet_per_hand
                            hand.doubleddown()
                            hand.deal_card(deck)

        #Give Player Option to Hit
        for i, hand in enumerate(all_player_hands):
            Stand = False
            while hand.calculate_value() < 21 and hand.if_doubledown() == False and Stand == False and len(hand.cards)<5:
                if len(all_player_hands) == 1: #Say this if they only have one hand
                        question_string = f'Would you like to hit?'
                else:                          #Say this if they have multiple hands
                    question_string = f'Would you like to hit on your{ordinals[i]} hand?'
                draw_entire_game(all_player_hands,bet_per_hand,1,i)
                text_box(question_string,'[yes or no]')
                decision = yes_no_question(input_pointer_with_spacing)
                if decision == 'y':
                    hand.deal_card(deck)
                elif decision =='n':     #Player decides to stand
                    Stand = True
       
        #Make the dealer hit if they need to
        dealer_draw = False
        for i in all_player_hands: #Check the player doesn't have all blackjacks or all busts
            if i.calculate_value()<21:
                dealer_draw = True
        if dealer_draw == True:
            while nate_hand.calculate_value()<17:  #Make the Dealer draw cards
                nate_hand.deal_card(deck)

        dealing = False #Dealing Phase is done
   
    #Determine Game Outcome
    draw_entire_game(all_player_hands,bet_per_hand,0,'n')
    player_bank = determine_outcome(player_bank,bet_per_hand)
    print('')

    if player_bank > most_money:
        most_money = player_bank
    #Check if the player is broke or won, and wants to play again
    if player_bank < 10:
        string = f'Your maximum chip total was ${most_money}'
        text_box('You can no longer afford the table minimum bet.','Ralph is coming to collect on his loan',string)
        playing = False
    elif player_bank >= 2000 and highscore_run == False:
        print(top_space)
        text_box('You Bankrupt Nate! You and Ralph are planning a trip to Spain','Would you like to keep playing for a highscore?','[yes or no]')
        go_for_highscore = yes_no_question(input_pointer_with_spacing)
        if go_for_highscore == 'n':
            chip_total = f'Your maximum chip total was ${most_money}'
            print(top_space)
            text_box(chip_total)
            playing = False
        elif go_for_highscore == 'y':
            highscore_run == True
    else:
        question_string = f'Continue playing? You have ${player_bank}.'
        text_box(question_string,'[yes or no]')
        decision = yes_no_question(input_pointer_with_spacing)
        if decision == 'n':
            clear_terminal()
            chip_total = f'Your maximum chip total was ${most_money}'
            print(top_space)
            text_box(chip_total)
            playing = False


#print message if a player busts or gets blackjack before they have option to hit on next hand
#Make ordinal list unlimited
#splitting limit
#Add timer to seal dealing, and make deal clockwise
#if you split aces you only get one more card(sideways), and if you get blackjack this way it only pays 1 to 1
#Add Insurance
#See if you can delete all player hands as an input to those functions
#Add a fun things where if you pay off ralph something cool happens
#make doubled down card hidden until after dealer show
#Add ability to start more than two hands
#Fix Instructions to have categories like: double down, and explain which hands are first
#Make bet circle display outcome, not text
#make top spacing before text boxes a fixed value based on the display of the cards and bets, not a calculation like it is now
#look at making yes no question function not require an input every time for the pointer spacing
#make all questions like hitting, where if the player only has one hand ask them "do you want to split" instead of do you want to split your first hand
#make error messages formatted better than being in top left corner
#need to check if player can afford 3-5 hands
#can probably simpllify the part that asks how many hands the player wants to play(set up a library or whatever it was called that maps words to numbers)
#add buttons or links for questions so the user doesn't have to type
#add a bank in the top left corner
#delete the total bet this round variable
#Can shorten the logic/overall code of the section #Give PLayer Option of How Many Hands to Start with
#make drawing 5 cards win automatically regardless of what the dealer has
#under determining game outcome reference near the bottom of the code there is a space i think that was fucking up some other spacing somewhere
#fix end of game message so it is more clear what happend to each hand, this will let you fix error where it shows the wrong chip count in the top left at the end of the game
#I think there is a glitch where if you win blackjack and the won amount is a decimal it fucks stuff up
#Check splitting I don't think it works anymore
#don't let the player play enough hands or split hands if the amount of hands could not be displayed on the screen