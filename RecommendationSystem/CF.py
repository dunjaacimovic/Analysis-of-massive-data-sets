# Collaborative filtering
# item-item, user-user

from math import sqrt
import sys
from copy import deepcopy
import numpy as np
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
# Decimal(Decimal(x).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))

class CF:
    
    def __init__(self, n, m, ratings):
        self.n = n
        self.m = m
        self.ratings = ratings

    # def ratingToFloat(self, r):
    #     if r == 'X':
    #         return 0.0
    #     else:
    #         return float(r)
    
    def normalizeRatings(self):
        for row in range(self.n):
            # self.ratings[row] = list(map(self.ratingToFloat, self.ratings[row]))
            # sum(a)
            sum = 0.0; cnt = 0
            for i in range(self.m):
                x = self.ratings[row][i]
                if x != 'X':
                    sum += float(x)
                    cnt += 1
            avg = sum / float(cnt)
            for i in range(self.m):
                x = self.ratings[row][i]
                if x != 'X':
                    self.ratings[row][i] = float(x) - avg
                else:
                    self.ratings[row][i] = 0.0

    def cfII(self, i, j, k):
        
        array = np.array(self.ratings)
        transpose = array.T
        self.ratings = transpose.tolist()

        self.cfUU(j, i, k)
        
        # for r in len(ratings[0]):
        #     newRatings.append([ratings[0][r]])

        # print(newRatings)
        # for r in range(1, len(ratings)):    
        #     for c in range(self.m):
        #         newRatings[]




    def cfUU(self, i, j, k):

        originalRatings = deepcopy(self.ratings)
        self.normalizeRatings()
        # print(type(self.ratings))
        # print(self.ratings)

        # cosine similarity
        cosSim = defaultdict(lambda: 0.0)
        for item in range(self.n):
            if item == i: 
                cosSim[item] = 1.0
                continue
            sum = 0; sqSumX = 0; sqSumY = 0

            for user in range(self.m):
                if user == j: continue
                x = self.ratings[i][user]
                y = self.ratings[item][user]
                # if x != -40.0 and y != -40.0:
                sum += x*y
                sqSumX += x**2
                sqSumY += y**2
            cosSim[item] = sum / (sqrt(sqSumX * sqSumY))
        # print(cosSim)

        # popped2 = []

        for item in range(self.n):
            if originalRatings[item][j] == 'X':
                # popped2.append(item)
                cosSim.pop(item)
            # else:
            #     print(originalRatings[item][j])
        
        popped = []
        for key in cosSim:
            if cosSim[key] < 0:
                popped.append(key)
        for key in popped:
            cosSim.pop(key)

        sortedCosSim = {k: v for k, v in sorted(cosSim.items(), key=lambda item: item[1], reverse=True)}
        # print(sortedCosSim.keys())

        if len(sortedCosSim) >= k :
            # allkeys = sortedCosSim.keys()
            # keys = allkeys[:k]
            # print(k)
            # print(keys)
            # print(len(keys))
            kSims = {key: sortedCosSim[key] for key in list(sortedCosSim)[:k]}
            # print(kSims)
        else:
            kSims = sortedCosSim
            k = len(sortedCosSim)
        
        ratingSum = 0.0
        simSum = 0.0

        # print(originalRatings)

        for item in kSims:
            # print(item)
            # print(float(originalRatings[item][j])) 
            # print(kSims[item])

            ratingSum += float(originalRatings[item][j]) * kSims[item]
            simSum += kSims[item]
        
        rating = ratingSum / simSum
        print(float(Decimal(Decimal(rating).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))))

        # print(popped)
        # print(len(popped))
        # print(len(popped2))
        # print(len(cosSim))

        # for r in range()
        # # for item in range

    def collaborativeFiltering(self, i, j, t, k): 
        if t == 0: 
            self.cfII(i, j, k) 
        else:
            self.cfUU(i, j, k)


def main():
    # input = open('R.in', 'r' )
    input = sys.stdin

    # n - number of items, m - number of users
    (n, m) = map(int, input.readline().split())
    # print(n, m)
    ratings = []

    for cnt in range(n):
        item = input.readline().split()
        ratings.append(item)
    
    cf = CF(n, m, ratings)
    q = int(input.readline())

    for cnt in range(q):
        # i - item, j - user, t - algorithm type (0: ii, 1: uu), k - max number of similar items/users
        (i, j, t, k) = map(int, input.readline().split())
        # print(i, j, t, k)
        cf.collaborativeFiltering(i, j, t, k)


if __name__ == "__main__":
    main()
