from piece import *

class Board:
    def __init__(self):
        self.board = self.resetBoard()
        self.bBG = self.resetHighlight()
        self.bH = self.resetHighlight()


    def resetHighlight(self):
        l = [['' for i in range(8)] for i in range(8)]
        for i in range(8):
            for x in range(8):
                if i % 2 == 0:
                    if x % 2 == 0:
                        l[i][x] = '47'
                    else:
                        l[i][x] = '40'
                else:
                    if x % 2 == 0:
                        l[i][x] = '40'
                    else:
                        l[i][x] = '47'
        return l

    def resetBoard(self):
        #create an 8x8 grid
        l = [[piece(" "," ")  for i in range(8)] for i in range(8)]
        #insert pawns
        for i in range(len(l[1])):
            l[1][i] = piece("P","black")
            l[6][i] = piece("P","white")
        #insert backranks
        l[0] = [piece("R","black"), piece("N","black"),
                piece("B","black"), piece("Q","black"),
                piece("K","black"), piece("B","black"),
                piece("N","black"), piece("R","black")]

        l[7] = [piece("R","white"), piece("N","white"),
                piece("B","white"), piece("Q","white"),
                piece("K","white"), piece("B","white"),
                piece("N","white"), piece("R","white")]

        return l

    def print(self, bg):
        print('\x1b[%sm %s \x1b[0m' % ("7;30;42","   A  B  C  D  E  F  G  H"))
    
        for y in range(len(self.board)):    
            print('\x1b[%sm %s \x1b[0m' % ("7;30;42",str(8 - y)), end = "")
            for x in range(len(self.board[y])):
                nl = ""
                if x == 7:
                    nl = "\n"
                format = '1;' + self.board[y][x].fg + ";" + bg[y][x]
                print('\x1b[%sm %s \x1b[0m' % (format,self.board[y][x].name), end = nl)
        print("")

    def highlight(self, x,y):
        if(self.board[y][x].name != " "):
            item = self.board[y][x]
            if item.name == "P":
                if item.team == "white" and y == 6:
                    self.bH[y][x] = '42'
                    self.bH[y-1][x] = '43'