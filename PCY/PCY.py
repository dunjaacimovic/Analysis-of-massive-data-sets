import sys
import collections
import numpy as np
import itertools as it


def PCY(input):
    # input = open(file, "r")
    n = float(input.readline())
    s = float(input.readline().strip())
    required_min = int(s*n)

    n = int(n)
    b = int(input.readline())
    items = collections.defaultdict(lambda : 0)
    baskets = []

    for num in range(n):
        line = input.readline().rstrip()
        basket = map(int, line.split())
        baskets.append(basket)
        for item in basket:
            items[item] += 1 

    itemsNum = len(items)
    buckets = collections.defaultdict(lambda : 0)

    for basket in baskets:
        for (i, j) in it.combinations(basket, 2):
            if (items[i] >= required_min) and (items[j] >= required_min):
                k = ((i * itemsNum) + j) % b
                buckets[k] += 1
    print len(buckets)

    frequent_itemsets = collections.defaultdict(lambda : 0)

    for basket in baskets:
        for (i, j) in it.combinations(basket, 2):
            if (items[i] >= required_min) and (items[j] >= required_min):
                k = ((i * itemsNum) + j) % b 
                if(buckets[k] >= required_min):
                    frequent_itemsets[(i, j)] += 1

    print len(frequent_itemsets)

    values = frequent_itemsets.values()
    values.sort(reverse=True)
    for v in values:
        print v
    


def main():
    input = sys.stdin
    # file = "R.in"
    PCY(input)


if __name__ == "__main__":
    main()