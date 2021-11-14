from collections import defaultdict
import random

class Mastermind:
    def __init__(self):
        self.num = [-1]*4
        self.cntr = 0
        self.number = 0000
        self.available = defaultdict(list)
        all_ = [1,2,3,4,5,6,7,8,9]
        for i in range(4):
            if i == 0: self.available[i] = all_.copy()
            else: self.available[i] = all_.copy() + [0]

    def generateNumber(self):
        for i in range(4):
            if self.num[i] == -1:
                self.num[i] = random.choice(self.available[i])
                

    def makeGuess(self, correct):
        self.cntr += 1

        for i in range(4):
            if correct[i] == -1:
                if self.num[i] in self.available[i]: 
                    self.available[i].remove(self.num[i])
                self.num[i] = -1

        self.generateNumber()
        return self.num


m = Mastermind()
num = random.randrange(1000, 10000)
correct = [-1]*4
print(num)
nums = []
while num > 0:
    nums.append(num % 10)
    num = num // 10
nums.reverse()
print(nums)

while m.makeGuess(correct):
    print(m.num, correct)
    if m.num == nums:
        print('You are a Mastermind!')
        break
    else:
        for i in range(4):
            if m.num[i] == nums[i]:
                correct[i] = nums[i]
