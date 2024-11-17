import os #For the ability to clear terminal, and pull terminal dimensions
import random
import platform #For the ability to check the OS
import time #For the ability to pause for animations
from card_graphics import *
#############################################################################################################################################################################################
######################## CUSTOM HAND CLASS and LOW LEVEL FUNCTIONS ########################### CUSTOM HAND CLASS and LOW LEVEL FUNCTIONS ####################################################
#############################################################################################################################################################################################
#Function to check the OS
def what_OS():
    if platform.system() == 'Windows':
        return 'Windows'
    else:
        return 'Linux'
Op_Sys = what_OS()

#Function to clear the terminal screen
def clear_terminal():
    if Op_Sys == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
clear_terminal() #want to clear terminal as soon as possible so the game looks cleaner

class Hand:
    def __init__(self):
        self.cards = [] #the cards in a hand, starting empty
        self.double = False
        self.split_Aces = False
    def deal_card(self, deck):  #ability of the hand class to be dealt a card
        card=deck.pop()
        self.cards.append(card)
    def card1(self): #This will return the rank of the first card in a hand(eg return 10)
        return (self.cards[0].split(' ')[0])
    def card2(self): #This will return the rank of the second card in a hand(eg return 10)
        return (self.cards[1].split(' ')[0])
    def card_rank_and_suit(i,self):
        return (self.cards[i].split(' ')[0])
    def check_for_split_option(self):  #This returns true if you have the option to split
        if len(self.cards) !=2:
            return 'no'
        elif self.check_if_split_aces():
            return 'no'
        elif  self.card1() == self.card2():  #See if the cards are the same
            return 'same_card'
        elif self.card1() in ['K', 'Q', 'J','10'] and self.card2() in ['K', 'Q', 'J','10']: #see if both cards are 10 value cards
            return 'different_cards'
        return 'no'
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
        return sum(1 for card in self.cards if card.split(' ')[0] == 'A')
    def doubleddown(self): #Mark a hand as doubled down
        self.double = True
    def if_doubledown(self): #Return whether you doubled down
        return self.double
    def remember_split_aces(self): #Mark a hand as being from split aces
        self.split_Aces = True
    def check_if_split_aces(self): #Return whether this hand is from splitting Aces
        return self.split_Aces

#Makes the Deck
def make_deck():
    suits = ['\u2663', '\u2665', '\u2666', '\u2660']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
    deck = []
    for i in range(6): #Use 6 Decks
        for suit in suits:
            for rank in ranks:
                deck.append(f'{rank} {suit}')
    random.shuffle(deck)
    random.shuffle(deck)
    return deck

#Function for asking the user a yes or no question
def yes_no_question(draw_bank_only,hide,location,endgame,*args):   
    screen_width = os.get_terminal_size()[0]
    input_pointer_with_spacing = ((int((screen_width/2)-1)* ' ')+'>')
    error_spacing = '' #error_spacing is a blank line printed before an error message, only if an error message is generated
    error_message = '' 
    while True:
        if draw_bank_only == 'draw_bank_only':
            screen_width = os.get_terminal_size()[0] 
            draw_dealer_hand(1,1,screen_width)
        else:
            draw_entire_game(hide,location,endgame)
            print('\n')
        text_box(*args,error_spacing,error_message) 
        print('\n')
        answer = input(input_pointer_with_spacing)
        if answer.isalpha() and (answer.lower() in ['y','n','yes','no','debug']):
            return answer[0].lower()
        elif answer.isalpha() and answer == 'DEBUG': #Player can enter debug mode by answering DEBUG to the first question
            return 'debug'
        else:
            error_spacing = ' '
            error_message = 'Please respond with yes or no.'

#Function to nicely print numbers with correct amount of decimals, dollar signs, and commas
def format_money(number_to_format):
    string = str(number_to_format)
    if '.' in string:
        parts = string.split('.')
        if not all(char == '0' for char in parts[1]): #only if there is a decimal number thats not all zeroes will it print the decimal number
            return f'${number_to_format:,.2f}'
        else:
            return f'${number_to_format:,.0f}'
    else:
        return f'${number_to_format:,.0f}'
#############################################################################################################################################################################################
##################################### GAMEPLAY AND USER INPUT FUNCTIONS ####################################### GAMEPLAY AND USER INPUT FUNCTIONS############################################
#############################################################################################################################################################################################          
#Function for accepting a bet from the player
def make_bet():
    screen_width = os.get_terminal_size()[0] 
    left_space = int((screen_width/2)-28)* ' ' #28 accounts for half the width of text boxes
    i = starting_hands
    error_spacing = ''
    error_message = ''
    if (starting_hands * 10) == player_bank: #If the player can't afford a bet above the table minimum don't ask
        return 10
    while True:
        clear_terminal()
        screen_width = os.get_terminal_size()[0] 
        draw_dealer_hand(0,1,screen_width) #draw the player bank
        string = 'hands' if i != 1 else 'hand'
        string2 = 'bet per hand' if i != 1 else 'bet'
        text_box(f'You are playing {numbers[i]} {string}.',f"How much would you like to {string2}?",' ','(You will be unable to split or double down','if you don\'t have money leftover)',error_spacing,error_message)
        bet_input = input(f'{left_space}                            $')   #the set amount of spaces is to account for half of the text box width
        if not bet_input.isdigit():
            error_spacing = ' '
            error_message = 'Bet must be a positive, whole number'
        elif int(bet_input) > player_bank:
            error_spacing = ' '
            error_message = 'Bet exceeds available funds'
        elif int(bet_input) > 1000:
            error_spacing = ' '
            error_message = 'Bet above table maximum ($1000)'
        elif (int(bet_input)*i) > player_bank:
            error_spacing = ' '
            error_message = 'Amount bet across all hands exceeds available funds'
        elif int(bet_input) < 10:
            error_spacing = ' '
            error_message = 'Bet below table minimum ($10)'
        else:
            return int(bet_input)

