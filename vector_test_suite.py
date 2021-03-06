from verifier.vector import Vector


class VectorTestSuite:
    @staticmethod
    def getTests():
        return [
            {"runnable": VectorTestSuite.vecInit, "name": "Vectors can be instantiated"},
            {"runnable": VectorTestSuite.vecInitAN, "name": "Vectors can be instantiated from AN"},
            {"runnable": VectorTestSuite.vecAcc, "name": "A Vector's x and y members can be accessed"},
            {"runnable": VectorTestSuite.vecEq, "name": "Vectors can be equated"},
            {"runnable": VectorTestSuite.anValid, "name": "Algebreic Notation has correct values"},
            {"runnable": VectorTestSuite.vecAdd, "name": "Addition of Vectors"},
            {"runnable": VectorTestSuite.vecSub, "name": "Subtraction of Vectors"},
            {"runnable": VectorTestSuite.vecToAN, "name": "Translation to Algebreic Notation"},
            {"runnable": VectorTestSuite.vecIn, "name": "Vector in List"},
        ]

    @staticmethod
    def vecInit():
        assert(Vector(0,0) != None)
        assert(Vector(1,0) != None)
        assert(Vector(0,1) != None)
        assert(Vector(-1,0) != None)
        assert(Vector(0,-1) != None)
        assert(Vector(-1,-1) != None)
        assert(Vector(1,1) != None)
        return True
    
    @staticmethod
    def vecInitAN():
        assert (Vector.fromAN("a1") != None)
        assert (Vector.fromAN("h8") != None)
        assert (Vector.fromAN("h2") != None)
        assert (Vector.fromAN("b4") != None)
        return True
    
    @staticmethod
    def vecAcc():
        assert(Vector(1,2).x == 1)
        assert(Vector(1,2).y == 2)
        return True

    @staticmethod
    def vecEq():
        assert(Vector(0,0) == Vector(0,0))
        assert(Vector(1,0) == Vector(1,0))
        assert(Vector(0,2) == Vector(0,2))
        assert(Vector(5,-4) == Vector(5,-4))
        assert(Vector(0,0) != Vector(0,1))
        assert(Vector(1,0) != Vector(1,1))
        assert(Vector(0,2) != Vector(1,2))
        assert(Vector(5,-4) != Vector(5,-3))
        return True
    
    @staticmethod
    def anValid():
        assert(Vector.fromAN("a1") == Vector(0,0))
        assert(Vector.fromAN("b1") == Vector(1,0))
        assert(Vector.fromAN("a2") == Vector(0,1))
        assert(Vector.fromAN("h8") == Vector(7,7))
        assert(Vector.fromAN("a1") != Vector(1,0))
        assert(Vector.fromAN("b1") != Vector(1,1))
        assert(Vector.fromAN("a2") != Vector(1,1))
        assert(Vector.fromAN("h8") != Vector(7,8))
        return True
    
    @staticmethod
    def vecAdd():
        assert(Vector(0,0) + Vector(0,0) == Vector(0,0))
        assert(Vector(1,0) + Vector(0,0) == Vector(1,0))
        assert(Vector(0,1) + Vector(0,0) == Vector(0,1))
        assert(Vector(1,0) + Vector(0,1) == Vector(1,1))
        assert(Vector(3,1) + Vector(-1,-2) == Vector(2,-1))
        assert(Vector(0,0) + Vector(0,0) == Vector.fromAN("a1"))
        assert(Vector.fromAN("a1") + Vector(0,0) == Vector.fromAN("a1"))
        assert(Vector.fromAN("a1") + Vector.fromAN("a1") == Vector.fromAN("a1"))
        assert(Vector.fromAN("b3") + Vector(1, -1) == Vector.fromAN("c2"))
        assert(Vector.fromAN("h8") + Vector(-2,-2) == Vector.fromAN("f6"))
        assert(Vector.fromAN("b2") + Vector.fromAN("b2") == Vector(2,2))
        assert(
            sum([
                Vector.fromAN("b2"),
                Vector.fromAN("b2"),
                Vector.fromAN("b2")
            ]) == Vector.fromAN("d4"))
        return True
    
    @staticmethod
    def vecSub():
        assert(Vector(0,0) - Vector(0,0) == Vector(0,0))
        assert(Vector(4,0) - Vector(1,0) == Vector(3,0))
        assert(Vector(0,4) - Vector(0,1) == Vector(0,3))
        assert(Vector(4,4) - Vector(1,1) == Vector(3,3))
        assert(Vector(0,0) - Vector(1,2) == Vector(-1,-2))
        assert(Vector.fromAN("a1") - Vector.fromAN("a1") == Vector.fromAN("a1"))
        assert(Vector.fromAN("c2") - Vector.fromAN("b3") == Vector(1,-1))
        return True
    
    @staticmethod
    def vecToAN():
        assert(Vector(0,0).toAN() == "a1"), Vector(0,0).toAN()
        assert(Vector(1,0).toAN() == "b1"), Vector(1,0).toAN()
        assert(Vector(0,1).toAN() == "a2"), Vector(0,1).toAN()
        assert(Vector(7,0).toAN() == "h1"), Vector(7,0).toAN()
        assert(Vector(0,7).toAN() == "a8"), Vector(0,7).toAN()
        assert(Vector(4,4).toAN() == "e5"), Vector(4,4).toAN()
        return True
        
    @staticmethod
    def vecIn():
        assert(Vector(0,0) in [Vector(0,0)])
        assert(Vector(0,0) in [Vector.fromAN("a1")])
        assert(Vector(0,0) in [Vector(1,0), Vector(0,1), Vector(0,0)])
        return True
