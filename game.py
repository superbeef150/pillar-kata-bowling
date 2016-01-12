class Game(object):
    rolls = [0] * 21 #or you could do for i in xrange(21)]
    currentRoll = 0
    
    def roll(self, pins):
        #self.score += pins
        self.rolls[self.currentRoll] = pins
        self.currentRoll = self.currentRoll + 1
        
    def score(self):
        score = 0
        frameIndex = 0
        for frame in xrange(0, 10):
            if (self.isSpare(frameIndex)):
                score += 10 + self.rolls[frameIndex+2]
            else:
                score += self.rolls[frameIndex] + self.rolls[frameIndex+1]
            frameIndex += 2
        return score
        
    
    def isSpare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10


'''
For the last check-in for Test 2, it is worth noting that in python, you cannot have variables and functions with the same name.

In the example, they had both an int and a function that returns an int called score
In my check-in for Test 2 I did not include the function since the var score is necessary but the function is not
If you rename the function to something such as getScore it flags it as unnecessary, so I simply left it out

that having been said, the int variable "score" is replaced in a method in the steps taken to complete Test 3 so this becomes a moot point
'''