#Function for determining number of starting hands:
def ask_how_many_starting_hands():
    if player_bank >= 20: #Player can't play two hands if they don't have at least $20
        error_spacing = ''
        error_message = ''
        error_message2 = ''
        while True:
            clear_terminal()
            screen_width = os.get_terminal_size()[0] 
            input_pointer_with_spacing = ((int((screen_width/2)-1)* ' ')+'>')
            draw_dealer_hand(0,1,screen_width)
            text_box('How many hands would you like to play this round?','The table maximum is starting five hands.',error_spacing,error_message,error_message2)
            number_hands = input(input_pointer_with_spacing)
            if number_hands.isdigit() and int(number_hands) >5:
                error_spacing = ' '
                error_message = 'The table maximum is starting 5 hands.'
                error_message2 = ''
            elif number_hands.isdigit() and int(number_hands) <1:
                error_spacing = ' '
                error_message = 'You must play at least one hand.'
                error_message2 = ''
            elif number_hands.isdigit() and int(number_hands) * 10 > player_bank:
                error_spacing = ' '
                error_message = 'You can\'t afford to play that many hands.'
                error_message2 = 'The table minimum bet is $10 a hand.'
            elif number_hands.isdigit() and int(number_hands) * 25 > screen_width:
                error_spacing = ' '
                error_message = 'Your screen cannot display that many hands.'
                error_message2 = 'Expand your screen or play fewer hands.'
            elif not number_hands.isdigit():
                error_spacing = ' '
                error_message = 'Please provide an integer from 1 to 5.'
                error_message2 = ''
            else:
                return (int(number_hands))
    else: #if the player can't afford to play two hands set the starting_hands variable equal to 1
        return(1)

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
        elif hand.calculate_value() == 21 and len(hand.cards) == 2:  #Player Blackjack
            if nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2: #and Dealer Blackjack
                player_bank += .5 * payout #Push
            else:
                if not hand.check_if_split_aces(): 
                    player_bank += ((1.5 * bet_per_hand) + bet_per_hand) #Player Paid out for Blackjack on a non split aces hand
                else:
                    player_bank += payout
        elif hand.calculate_value() == nate_hand.calculate_value(): #The Player and Dealer Pushed
            player_bank += .5 * payout
        elif nate_hand.calculate_value() > 21:                       #Dealer Busted
            player_bank += payout
        elif hand.calculate_value() > nate_hand.calculate_value():   #The Players total was higher:
            player_bank += payout
        elif hand.calculate_value() < nate_hand.calculate_value():   #The Dealer Total was higher:
            pass
    return player_bank

#Function to Give Player Option to Split
def give_split_option(player_bank):
    i = 0
    while i < len(all_player_hands): #This needs to be done with the index, in case a hand it split and a splittable hand is created in its previous location
        hand = all_player_hands[i]
        split_option = hand.check_for_split_option()
        if player_bank >= bet_per_hand and split_option != 'no': #if you can split the hand
            screen_width = os.get_terminal_size()[0] 
            if (len(all_player_hands)+1) * 25 > screen_width:
                draw_entire_game('hide','n','not_endgame')
                text_box('You have a splittable hand but your','screen cannot display another hand.','Expand your screen if possible.',' ','[press enter to continue]')
                input()
                screen_width = os.get_terminal_size()[0] 
                if (len(all_player_hands)+1) * 25 > screen_width:
                    break
            if split_option == 'same_card':
                question_string = f'Do you want to split your {card_ranks_plural[hand.card1()]}?'
            elif split_option == 'different_cards':
                question_string = f'Do you want to split your {hand.card1()} {hand.card2()}?'
            decision = yes_no_question('print_entire_game','hide',i,'not_engame',question_string)
            if decision == 'y':
                player_bank -= bet_per_hand
                new_hand_position = len(all_player_hands) #
                all_player_hands.append(Hand())                                     #add another hand to all_player_hands
                draw_entire_game('hide','n','not_endgame')
                time.sleep(.5)
                all_player_hands[new_hand_position].cards.append(hand.cards.pop(0)) #move one card from OG to new hand
                draw_entire_game('hide','n','not_endgame')
                time.sleep(.5)
                if hand.card1() == 'A': #Have both hands remember they split Aces
                    hand.remember_split_aces()
                    all_player_hands[new_hand_position].remember_split_aces()
                hand.deal_card(deck)                                                #deal one card to the og hand
                draw_entire_game('hide','n','not_endgame')
                time.sleep(.5)
                all_player_hands[new_hand_position].deal_card(deck)                 #deal one card to the new hand
                i -= 1
        i += 1

