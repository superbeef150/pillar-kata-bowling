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
        self.rollMany(20, 0)
        self.assertEqual(0, self.g.score())
        
    def test_game_all_1s(self):
        self.setUp()
        self.rollMany(20, 1)
        self.assertEqual(20, self.g.score())
        
    def test_one_spare(self):
        self.setUp()
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17, 0) #17 gutterballs ouch lol
        self.assertEqual(16, self.g.score())
        
    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5)

if __name__ == '__main__':
    unittest.main()
