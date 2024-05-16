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

clear_terminal()

heart = '\u2665'
print('┌─────────┐')
print('│{}{}       │'.format(8,heart))
print('│         │')
print('│    {}    │'.format(heart))
print('│         │')
print('│       {}{}│'.format(8,heart))
print('└─────────┘')

print('╭──────────╮')
print('│{}         │'.format(8))
print('│{}         │'.format(heart))
print('│          │')
print('│    {}     │'.format(heart))
print('│          │')
print('│         {}│'.format(heart))
print('│         {}│'.format(8))
print('╰──────────╯')







'8 of hearts'
print('╭──────────╮')
print('│{}         │'.format(8))
print('│{} {}    {}  │'.format(heart,heart,heart))
print('│     {}    │'.format(heart))
print('│  {}    {}  │'.format(heart,heart))
print('│     {}    │'.format(heart))
print('│  {}    {} {}│'.format(heart,heart,heart))
print('│         {}│'.format(8))
print('╰──────────╯')

print('')
print('')
print('')
print('')
'9 of hearts'
print('╭──────────╮')
print('│{}         │'.format(9))
print('│{} {}    {}  │'.format(heart,heart,heart))
print('│  {}    {}  │'.format(heart,heart))
print('│     {}    │'.format(heart))
print('│  {}    {}  │'.format(heart,heart))
print('│  {}    {} {}│'.format(heart,heart,heart))
print('│         {}│'.format(9))
print('╰──────────╯')
'10 of hearts'
print('╭──────────╮')
print('│{}        │'.format(10))
print('│{} {}    {}  │'.format(heart,heart,heart))
print('│  {}    {}  │'.format(heart,heart))
print('│  {}    {}  │'.format(heart,heart))
print('│  {}    {}  │'.format(heart,heart))
print('│  {}    {} {}│'.format(heart,heart,heart))
print('│        {}│'.format(10))
print('╰──────────╯')
'Jack of Hearts'
print('╭──────────╮')
print('│J┌──────┐ │')
print('│{}│    ww│ │'.format(heart,heart))
print('│ │    {)│ │')
print('│ │    # │ │')
print('│ │    # │ │')
print('│ │    # │{}│'.format(heart,heart))
print('│ └──────┘J│')
print('╰──────────╯')
'Queen of Hearts'
print('╭──────────╮')
print('│Q┌──────┐ │')
print('│{}│    ww│ │'.format(heart,heart))
print('│ │    {(│ │')
print('│ │    ##│ │')
print('│ │   ###│ │')
print('│ │   ###│{}│'.format(heart,heart))
print('│ └──────┘Q│')
print('╰──────────╯')
'King of Hearts'
print('╭──────────╮')
print('│K┌──────┐ │')
print('│{}│    ww│ │'.format(heart,heart))
print('│ │    {)│ │')
print('│ │    ##│ │')
print('│ │   ###│ │')
print('│ │   ###│{}│'.format(heart,heart))
print('│ └──────┘K│')
print('╰──────────╯')
'Ace of Hearts'
print('╭──────────╮')
print('│A         │')
print('│{}   _ _   │'.format(heart,heart))
print('│   ( V )  │')
print('│    \ /   │')
print('│     V    │')
print('│         {}│'.format(heart,heart))
print('│         A│')
print('╰──────────╯')
'''

          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
ejm98    |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|

                              
//        ⎹          ╱               ⟋            ⎽⎼⎻⎺                                       
//        |         ╱              ⟋           ⎽⎼⎻⎺                                          
//        ⎸        ╱             ⟋          ⎽⎼⎻⎺                                             
//       ⎹        ╱            ⟋         ⎽⎼⎻⎺       _-‾                                      
//       |       ╱           ⟋        ⎽⎼⎻⎺       _-‾               __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺ 
//       ⎸      ╱          ⟋       ⎽⎼⎻⎺       _-‾           __---‾‾         _⎽⎽⎼⎼⎻⎻⎺⎺‾       
//      ⎹      ╱         ⟋      ⎽⎼⎻⎺       _-‾       __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                
//      |     ╱        ⟋     ⎽⎼⎻⎺       _-‾   __---‾‾       _⎽⎽⎼⎼⎻⎻⎺⎺‾                       
//      ⎸    ╱       ⟋    ⎽⎼⎻⎺                                                               
//          ╳      ⤫                                                                         
//      ⎸    ╲       ⟍    ⎺⎻⎼⎽          ‾-_   ‾‾---__       ‾⎺⎺⎻⎻⎼⎼⎽⎽_                       
//      |     ╲        ⟍     ⎺⎻⎼⎽          ‾-_       ‾‾---__        ‾⎺⎺⎻⎻⎼⎼⎽⎽_               
//      ⎹      ╲         ⟍      ⎺⎻⎼⎽          ‾-_           ‾‾---__        ‾⎺⎺⎻⎻⎼⎼⎽⎽_        
//       ⎸      ╲          ⟍       ⎺⎻⎼⎽          ‾-_                ‾‾---__       ‾⎺⎺⎻⎻⎼⎼⎽⎽_ 
//       |       ╲           ⟍        ⎺⎻⎼⎽          ‾-_                                      
//       ⎹        ╲            ⟍         ⎺⎻⎼⎽                                                
//        ⎸        ╲             ⟍          ⎺⎻⎼⎽                                             
//        |         ╲              ⟍           ⎺⎻⎼⎽ 
//        ⎹          ╲               ⟍         

           .....
        _d^^^^^^^^^b_
     .d''           ``b.
   .p'     Objects     `q.
  .d'   in mirror may   `b.
 .d'   be less virtual   `b.
 ::   than they appear.   ::
 ::  ...................  ::
 ::                       ::
 `p.  johnca@netcom.com  .q'
  `p.   John Abbe aka   .q'
   `b.     Rademir     .d'
     `q..          ..p'
        ^q........p^

            

        _.,,,,,,,,,._
     .d''           ``b.
   .p'     Objects     `q.
 .d'   in mirror may    `b.
 .d'   be less virtual   `b.
 ::   than they appear.   ::
 `p.  johnca@netcom.com  .q'
  `p.   John Abbe aka   .q'
   `b.     Rademir     .d'
     `q..            ..,'
        '',,,,,,,,,,''


        . -- ~~~ -- .
    .-~               ~-.
   /                     \
  /                       \
 |                         |
 |                         |
 |                         |
  \                       /
   \                     /
    `-.               .-'
        ~- . ___ . -~


         , - ~~ - ,
     , '            ' ,
   ,                    ,
  ,                      ,
 ,                        ,
 ,                        ,
 ,                        ,
  ,                      ,
   ,                    ,
     ,                , 
       ' - , __ , - '

        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *        *        *        *
        *  *              *  *


        /  /              /  /
     /        /        /        /
    /          /      /          /
    /          /      /          /
     /        /        /        /
        /  /              /  /


        o  o              o  o
     o        o        o        o
    o          o      o          o
    o          o      o          o
     o        o        o        o
        o  o              o  o


        =  =              =  =
     =        =        =        =
    =          =      =          =
    =          =      =          =
     =        =        =        =
        =  =              =  =



        x  x              x  x
     x        x        x        x
    x          x      x          x
    x          x      x          x
     x        x        x        x
        x  x              x  x



                                              _  _
             =  =                          =        =
          =        =                     =            =
         =          =                   =              =
         =          =                   =              =
          =        =                     =            =
             =  =                          =        =
                                              ~  ~


           %%%    %%%
      %%%              %%%

  %%%                      %%%

 %%%                         %%%

 %%%                         %%%

 %%%                        %%%

    %%%                  %%%

          %%%     %%%

                                                                                                                                                            
                                                                                                                                                  
                                                                          ▓▓▓▓▓▓                                                                  
                                                                  ▒▒░░            ░░▒▒                                                            
                                                              ▒▒                        ▒▒                                                        
                                                            ▒▒                            ▒▒                                                      
                                                          ▒▒                                ▓▓                                                    
                                                        ░░                                    ▒▒                                                  
                                                        ▒▒                                    ░░                                                  
                                                                                                ▒▒                                                
                                                      ▒▒                                        ░░                                                
                                                      ▒▒                                                                                          
                                                      ░░                                                                          
                                                      ░░                                                                               
                                                      ▒▒                                        ░░░                                    
                                                      ██                                        ▓▓                                        
                                                                                                ▒▒                                          
                                                        ▓▓                                    ▓▓                                                  
                                                          ▓▓                                ░░                                             
                                                          ▓▓▒▒                              ▓▓                                                    
                                                             ▒▒                        ░░░░░        
                                                                ▒▒░░                  ▒▒      
                                                                      ▒▒▒▒░░  ▒▒▒▒▒▒           
                                                                                                                 
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  


'''