#Function for asking the user when they would like to be asked to double down
def ask_when_to_double():
    screen_width = os.get_terminal_size()[0] 
    input_pointer_with_spacing = ((int((screen_width/2)-1)* ' ')+'>')
    error_spacing = ''
    error_message = ''
    while True:
        screen_width = os.get_terminal_size()[0] 
        draw_dealer_hand(0,1,screen_width)
        text_box('When would you like to be asked to double down?',' ','A: for every hand','B: your count is hard 9-11','C: your count is hard 9-11 or soft 16-18','D: never',error_spacing,error_message)
        when_double = input(input_pointer_with_spacing)
        if when_double.isalpha() and when_double.lower() in ['a','b','c','d']:
            return(when_double.lower())
        else:
            error_spacing = ' '
            error_message = 'Please respond with A, B, C, or D'
            clear_terminal()

#Function for asking the player if they want to double down on any of their hands
def give_double_down_option(player_bank):
    if player_bank >= bet_per_hand: 
        if when_double == 'a': #Ask to double on every hand
            if len(all_player_hands) > 2:
                decision = yes_no_question('print_entire_game','hide','n','not_endgame','Would you like to double down on any of your hands?')
            else:
                decision = 'y'
            if decision == 'y':
                for i, hand in enumerate(all_player_hands):
                    if hand.calculate_value() < 21 and player_bank >= bet_per_hand and not hand.check_if_split_aces(): #FIX THE CHECKING NOT SPLIT ACES CRITERIA
                        player_bank = double_hand(i,player_bank)
        else:  # For scenarios b and c
            for i, hand in enumerate(all_player_hands):
                hand_value = hand.calculate_value()
                if (not hand.check_if_split_aces() and (when_double == 'b' and hand_value in [9, 10, 11] and player_bank >= bet_per_hand) or \
                (when_double == 'c' and player_bank >= bet_per_hand and (hand_value in [9, 10, 11] or (hand_value in [16, 17, 18] and hand.num_aces())))): #FIX THE CHECKING NOT SPLIT ACES CRITERIA
                    player_bank = double_hand(i, player_bank)

#Function for asking the user if they want to double down on a specific hand
def double_hand(i,player_bank):
    if len(all_player_hands) == 1:
        question_string = 'Do you want to double down on your hand?'
    else:
        question_string = f"Do you want to double down on your{ordinals[i]} hand?"
    decision = yes_no_question('print_entire_game','hide',i,'not_endgame',question_string)
    if decision == 'y':
        player_bank -= bet_per_hand
        hand.doubleddown()
        hand.deal_card(deck)
    return player_bank

#Function to prompt the player to hit or stand
def give_hit_option():
    for i, hand in enumerate(all_player_hands):
        Stand = False
        while hand.calculate_value() < 21 and hand.if_doubledown() == False and Stand == False and len(hand.cards)<5 and not hand.check_if_split_aces():
            if len(all_player_hands) == 1: #Say this if they only have one hand
                decision = yes_no_question('print_entire_game','hide','n','not_endgame',f'Would you like to hit?')
            else:                          #Say this if they have multiple hands
                decision = yes_no_question('print_entire_game','hide',i,'not_endgame',f'Would you like to hit on your{ordinals[i]} hand?')
            if decision == 'y':
                hand.deal_card(deck)
            elif decision =='n':     #Player decides to stand
                Stand = True
