'''import random


class flip_coin:
    def coinToss(self):
        heads = 0
        tails = 0
        headpercentage = 0
        tailpercentage = 0
        inp = int(input(" Number Of Times You Want To flip Coin: "))

        num = random.randint(0, 1)
        for i in range(inp):
            if num <= 0.5:
                print("Tail")
                tails += 1
            else:
                print("Head")
                heads += 1
        headpercentage = heads / inp * 100
        tailpercentage = tails / inp * 100
        print("Total HeadPercentage: {}".format(headpercentage), " & Total Headcount: {}".format(heads))
        print("Total TailPercentage: {}".format(tailpercentage), " & Total Tailcount: {}".format(tails))


output = flip_coin()
output.coinToss()'''

# Program to flip coin

import random


class flip_coin:
    def coinToss(self):
        number = int(input("Number Of Time To flip Coin: "))
        head = 0
        tail = 0
        for flip in range(number):
            coinFlip = random.choice([0, 1])
            if coinFlip < 0.5:
                tail += 1
                print("Tails")

            else:
                head += 1
                print("Heads")

        tailpercentage = tail / number * 100
        headpercentage = head / number * 100
        print("Total TailPercentage: {}".format(tailpercentage), " & Total Tailcount: {}".format(tail))
        print("Total HeadPercentage: {}".format(headpercentage), " & Total Headcount: {}".format(head))


output = flip_coin()
output.coinToss()
