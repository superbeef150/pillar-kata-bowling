import unittest
from game import Game

class BowlingGameTest(unittest.TestCase):
    
    def setUp(self):
        self.g = Game()
        
    def rollMany(self, n, pins):
        for x in xrange(1, n+1):
            self.g.roll(pins)
    
    def test_game_all_gutterballs(self):
        self.setUp()
        print "test_game_all_gutterballs"
        self.rollMany(20, 0)
        self.assertEqual(0, self.g.score())
        
    def test_game_all_1s(self):
        self.setUp()
        print "test_game_all_1s"
        self.rollMany(20, 1)
        self.assertEqual(20, self.g.score())
        
    def test_one_spare(self):
        self.setUp()
        print "test_one_spare"
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17, 0) #17 gutterballs ouch lol
        self.assertEqual(16, self.g.score())
        
    def test_one_strike(self):
        self.setUp()
        print "test_one_strike"
        self.rollStrike()
        self.g.roll(3)
        self.g.roll(4)
        self.rollMany(16, 0) #16 gutterballs ouch lol
        self.assertEqual(24, self.g.score())
        
    def test_perfect_game(self):
        self.setUp()
        print "test_perfect_game"
        self.rollMany(12, 10)
        self.assertEqual(300, self.g.score())
        
    
    def rollStrike(self):
        self.g.roll(10)
    
    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5)

if __name__ == '__main__':
    unittest.main()
