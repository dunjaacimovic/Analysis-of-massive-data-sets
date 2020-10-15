import sys
import numpy as np 
from collections import defaultdict

def findNearestBlackNode(visited, openedNodes, dist, nodeColors, adjacencyMatrix, deadEnds):
    
    if (dist > 10 or len(openedNodes) == 0):
        return (-1, -1)

    next = set()
    visited.union(openedNodes)
    for node in openedNodes:
        if(nodeColors[node] == 1):
            return (node, dist)
        next = next.union([node for node in adjacencyMatrix[node] if (node not in visited and node not in deadEnds)])
    return findNearestBlackNode(visited, sorted(next), dist+1, nodeColors, adjacencyMatrix, deadEnds)

def main():
    # input = open("RB.in", "r")
    input = sys.stdin

    (n, e) = map(int, input.readline().split())
    nodeColors = [];
    adjacencyMatrix = defaultdict(lambda: [])
    deadEnds = []

    for i in range(n):
        t = int(input.readline())
        nodeColors.append(t)
    
    for i in range(e):
        (s, d) = map(int, input.readline().split())
        adjacencyMatrix[s].append(d)
        adjacencyMatrix[d].append(s)

    for i in range(n):
        (node, dist) = findNearestBlackNode(set(), {i}, 0, nodeColors, adjacencyMatrix, deadEnds)
        if node == -1:
            deadEnds.append(node)
        print(node, dist)


if __name__ == "__main__":
    main()
