from CartesianCoordinate import CartesianCoordinate
import re

class Move():
    def __init__(self, pieceType, sourceFile, sourceRank, destination, isCapture, isCheck, isCheckmate):
        self.pieceType = pieceType
        self.sourceFile = sourceFile
        self.sourceRank = sourceRank
        self.destination = destination
        self.isCapture = isCapture 
        self.isCheck = isCheck
        self.isCheckmate = isCheckmate

    def fromString(string):
        pieceType = string[0] if len(string) >= 1 and (string[0] in "RNBQK") else None
        sourceFile = None
        sourceRank = None
        destination = None
        isCapture = "x" in string
        isCheck = "+" in string
        isCheckmate = "#" in string
        
        if re.fullmatch("[RNBQK]*x*\w\d[+#]*", string):         #Parse Moves like Ke2, Be4+, Be4#
            destination = string.replace("x", "")[1:3]
        elif re.fullmatch("[RNBQK]*\wx*\w\d[+#]*", string):     #Parse moves like Rae4, etc
            sourceFile = string[1]
            destination = string.replace("x", "")[2:4]
        elif re.fullmatch("[RNBQK]*\dx*\w\d[+#]*", string):     #Parse moves like R1e4, etc
            sourceRank = string[1]
            destination = string.replace("x", "")[2:4]
        elif re.fullmatch("[RNBQK]*\w\dx*\w\d[+#]*", string):   #Parse moves like Qa1e4, etc
            sourceFile = string[1]
            sourceRank = string[2]
            destination = string.replace("x", "")[3:5]
        elif re.fullmatch("\w\d[+#]*", string):         #Parse moves like e4, 
            destination = string[0:2]
        elif re.fullmatch("\wx\w\d[+#]", string):       #Parse moves like dxe4
            sourceFile = string[0]
            destination = string[2:4]
        elif re.fullmatch("o-o-o"):
            raise MoveParsingError("Long Castling is not implemented yet.")
        elif re.fullmatch("o-o"):
            raise MoveParsingError("Castling is not implemented yet.")
        else:
            raise MoveParsingError("Move does not match any valid regex expression", string)

        return Move(pieceType, sourceFile, sourceRank, destination, isCapture, isCheck, isCheckmate)

class MoveParsingError(ValueError):
    def __init__(self, message, moveString):
        super.__init__("The move %s cannot be parsed:\n\t%s" %(moveString, message))