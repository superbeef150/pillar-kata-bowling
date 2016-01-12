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
        self.assertEqual(0, self.g.score)
        
    def test_game_all_1s(self):
        self.setUp()
        self.rollMany(20, 1)
        self.assertEqual(20, self.g.score)

if __name__ == '__main__':
    unittest.main()
