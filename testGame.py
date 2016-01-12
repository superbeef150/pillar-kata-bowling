import unittest
#import game
from game import Game

class BowlingGameTest(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        result = 2 + 2
        self.assertEqual(4, result)
        
    def test_gutter_game(self):
        g = Game()
        score = 0;
        for x in xrange(1, 21):
            g.roll(0);
        self.assertEqual(0, g.score())



if __name__ == '__main__':
    unittest.main()
