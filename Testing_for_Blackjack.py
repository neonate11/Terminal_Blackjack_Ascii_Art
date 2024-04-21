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
    for i in range(8):
        lines.append('')
    lines[0] += '           '
    lines[1] += '┌─────────┐'
    lines[2] += '│ ▓▓▓▓▓▓▓ │'
    lines[3] += '│ ▓▓▓▓▓▓▓ │'
    lines[4] += '│ ▓▓▓▓▓▓▓ │'
    lines[5] += '│ ▓▓▓▓▓▓▓ │'
    lines[6] += '│ ▓▓▓▓▓▓▓ │'
    lines[7] += '└─────────┘'
    for i in lines:
        print(i)
    time.sleep(1)
    clear_terminal()
    time.sleep(1)
    lines= []
    for i in range(8):
        lines.append('')
    lines[0] += '      _⎽⎽⎼┐'
    lines[1] += '┌⎻⎻⎺‾  ▓▓ │'
    lines[2] += '│ ▓▓▓▓▓▓▓ │'     
    lines[3] += '│ ▓▓▓▓▓▓▓ │'    
    lines[4] += '│ ▓▓▓▓▓▓▓ │'
    lines[5] += '│ ▓▓▓▓▓▓▓ │'  
    lines[6] += '│ ▓▓  _⎽⎽⎼┘'
    lines[7] += '└⎻⎻⎺‾'
    for i in lines:
        print(i)

draw_dealer_hand()

'''         
//        ⎸        ╱             ⟋          ⎽⎼⎻⎺                                             
//       ⎹        ╱            ⟋         ⎽⎼⎻⎺       _-‾                                      
//       |       ╱           ⟋        ⎽⎼⎻⎺       _-‾               __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺ 
//       ⎸      ╱          ⟋       ⎽⎼⎻⎺       _-‾           __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺‾       
//      ⎹      ╱         ⟋      ⎽⎼⎻⎺       _-‾       __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                
//      |     ╱        ⟋     ⎽⎼⎻⎺       _-‾   __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                       
//      ⎸    ╱       ⟋    ⎽⎼⎻⎺                                                              


'''