from position import *
from cartesian_coordinate import CartesianCoordinate as Coordinate
class PositionTestSuite():
    def getTests():
        return [
            {"runnable": PositionTestSuite.test1, "name": "Chess Starting Position Initialized Correctly"}
        ]
    def test1():
        pos = Position.fromStartingPosition()        
        assert(pos.boardState != None)
        assert(pos.gameStatus == GameStatus.WHITE_TO_MOVE)
        assert(pos.castlingRights == CastlingRights.fromAllTrue())
        assert(pos.enPassantPawn == Coordinate.fromNonExistent())
        assert(pos.halfClock == 0)
        assert(pos.fullClock == 1)
        return True
