import random
import os
import platform
import time
screen_width = os.get_terminal_size()[0] 
screen_height = os.get_terminal_size()[1]

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def make_a_firework():
    left_spacing = (random.randint(0,screen_width-1 ))*' ' #random horizontal position for firework to start in
    spaces_above_firework = os.get_terminal_size()[1]
    for i in range(10):
        printing_list = []
        for x in range((spaces_above_firework-1)//2):
            printing_list.append('\n')
        printing_list.append(left_spacing+'|')
        clear_terminal()
        for n in printing_list:
            print(n)
        time.sleep(.3)
        spaces_above_firework-=1

make_a_firework()
clear_terminal()
make_a_firework()




