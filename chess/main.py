from board import *
import os
import time

clear = lambda: os.system("clear")
x = Board()

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

x.print(x.bBG)

# selected = False
# while True:
#     if selected:
#         x.print(x.bBG)
#     else:
#         x.print(x.bH)
    
#     pos = input("Choose a piece: ")
#     time.sleep(0.5)
#     clear()

#     selected = x.highlight(pos)