class Game(object):
    rolls = [0] * 21 #or you could do for i in xrange(21)]
    currentRoll = 0
    
    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll = self.currentRoll + 1
        
    def score(self):
        score = 0
        frameIndex = 0
        for frame in xrange(0, 10):
            if (self.isStrike(frameIndex)):
                score += 10 + self.strikeBonus(frameIndex)
                frameIndex += 1
                print "STRIKE!! MOM GET THE CAMERA"
                print "score is now ",score," after frameIndex ",frameIndex
                continue
            elif (self.isSpare(frameIndex)):
                score += 10 + self.spareBonus(frameIndex)
                print "SPARE OH BABY"
            else:
                score += self.sumOfBallsInFrame(frameIndex)
            frameIndex += 2
            print "score is now ",score," after frameIndex ",frameIndex
        return score
    
    
    def isStrike(self, frameIndex):
        return self.rolls[frameIndex] == 10
    
    def sumOfBallsInFrame(self, frameIndex):
        return self.rolls[frameIndex]+self.rolls[frameIndex+1]
    
    def spareBonus(self, frameIndex):
        return self.rolls[frameIndex+2]
        
    def strikeBonus(self, frameIndex):
        return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]
    
    def isSpare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10
