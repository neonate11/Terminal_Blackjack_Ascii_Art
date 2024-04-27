import os #For the ability to clear terminal on windows or linux
import platform #For the ability to check the OS
import time

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
clear_terminal() #Try and Get Screen blank asap

def draw_dealer_hand(): 
    lines= []
    for i in range(12):
        lines.append('')
    lines[0] += '           '
    lines[1] += '           '
    lines[2] += '           '
    lines[3] += '           '
    lines[4] += '           '
    lines[5] += '┌─────────┐'
    lines[6] += '│ ▓▓▓▓▓▓▓ │'
    lines[7] += '│ ▓▓▓▓▓▓▓ │'
    lines[8] += '│ ▓▓▓▓▓▓▓ │'
    lines[9] += '│ ▓▓▓▓▓▓▓ │'
    lines[10]+= '│ ▓▓▓▓▓▓▓ │'
    lines[11]+= '└─────────┘'

    lines[0]  +='              '
    lines[1]  +='              '
    lines[2]  +='              '
    lines[3]  +='              '
    lines[4]  +='              '
    lines[5]  +='              '
    lines[6]  +='              '   
    lines[7]  +='              '
    lines[8]  +='              '         
    lines[9]  +='              '           
    lines[10] +='              '                  
    lines[11] +='              '   

    lines[0]  +='              '
    lines[1]  +='              '
    lines[2]  +='              '
    lines[3]  +='     ⟋ ││││││││││' 
    lines[4]  +='   ⟋   ││││││││││' 
    lines[5]  +=' ⟋     ││││││││││' 
    lines[6]  +='│      ││││││││││' 
    lines[7]  +='│      ││││││││││'      
    lines[8]  +='│      ││││││││││'           
    lines[9]  +='│    ⟋⟋⟋⟋⟋⟋⟋⟋'             
    lines[10] +='│  ⟋⟋⟋⟋⟋⟋⟋⟋'                   
    lines[11] +='│⟋⟋⟋⟋⟋⟋⟋⟋'   
    for i in lines:
        print(i)

draw_dealer_hand()
#f string tricks:
n = 1000
print(f'{n:,}')
word = "test"
print(f'|{word:^20}|') #can also fill with another symbol I don't think I need that
decimal_number = 34544425.509
print(f'{decimal_number:,.2f}')

'''         
//        ⎸        ╱             ⟋          ⎽⎼⎻⎺                                             
//       ⎹        ╱            ⟋         ⎽⎼⎻⎺       _-‾                                      
//       |       ╱           ⟋        ⎽⎼⎻⎺       _-‾               __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺ 
//       ⎸      ╱          ⟋       ⎽⎼⎻⎺       _-‾           __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺‾       
//      ⎹      ╱         ⟋      ⎽⎼⎻⎺       _-‾       __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                
//      |     ╱        ⟋     ⎽⎼⎻⎺       _-‾   __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                       
//      ⎸    ╱       ⟋    ⎽⎼⎻⎺                                                              

    lines[0] += '     __⎽⎽⎼┐┐┐┐┐┐'
    lines[1] += '┌⎻⎻⎺‾     ││││││'
    lines[2] += '│         ││││││'     
    lines[3] += '│         ││││││'    
    lines[4] += '│         ││││││'
    lines[5] += '│         │  │  │  │ 
    lines[6] += '│    __⎽⎽⎼┘⎽⎼┘⎽⎼┘⎽⎼┘⎽⎼┘⎽⎼┘⎽⎼┘⎽⎼┘
    lines[7] += '└⎻⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾⎻⎺‾'
    lines[0] += '     __⎽⎽⎼┐┐┐┐┐┐'
'''
def format_money(number_to_format): #This function will format the player bank or amount bet per hand with commas, and round to 2 decimals if necessary
    string = str(number_to_format)
    if '.' in string:
        parts = string.split('.')
        if not all(char == '0' for char in parts[1]): #only if there is a decimal number thats not all zeroes will it print the decimal number
            return f'${number_to_format:,.2f}'
        else:
            return f'${number_to_format:,.0f}'
    else:
        return f'${number_to_format:,.0f}'
    
print(format_money(25.00))