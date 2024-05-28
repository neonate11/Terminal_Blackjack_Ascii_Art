#Function to draw all player hands
def draw_all_player_hands(lines,location,endgame,side_spacing):
    player_cards = [''] * 15
    cursor_and_spacing = [''] * 15
    final_formatting = [''] * 15
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
        for i in range(15):
            player_cards[i] = '                       ' #this is a blank printed for dealing purposes (before a hand has any cards)
        if len(hand.cards) >= 1:
            player_cards[8]='┌─────────┐            '
            player_cards[9]='│{}      │            '.format(left_edge_data[0])
            player_cards[10]='│         │            '
            player_cards[11]='│    {}    │            '.format(suits[0])
            player_cards[12]='│         │            '
            player_cards[13]='│      {}│            '.format(right_edge_data[0])
            player_cards[14]='└─────────┘            '
        if len(hand.cards) >= 2 and hand.check_if_split_aces():
            player_cards[6]  = '    ┌─────────────┐    '
            player_cards[7]  = '    │          {}│    '.format(right_edge_data[1])
            player_cards[8]  = '┌───│      {}      │    '.format(suits[1])
            player_cards[9]  = '│{} │{}          │    '.format(covered_data[0],left_edge_data[1])
            player_cards[10]  = '│   └─────────────┘    '
        if len(hand.cards) >= 2 and not hand.check_if_split_aces():
            player_cards[6]  = '   ┌─────────┐         '
            player_cards[7]  = '   │{}      │         '.format(left_edge_data[1])
            player_cards[8]  = '┌──│         │         '
            player_cards[9]  = '│{}│    {}    │         '.format(covered_data[0],suits[1])
            player_cards[10] = '│  │         │         '
            player_cards[11] = '│  │      {}│         '.format(right_edge_data[1])
            player_cards[12] = '│  └─────────┘         '
        if hand.if_doubledown() and (endgame == 'endgame' or not hide_double):
            player_cards[4]  = '       ┌─────────────┐ '
            player_cards[5]  = '       │          {}│ '.format(right_edge_data[2])
            player_cards[6]  = '   ┌───│      {}      │ '.format(suits[2])
            player_cards[7]  = '   │{} │{}          │ '.format(covered_data[1],left_edge_data[2])
            player_cards[8]  = '┌──│   └─────────────┘ '
        elif hand.if_doubledown() and endgame == 'not_endgame':
            player_cards[4]  = '       ┌─────────────┐ '
            player_cards[5]  = '       │ ▓▓▓▓▓▓▓▓▓▓▓ │ '
            player_cards[6]  = '   ┌───│ ▓▓▓▓▓▓▓▓▓▓▓ │ '
            player_cards[7]  = '   │{} │ ▓▓▓▓▓▓▓▓▓▓▓ │ '.format(covered_data[1])
            player_cards[8]  = '┌──│   └─────────────┘ '
        elif not hand.if_doubledown():
            if len(hand.cards) >= 3:
                player_cards[4]  = '      ┌─────────┐      '
                player_cards[5]  = '      │{}      │      '.format(left_edge_data[2])
                player_cards[6]  = '   ┌──│         │      '
                player_cards[7]  = '   │{}│    {}    │      '.format(covered_data[1],suits[2])
                player_cards[8]  = '┌──│  │         │      '
                player_cards[9]  = '│{}│  │      {}│      '.format(covered_data[0],right_edge_data[2])
                player_cards[10] = '│  │  └─────────┘      '
            if len(hand.cards) >= 4:
                player_cards[2]  = '         ┌─────────┐   '
                player_cards[3]  = '         │{}      │   '.format(left_edge_data[3])
                player_cards[4]  = '      ┌──│         │   '
                player_cards[5]  = '      │{}│    {}    │   '.format(covered_data[2],suits[3])
                player_cards[6] = '   ┌──│  │         │   '
                player_cards[7] = '   │{}│  │      {}│   '.format(covered_data[1],right_edge_data[3])
                player_cards[8] = '┌──│  │  └─────────┘   '
            if len(hand.cards) >= 5:
                player_cards[0]  = '            ┌─────────┐'
                player_cards[1]  = '            │{}      │'.format(left_edge_data[4])
                player_cards[2]  = '         ┌──│         │'
                player_cards[3]  = '         │{}│    {}    │'.format(covered_data[3],suits[4])
                player_cards[4] = '      ┌──│  │         │'
                player_cards[5] = '      │{}│  │      {}│'.format(covered_data[2],right_edge_data[4])
                player_cards[6] = '   ┌──│  │  └─────────┘'

        for i in range(0,15): #Add the spacing for these lines
            cursor_and_spacing[i]= '  '
        if location == (len(all_player_hands) -1)-z:      #if we are referring to this hand currently add the cursor (this part also adds the spacing between hands -2 to account for the cursor)
            cursor_and_spacing[10]= '➤ ' #Add the cursor
            cursor_and_spacing[11]= '➤ ' #Add the cursor
            cursor_and_spacing[12]= '➤ ' #Add the cursor
        for n in range(15):
            final_formatting[n]+= (cursor_and_spacing[n]+player_cards[n])

    for i in range(15):
        final_formatting[i] = (side_spacing+final_formatting[i]+side_spacing)
    lines.extend(final_formatting)
    return lines