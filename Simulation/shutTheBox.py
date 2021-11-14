import random

class ShutTheBox:
    def __init__(self):
        self.available = {1,2,3,4,5,6,7,8,9}
        self.nextChance = True
        self.singleDice = False
        self.score = 0

    def rollDice(self):
        if self.singleDice:
            sum_ = random.randrange(1,6)
        else:
            sum_ = random.randrange(1,12)
            if sum_ > 9: return self.rollDice()
        return sum_

    def checkDiceRequired(self):
        higher = {7,8,9}
        if len(higher.intersection(self.available)) == 0:
            self.singleDice = True

    def shutBoxes(self):
        if self.nextChance:
            sum_ = self.rollDice()
            #print(sum_)
            l = len(self.available)
            if sum_ in self.available:
                self.available.discard(sum_)
            else:
                for i in range(1,(sum_ // 2)+1):
                    if i in self.available and (sum_-i) in self.available:
                        self.available.discard(i)
                        self.available.discard(sum_-i)
                        #self.nextChance = True
                        break
            if l == len(self.available): self.nextChance = False
            print(sum_, self.available)
            self.score = sum(list(self.available))
            if self.score == 0: return 0
            if self.score != 0:
                self.checkDiceRequired()
                return self.shutBoxes()
        else:
            return self.score

player1 = ShutTheBox()
player2 = ShutTheBox()
winner = ''

while player1.nextChance == True or player2.nextChance == True:
    if player1.shutBoxes() == 0: 
        winner = 'player1'
        break
    if player2.shutBoxes() == 0: 
        winner = 'player2'
        break
    print('scores : \nPlayer1 -> ', player1.score, '\mPlayer2 -> ', player2.score)

if winner == '':
    if player1.score < player2.score:
        winner = 'player1'
    elif player1.score > player2.score: 
        winner = 'player2'
    else: winner = 'Tie'

print('Winner : ', winner)
