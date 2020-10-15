import sys
import numpy as np
import hashlib

def simhash(text):
    sh = np.zeros(128, dtype=int)
    words = text.split()
    for word in words:
        hash = hashlib.md5(word.encode()).hexdigest()
        binary_hash = bin(int(hash, 16))[2:].zfill(128)
        for cnt, b in enumerate(binary_hash):
            sh[cnt] += 1 if int(b)==1 else -1
            
    binary_result = ""
    for i in range(0, len(sh)):
        sh[i] = 1 if sh[i] >= 0 else 0
        
    return sh


def hammingDistance(x, y, k):
    ans = 0
    for i in range(128):
        ans += not(x[i] == y[i])
        if ans > k: return 0
    return 1

def main():
    sh_lines = []
    file = sys.stdin
    n = int(file.readline())

    sh_lines = [(simhash(file.readline())) for count in range(n)]
    
    q = int(file.readline())
    for count in range(q):
        result = 0
        line = file.readline()
        
        [i, k] =  line.split()
        i = int(i); k = int(k)
        s1 = sh_lines[i]

        for index in range(0, q):
            if index == i: continue
            ham_dist = hammingDistance(s1, sh_lines[index], k)
            result += ham_dist
        print result

if __name__== "__main__":
    main()
  