#############################################################################################################################################################################################
##################################### GRAPHICS FUNCTIONS ####################################### GRAPHICS FUNCTIONS##########################################################################
#############################################################################################################################################################################################
#Function to draw the top of the board (either just player bank or player bank and the dealer's hands)
def draw_dealer_hand(hide,just_bank,screen_width): 
    dealer_spacing = ((screen_width -36)//2) #used to the left of the dealers hand
    dealer_cards= []
    after_bank_spacing = ((dealer_spacing-18)*' ') #13 is how wide the player bank box is
    dealer_cards.append( '┌────────────────┐' + after_bank_spacing)
    dealer_cards.append( '│ Total invested:│' + after_bank_spacing)
    dealer_cards.append(f'│{format_money(total_bought_in_for):^16}│' + after_bank_spacing)
    dealer_cards.append( '│                │' + after_bank_spacing)
    dealer_cards.append( '│  Your Chips:   │' + after_bank_spacing)
    dealer_cards.append(f'│{format_money(player_bank):^16}│' + after_bank_spacing)
    dealer_cards.append( '└────────────────┘' + after_bank_spacing)
    if not just_bank:   #if drawing the bank and the dealer's cards
        for i in range(1):
            dealer_cards.append(dealer_spacing*' ') #Add spaces before the 6th and 7th lines of the cards that don't have the bank to their left
        cards_to_print_faceup = len(nate_hand.cards)
        cards_to_print_facedown = 0
        if hide == 'hide': #if the argument input is hide draw one card face up
            cards_to_print_faceup = 1
            cards_to_print_facedown = 1
        elif hide == 'first': #if the argument input is first draw no cards face up
            cards_to_print_faceup = 0
            cards_to_print_facedown = 1
        elif hide == 'second': #if the argument input is first draw no cards face up
            cards_to_print_faceup = 0
            cards_to_print_facedown = 2

        for card in nate_hand.cards[:cards_to_print_faceup]:
            card_graphic = return_card(card,False,Op_Sys)
            for i in range(7):
                dealer_cards[i]+= card_graphic[i]
        for card in nate_hand.cards[:cards_to_print_facedown]:  # Iterate over the cards to print
            if hide in ['hide','first','second'] and len(nate_hand.cards)>=1: #Don't print a hidden card before no cards are dealt
                card_graphic = return_card('back side',False,Op_Sys)
                for i in range(7):
                    dealer_cards[i]+= card_graphic[i]

        return dealer_cards
    elif just_bank: #if just drawing the bank
        for i in range(13):
            dealer_cards.append('\n')
        clear_terminal()
        for i in dealer_cards:
            print(i)

#Function to draw all player hands
def draw_all_player_hands(lines,location,endgame,side_spacing):
    #Reference Printing Formatting
    #player_cards[0]  = '            ┌─────────┐'
    #player_cards[1]  = '            │         │'
    #player_cards[2]  = '         ┌──│         │'
    #player_cards[3]  = '         │  │         │'
    #player_cards[4]  = '      ┌──│  │         │'
    #player_cards[5]  = '      │  │  │         │'
    #player_cards[6]  = '   ┌──│  │  └─────────┘'
    #player_cards[7]  = '   │  │  │         │   '
    #player_cards[8]  = '┌──│  │  └─────────┘   '
    #player_cards[9]  = '│  │  │         │      '
    #player_cards[10] = '│  │  └─────────┘      '
    #player_cards[11] = '│  │         │         '
    #player_cards[12] = '│  └─────────┘         '
    #player_cards[13] = '│         │            '
    #player_cards[14] = '└─────────┘            '
    #The way the following logic works is by updating certain lines within the list player_cards, for instance 
    #to update the third card we are updating lines 4 through 10, when we update we have to keep the 
    #underneath card visible, then add the new card, then add appropriate spacing on the right side so 
    #player_cards is a consistent length
    cursor_and_spacing = [''] * 15
    final_formatting = [''] * 15
    for z, hand in enumerate(reversed(all_player_hands)):
        player_cards = ['                       '] * 15 #Need a blank for dealing animation
        if len(hand.cards) >= 1:                                               #First Card
            card_graphic = return_card(hand.cards[0],False,Op_Sys)
            for b in range(7):
                player_cards[b+8]=card_graphic[b]+'            '
        if len(hand.cards) >= 2 and hand.check_if_split_aces():                #Second Card (Doubled Down)
            card_graphic = return_card(hand.cards[1],True,Op_Sys)
            for c in range(5):
                player_cards[c+6]=player_cards[c+6][0:3]+card_graphic[c]+'     '
        if len(hand.cards) >= 2 and not hand.check_if_split_aces():            #Second Card
            card_graphic = return_card(hand.cards[1],False,Op_Sys)
            for d in range(7):
                player_cards[d+6]=player_cards[d+6][0:3]+card_graphic[d]+'         '
        if hand.if_doubledown() and (endgame == 'endgame' or not hide_double): #Third card (Doubled Down, Faceup)
            card_graphic = return_card(hand.cards[2],True,Op_Sys)
            for e in range(5):
                player_cards[e+4]=player_cards[e+4][0:7]+card_graphic[e]+' '
        elif hand.if_doubledown() and endgame == 'not_endgame':                #Third Card (Doubled Down, Face Down)
            card_graphic = return_card('back side',True,Op_Sys)
            for f in range(5):
                player_cards[f+4]=player_cards[f+4][0:7]+card_graphic[f]+' '
        elif not hand.if_doubledown():
            if len(hand.cards) >= 3:                                           #Third Card
                card_graphic = return_card(hand.cards[2],False,Op_Sys)
                for g in range(7):
                    player_cards[g+4]=player_cards[g+4][0:6]+card_graphic[g]+'      '
            if len(hand.cards) >= 4:                                           #Fourth Card
                card_graphic = return_card(hand.cards[3],False,Op_Sys)
                for h in range(7):
                    player_cards[h+2]=player_cards[h+2][0:9]+card_graphic[h]+'   '
            if len(hand.cards) >= 5:                                           #Fifth Card
                card_graphic = return_card(hand.cards[4],False,Op_Sys)
                for i in range(7):
                    player_cards[i]=player_cards[i][0:12]+card_graphic[i]

        for j in range(0,15): #Add the spacing for these lines
            cursor_and_spacing[j]= '  '
        if location == (len(all_player_hands) -1)-z:      #if we are referring to this hand currently add the cursor (this part also adds the spacing between hands -2 to account for the cursor)
            cursor_and_spacing[10]= '➤ ' #Add the cursor
            cursor_and_spacing[11]= '➤ ' #Add the cursor
            cursor_and_spacing[12]= '➤ ' #Add the cursor
        for k in range(15):
            final_formatting[k]+= (cursor_and_spacing[k]+player_cards[k])

    for l in range(15):
        final_formatting[l] = (side_spacing+final_formatting[l]+side_spacing)
    lines.extend(final_formatting)
    return lines

#Function to draw bets under their associated hand, this will also print the result of a hand within the bet circle
def draw_bets(lines,endgame,side_spacing):
    bet_display = ['' for i in range(6)]
    for i, hand in enumerate(reversed(all_player_hands)):
        bet = bet_per_hand
        if hand.if_doubledown():
            bet = bet_per_hand*2
        push_return_amt = bet  #In case player pushes a blackjack you want to return the original bet placed, not how much blackjack would have paid
        if hand.calculate_value() == 21 and len(hand.cards) == 2 and not hand.check_if_split_aces(): #Don't increase payout if blackjack is made on split aces
            bet = bet * 1.5
        bet_string_payout = f'+{format_money(bet)}' #appends a plus sign
        bet_string_lost = f'-{format_money(bet)}' #appends a neg sign
        bet_display[0] += '      =  =               '         
        bet_display[1] += '   =        =            '         
        bet_display[4] += '   =        =            '    
        bet_display[5] += '      =  =               ' 
        hide_busted = False
        if hand.if_doubledown() and hide_double:
            hide_busted = True                              
        #these first two scenarios always win or lose so we can print no matter what stage of the game we are in
        if hand.calculate_value() > 21 and not hide_busted:                   #Player Busted, don't reveal this is the player busted down on a double down since the card is hidden until the end 
                bet_display[2] += f'  =  BUSTED  =           '
                bet_display[3] += f'  ={bet_string_lost:^10}=           '
        elif len(hand.cards) == 5:                                                     #The Player got 5 cards without busting: 
                bet_display[2] += f'  =5 no bust =           '
                bet_display[3] += f'  ={bet_string_payout:^10}=           '
        #the dealer's hand has already been revealed, you can now show the results of every hand
        elif endgame == 'endgame':
            if hand.calculate_value() > 21:                                             #this is needed if the player busts on a double down card that was hidden previously
                bet_display[2] += f'  =  BUSTED  =           '
                bet_display[3] += f'  ={bet_string_lost:^10}=           '
            elif nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2 and not (hand.calculate_value() == 21 and len(hand.cards) == 2): #Dealer Blackjack, Player no Blackjack
                bet_display[2] += f'  =   Lost:  =           '
                bet_display[3] += f'  ={bet_string_lost:^10}=           '
            elif hand.calculate_value() == 21 and len(hand.cards) == 2:                 #Player Blackjack
                bet_display[2] += f'  =BLACKJACK!=           '
                bet_display[3] += f'  ={bet_string_payout:^10}=           '
            elif hand.calculate_value() == nate_hand.calculate_value():                 #The Player and Dealer Pushed
                bet_display[2] += f'  =   PUSH   =           '
                bet_display[3] += f'  ={format_money(push_return_amt):^10}=           '
            elif nate_hand.calculate_value() > 21:                                      #Dealer Busted
                bet_display[2] += f'  =  Payout: =           '
                bet_display[3] += f'  ={bet_string_payout:^10}=           '
            elif hand.calculate_value() > nate_hand.calculate_value():                  #The Players total was higher:
                bet_display[2] += f'  =  Payout: =           '
                bet_display[3] += f'  ={bet_string_payout:^10}=           '
            elif hand.calculate_value() < nate_hand.calculate_value():                  #The Dealer Total was higher:
                bet_display[2] += f'  =   Lost:  =           '
                bet_display[3] += f'  ={bet_string_lost:^10}=           '
        #The dealer's cards have not been shown yet    
        else:
            if hand.calculate_value()==21 and len(hand.cards) == 2:                    #The player has blackjack, we don't know if the dealer got blackjack as well
                bet_display[2] += f'  =BLACKJACK!=           '
                bet_display[3] += f'  =          =           '
            elif hand.if_doubledown():                                              #The Player doubled down
                bet_display[2] += f'  =  Doubled =           '
                bet_display[3] += f'  ={format_money(bet):^10}=           ' 
            elif hand.calculate_value()==21:                                              #The Player has a count of 21 and should not hit anymore
                bet_display[2] += f'  = Count:21 =           '
                bet_display[3] += f'  =          =           '
            else:                                                                      #It is unknow if the player has won or lost at this point
                bet_display[2] += f'  =   Bet:   =           '
                bet_display[3] += f'  ={format_money(bet):^10}=           '
    for i in range(6):
        bet_display[i] = (side_spacing+bet_display[i]+side_spacing)
    for n in bet_display:
        lines.append(n)    
    return lines

#Function for printing information to the user in a formatted box
def text_box(*args):
    screen_width = os.get_terminal_size()[0] 
    left_space = int((screen_width/2)-28)* ' ' 
    print(f'{left_space}┌────────────────────────────────────────────────────┐')
    print(f'{left_space}│                                                    │')
    for arg in args:
        if arg!= '':
            print(f'{left_space}│{arg:^52}│')
    print(f'{left_space}│                                                    │')
    print(f'{left_space}└────────────────────────────────────────────────────┘')

#Function to call all graphics functions
def draw_entire_game(hide,location,endgame): 
    screen_width = os.get_terminal_size()[0] 
    side_spacing = ((screen_width - (25*len(all_player_hands)))//2) * ' '
    
    lines = draw_dealer_hand(hide,0,screen_width)                
    lines = draw_all_player_hands(lines,location,endgame,side_spacing) 
    lines = draw_bets(lines,endgame,side_spacing) 

    clear_terminal()
    for i in lines:
        print(i)
    if Debug:
        print(f'Nate has {len(nate_hand.cards)} cards, the value of his cards is {nate_hand.calculate_value()}')
        for i, hand in enumerate(all_player_hands):
            print(f'Your {i+1} hand has {len(hand.cards)} cards and has a total value of {hand.calculate_value()}')
#############################################################################################################################################################################################
##################################### STARTUP ACTIONS ####################################### STARTUP ACTIONS ###############################################################################
#############################################################################################################################################################################################
#General Variable Setup
player_bank = 100 #Player Starting Cash
total_bought_in_for = 100
ordinals = [' first',' second',' third',' fourth',' fifth',' sixth',' seventh',' eighth',' ninth',' tenth']
card_ranks_plural = {'A': 'Aces', 'K': 'Kings', 'Q': 'Queens', 'J': 'Jacks','10': '10\'s', '9': '9\'s', '8': '8\'s', '7': '7\'s','6': '6\'s', '5': '5\'s', '4': '4\'s', '3': '3\'s', '2': '2\'s'}
numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four',5: 'five', 6: 'six', 7: 'seven', 8: 'eight',9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen'}
highscore_run = False #For remembering if the player has already beat the dealer
most_money = 100 #For printing the player's highscore when they lose or quit
screen_width = os.get_terminal_size()[0] 
screen_height = os.get_terminal_size()[1]
playing = True

#Print Boot Screen
print('\n'*int((screen_height-14)/2))
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
print(bj_space,'                                                                          _           _  _      _        __   __')
print(bj_space,'                                                                         | |__ _  _  | \| |__ _| |_ ___  \ \ / /')
print(bj_space,'                                                                         | \'_ \ || | | .` / _` |  _/ -_)  \ V / ')
print(bj_space,'                                                                         |_.__/\_, | |_|\_\__,_|\__\___|   \_(_)  ')
print(bj_space,'                                                                               |__/   ')
time.sleep(3)
clear_terminal()

#Print Introductory Message, Give option to read rules
Debug = False
decision = yes_no_question('draw_bank_only',0,0,0,'Welcome to Nate\'s blackjack table','You just bought in for $100','Win $2000 to bankrupt Nate','Would you like to read the rules?')
#decision = 'debug'
if decision == 'debug':
    Debug = True

elif decision == 'y':
    screen_height = os.get_terminal_size()[1]
    screen_width = os.get_terminal_size()[0]
    spacing_above_instructions = ((screen_height- 40)//2)*'\n'
    clear_terminal()
    instruction_spacing = int((screen_width - 141)/2)* ' '
    while True:
        print(spacing_above_instructions)
        print(f'{instruction_spacing}┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐')
        print(f'{instruction_spacing}│ How to play Blackjack                                                                                                           │')
        print(f'{instruction_spacing}│      You will be competing against the dealer, Nate to get the value of your cards as close to 21 without going over            │')
        print(f'{instruction_spacing}│      You will be dealt two cards and then decide whether to hit (be dealt another card) or stand (receive no more cards)        │')
        print(f'{instruction_spacing}│      Face cards are worth 10, Aces can be worth 11 or 1                                                                         │')
        print(f'{instruction_spacing}│                                                                                                                                 │')
        print(f'{instruction_spacing}│ Betting                                                                                                                         │')
        print(f'{instruction_spacing}│      You will decide how much to bet per hand you play, and if you win your bet will be paid out 1:1                            │')
        print(f'{instruction_spacing}│      If you are dealt blackjack, 21 total with only 2 cards, you will be paid out 3:2                                           │')
        print(f'{instruction_spacing}│      If you and the dealer have the same total your bet will be returned to you without profit, (push)                          │')
        print(f'{instruction_spacing}│                                                                                                                                 │')
        print(f'{instruction_spacing}│ Splitting                                                                                                                       │')
        print(f'{instruction_spacing}│      If you have two cards of the same value, you can split your hand (make two hands out of your original hand)                │')
        print(f'{instruction_spacing}│      In order to split you must be able to afford another bet to create the second hand                                         │')
        print(f'{instruction_spacing}│                                                                                                                                 │')
        print(f'{instruction_spacing}│ Doubling Down                                                                                                                   │')
        print(f'{instruction_spacing}│      To double down means to double the initial amount you bet on a hand, and in exchange be dealt exactly one more card        │')
        print(f'{instruction_spacing}│      If you double down you won\'t be able to hit anymore after receiving this card                                              │')
        print(f'{instruction_spacing}│                                                                                                                                 │')
        print(f'{instruction_spacing}│ Insurance                                                                                                                       │')
        print(f'{instruction_spacing}│      If the dealer\'s faceup card is an Ace, you will be offered the chance to buy insurance                                     │')
        print(f'{instruction_spacing}│      Insurance costs half the amount you bet per hand, for everyhand you have except hands dealt blackjack                      │')
        print(f'{instruction_spacing}│      Insurance is paid out 2:1 if the dealer was dealt Blackjack                                                                │')
        print(f'{instruction_spacing}│      If you don\'t buy insurance and the dealer had blackjack, you will lose all your bets, except for any hands dealt Blackjack │')
        print(f'{instruction_spacing}│                                                                                                                                 │')
        print(f'{instruction_spacing}│ Nate\'s Casino Rules                                                                                                             │')
        print(f'{instruction_spacing}│      You can only split Aces once, and can\'t hit on split Aces, split Aces that make Blackjack are paid 1:1                     │')
        print(f'{instruction_spacing}│      If you can hit to 5 cards without busting your hand will be paid out regardless of the count                               │')
        print(f'{instruction_spacing}│      The dealer will always hit on 16, and stand on 17, including soft 17                                                       │')
        print(f'{instruction_spacing}│      There is no splitting limit, though the game will limit how many hands you can play based on your screen size              │')
        print(f'{instruction_spacing}│      For all yes/no questions you can respond with y or n to play quicker                                                       │')
        print(f'{instruction_spacing}│                                                                                                                                 │')
        print(f'{instruction_spacing}│                                                   [press enter to continue]                                                     │')
        input(f'{instruction_spacing}└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘')
        break
if Debug:
    when_double = 'c'
else:
    when_double = ask_when_to_double()
    if when_double in ['a','b','c']:
        decision = yes_no_question('draw_bank_only',0,0,0,'Would you like to keep your doubled','down card hidden until the dealer shows?')
        if decision == 'y':
            hide_double = True
        else:
            hide_double = False

#############################################################################################################################################################################################
##################################### GAMEPLAY LOOP ####################################### GAMEPLAY LOOP ###################################################################################
#############################################################################################################################################################################################
while playing:
    deck = make_deck()  
    previous_bank = player_bank
    all_player_hands = []

    #Give PLayer Option of How Many Hands to Start with
    if Debug:
        starting_hands = 5
    else:
        starting_hands = ask_how_many_starting_hands()
                  
    #Find out how much the player wants to bet
    if Debug:
        bet_per_hand = 10
    else:
        bet_per_hand = make_bet() 
    for i in range(starting_hands):
        player_bank -= bet_per_hand

    #Dealing Animation Section###########################################
    if Debug:
        nate_hand = Hand()
        nate_hand.deal_card(deck)
        nate_hand.deal_card(deck)
        for i in range(starting_hands):
            all_player_hands.append(Hand())
            all_player_hands[i].deal_card(deck)
            all_player_hands[i].deal_card(deck)

    else:
        hand_counter = starting_hands
        nate_hand = Hand()
        for i in range(hand_counter):
            all_player_hands.append(Hand())
        draw_entire_game('hide','n','not_endgame') #draw a blank board with no cards that is shown for a second
        time.sleep(.5)

        #Deal the first card to each of the player's hands
        for i in range(hand_counter):
            all_player_hands[i].deal_card(deck)
            draw_entire_game('hide','n','not_endgame')
            time.sleep(.5)
        
        #Deal the dealer's first card
        nate_hand.deal_card(deck)
        draw_entire_game('first','n','not_endgame')
        time.sleep(.5)

        #Deal the second card to each of the player's hands
        for i in range(hand_counter):
            all_player_hands[i].deal_card(deck)
            draw_entire_game('first','n','not_endgame')
            time.sleep(.5)

        #Deal Nate's second card
        nate_hand.deal_card(deck)
        draw_entire_game('second','n','not_endgame')
        time.sleep(.5)
        draw_entire_game('hide','n','not_endgame')
        time.sleep(.5)

    #Offer Player option to buy insurance if the dealer is showing an Ace
    prompted_insurance = False
    bought_insurance = False
    hands_not_dealt_blackjack = starting_hands
    for i, hand in enumerate(all_player_hands):
        if hand.calculate_value() == 21 and len(hand.cards) == 2: 
            hands_not_dealt_blackjack -= 1
    insurance_cost = .5*bet_per_hand*hands_not_dealt_blackjack

    if nate_hand.cards[0].split(' ')[0] == 'A' and player_bank >= (insurance_cost):
        prompted_insurance = True
        insurance_payout = insurance_cost * 3 #return the bet amount and two times bet amount
        decision = yes_no_question('print_entire_game','hide','n','not_endgame','Nate is showing an Ace. Do you want to','buy insurance for your hands not dealt Blackjack?',' ',f'Insurance will cost {format_money(insurance_cost)} for your hands.','Insurance pays out 2:1 if Nate is dealt Blackjack.')
        if decision == 'y':
            player_bank -= insurance_cost
            bought_insurance = True

    #Don't Give Option to Split, Double Down, or hit if they dealer was dealt blackjack
    if nate_hand.calculate_value() != 21: 

        #let the player know that the dealer was not dealt Blackjack
        if prompted_insurance:
            extra_line = ''
            if bought_insurance:
                extra_line = f'Thanks for the {format_money(insurance_cost)} bozo.'
            draw_entire_game('hide','n','not_endgame')
            print('\n')
            text_box('Nate was not dealt Blackjack.',extra_line,' ','[press enter to continue]')
            input()
        elif nate_hand.cards[0].split(' ')[0] in ['A','K','Q','J','10']: #the dealer is showing a ten value card, or player could not afford insurance
            draw_entire_game('hide','n','not_endgame')
            print('\n')
            text_box('Nate was not dealt Blackjack.',' ','[press enter to continue]')
            input()
            
        give_split_option(player_bank)
        give_double_down_option(player_bank)
        give_hit_option()
       
        #Make the dealer hit if they need to, dispay the animation for the dealing drawing
        dealer_draw = False
        for i in all_player_hands: #Check the player doesn't have all busts or all blackjacks
            if i.calculate_value()<21:
                dealer_draw = True
                break #don't need to keep checking if criteria is met once
            elif i.if_doubledown() and hide_double: #Dealer should draw if the player has a hand that doubled down to 21, but that is hidden still
                dealer_draw = True
                break #don't need to keep checking if criteria is met once
        draw_entire_game('hide','n','not_endgame') #add an animation here for the card flipping
        time.sleep(1)
        draw_entire_game('show','n','not_endgame') #add an animation here for the card flipping
        time.sleep(1)
        if dealer_draw == True:
            while nate_hand.calculate_value()<17:  #Make the Dealer draw cards
                nate_hand.deal_card(deck)
                draw_entire_game('show','n','not_endgame') 
                time.sleep(1)
        
        #If the player has a hidden double down card reveal it dramatically before the final messages are displayed
        had_doubled_hand = 0
        for i, hand in enumerate(all_player_hands):
            if hand.if_doubledown():
                had_doubled_hand = 0
        draw_entire_game('show','n','endgame')
        time.sleep(1)

    #Determine outcome of Dealer Hand
    player_all_blackjacks = all(hand.calculate_value() == 21 and len(hand.cards) == 2 for hand in all_player_hands) #return True if player has all blackjacks
    player_all_busts = all(hand.calculate_value() > 21 for hand in all_player_hands) #return True if all player hands bust
    dealer_outcome = ''
    dealer_outcome2 = ''
    if player_all_busts:
        if len(all_player_hands)==1:
            dealer_outcome = 'Your hand busted.'
        else:
            dealer_outcome = 'All of your hands busted.'
    elif nate_hand.calculate_value() > 21:
        dealer_outcome = 'Nate busted!'
    elif nate_hand.calculate_value() == 21 and len(nate_hand.cards) == 2:
        if prompted_insurance:
            if bought_insurance:
                player_bank += (insurance_payout) 
                dealer_outcome = 'Nate got Blackjack.'
                dealer_outcome2 = f'Your insurance bet paid out {format_money(insurance_cost * 2)}.'
            else:
                dealer_outcome = 'Nate got Blackjack!'
                dealer_outcome2 = 'You should have bought that insurance: Womp Womp!'
        else:
            dealer_outcome = 'Nate got Blackjack! Womp Womp'
    elif player_all_blackjacks:
        if len(all_player_hands) == 1:
            dealer_outcome = 'Nice Blackjack!'
        else:
            dealer_outcome = 'Nice Blackjacks!'
    elif nate_hand.calculate_value() <= 21:
        dealer_outcome = f'Nate got {nate_hand.calculate_value()}.'

    #Adjust player's bank
    player_bank = payout_player(player_bank)
    if player_bank > most_money:
        most_money = player_bank
    profit = player_bank - previous_bank

    #Determine outcome of Player's Hands
    if profit > 0:
        result = f'You won {format_money(profit)} this round!'
    elif profit < 0:
        result = f'You lost {format_money(abs(profit))} this round.' #abs removes the negative sign
    elif profit == 0:
        result = f'You broke even this round across your hands.'
    
    #Print results to player and prompt them to continue or not
    top_space = (29*'\n') #set height, you could make this a calculation for how many lines are printed in the draw entire game function
    if player_bank < 10:
        draw_entire_game('show','n','endgame')
        decision = yes_no_question('print_entire_game','show','n','endgame',dealer_outcome,dealer_outcome2,' ',result,' ','You can no longer afford the table minimum bet.','','Buy in for another $100?')
        if decision == 'y':
            player_bank += 100
            total_bought_in_for += 100
        elif decision == 'n':       
            playing = False
    elif player_bank >= 2000 and not highscore_run:
        go_for_highscore = yes_no_question('print_entire_game','show','n','endgame',dealer_outcome,dealer_outcome2,' ',result,' ','You Bankrupt Nate!','You are planning a trip to Spain','Would you like to keep playing for a highscore?')
        if go_for_highscore == 'n':
            playing = False
        elif go_for_highscore == 'y':
            highscore_run = True
    else:
        decision = yes_no_question('print_entire_game','show','n','endgame',dealer_outcome,dealer_outcome2,' ',result,' ','Continue playing?')
        if decision == 'n':
            clear_terminal()
            playing = False 

clear_terminal()
bought_in_total = f'You bought in for {format_money(total_bought_in_for)} total,'
game_result = f'You are walking away with {format_money(player_bank)},'
chip_total = f'Your maximum chip total was {format_money(most_money)}.'
print(top_space)
text_box(bought_in_total,game_result,chip_total,' ','Thank you for playing at Nate\'s blackjack table!')

#new content to add/improvment to existing functions
    #Add a fun things if you win the game
    #add a graphic of the dealer's shoe
    #add ability to count cards with a deck that dosn't reshuffle each time, adn that has a hsoe you can see run out
    #add side bets, like 21+3
    #Make the sequence of asking to double down, split, hit all in clockwise order
    #there is a glitch where sometimes it doesn't ask you if you want to keep playing??
    #don't ask to double down if you split aces and make a doubleable hand
    #there may be a glitch about doubling down when multiple hands are duobleable and you say double down to the first one it doubels down the other one?
    #add ability to go back, for example you choose 5 hands, then when you see the betting screen you want to change
    #the player should type in their action every hand, instead of being prompted when they would like to double down. 
