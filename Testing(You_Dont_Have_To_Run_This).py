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
'''
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


         , - ~ ~ - ,
     , '             ' ,
   ,                     ,
  ,                       ,
 ,                         ,
 ,                         ,
 ,                         ,
  ,                       ,
   ,                      ,
     ,                 , '
       ' - , _ _ , - '

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