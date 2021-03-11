from piece import *

class Board:
    def __init__(self):
        self.board = self.resetBoard()
        self.bg = self.resetHighlight()

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

    def print(self):
        print('\x1b[%sm %s \x1b[0m' % ("7;30;42","   A  B  C  D  E  F  G  H"))
    
        for y in range(len(self.board)):    
            print('\x1b[%sm %s \x1b[0m' % ("7;30;42",str(8 - y)), end = "")
            for x in range(len(self.board[y])):
                nl = ""
                if x == 7:
                    nl = "\n"
                format = '1;' + self.board[y][x].fg + ";" + self.bg[y][x]
                print('\x1b[%sm %s \x1b[0m' % (format,self.board[y][x].name), end = nl)
        print("")

    def mToXY(self,m):
        if len(m) != 2:
            raise throw("Move Length != 2!")
        else:
            x,y = 0,0
            try:
                x = ord(m[0].lower()) - 97
                y = 8 - int(m[1])
            except Exception as e:
                print(e)
            finally:
                return x,y

    def move(self,move,team):
        pType, pre, post = move[0].upper(), move[1:3], move[3:]
        
        if team:team = "black"
        else:team = "white"

        fx,fy = self.mToXY(pre) 
        tx,ty = self.mToXY(post)
        if any(i > 7 for i in [fx,fy,tx,ty]):
            raise throw("You are moving to a place outside of the board.")

        chosen = self.board[fy][fx]
        toPos = self.board[ty][tx]
        self.moveException(chosen,toPos,pType,team)
        captured = ""
        if toPos.name != " ":
            captured = toPos.name

        valid = False
        if pType == "N":
            if any([tx == fx + 2, tx == fx - 2]):
                valid = any([ty == fy - 1,ty == fy + 1])
            elif any([ty == fy + 2, ty == fy - 2]):
                valid = any([tx == fx - 1,tx  == fx + 1])

            # print([fx,fy],[tx,ty])

            if valid:
                self.board[ty][tx] = chosen
                self.board[fy][fx] = piece(" ", " ")
                
                if captured != "":
                    print(f"Your knight moved to {post} capturing a {captured}")
                else:
                    print(f"Your knight moved to {post}.")
            else:
                raise throw("Your knight can't move there.")

        elif pType == "P":
            if chosen.team == "white" and fx == 6:
                if ty == fy - 1 or fy - 2:
                    pass
        
        
        
        # raise throw("ruh roh")
        
    def moveException(self,chosen,toPos,pType,team):
        if chosen.name != pType:
            raise throw(f"There is no {pType} at that position.")
        if chosen.team != team:
            raise throw("That is not your piece.")
        if toPos.team == team:
            raise throw("You can't take your own piece.")

class throw(Exception):
    pass