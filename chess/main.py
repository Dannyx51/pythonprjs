from board import *
import os
import time

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

# selected = False
while True:
    while True:
        # first set to select a piece to move
        try:
            cb.print(cb.bBG)
            pos = input("Choose a piece: ")
            x = ord(pos[0].lower()) - 97
            y = 8 - int(pos[1])
            cb.highlight(x,y)
            clear()
            cb.print(cb.bH)
            break
        except Exception as e:
            print("Error: {0}".format(e))

        # second set to select a place to move it to
        

    time.sleep(1)
    clear()