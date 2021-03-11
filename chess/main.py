from board import *
import os
import time
from math import *


clear = lambda: os.system("CLS")
cb = Board()

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

# print_format_table()

# black on black 
# format = '7;30;41'

# white on white 
# format = '7;37;46'

# highlight color
# format = '7;33;[piece color]'

selected = False
player = 0
while True:
    while True:
        # first set to select a piece to move
        try:
            cb.print()
            pos = input("Make a move: ")
            clear()
            print()
            cb.move(pos,player)
            if player == 0:
                player = 1
            else:
                player = 0
            
            time.sleep(1.5)
            clear()
        except Exception as e:
            print(f"Error: {e}")