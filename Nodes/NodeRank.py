import numpy as np
import sys

def main():
    # input = open('R.in', 'r's )
    input = sys.stdin
    firstline = input.readline().split()
    
    n = int(firstline[0]); 
    B = float(firstline[1])
    rank = {}
    matrix = {}
    queries = []
    maxIter = 0

    for i in range(n):
        matrix[i] = [int(x) for x in input.readline().split()]

    q = int(input.readline())

    # queries = np.array([list(map(int, input.readline().split())) for cnt in range(q)])
    # iterations = [q[1] for q in queries]
    # maxIterations = max(iterations)
    # print(maxIterations)
    for cnt in range(q):
        (index, iterations) = map(int, input.readline().split())
        queries.append((index, iterations))
        if iterations > maxIter: 
            maxIter = iterations
    # print(maxIter)

    initRank = (1.0-B) / n
    rank[0] = np.full(n, 1.0/n)

    convergenceIteration = 30000
    for iteration in range(maxIter):
        rank[iteration+1] = np.full(n, initRank)

        for index in range(n):
            value = B * rank[iteration][index] / len(matrix[index])
            for dest in matrix[index]:
                rank[iteration+1][dest] += value

        if np.sum(np.abs(rank[iteration+1] - rank[iteration])) < 1e-10:
            convergenceIteration = iteration
            break

    for q in queries:
        if q[1] <= convergenceIteration:
            print("{:.10f}".format(rank[q[1]][q[0]]))
        else:
            print("{:.10f}".format(rank[convergenceIteration][q[0]]))

if __name__ == "__main__":
    main()
