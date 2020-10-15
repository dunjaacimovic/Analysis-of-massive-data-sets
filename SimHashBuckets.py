import sys
import numpy as np
import hashlib

def simhash(text):
    sh = np.zeros(128, dtype=int)
    words = text.split()
    for word in words:
        hash = hashlib.md5(word).hexdigest()
        binary_hash = int(hash, 16)
        for i in range(127, -1, -1):
            b = binary_hash>>i&1
            sh[127-i] += 1 if b == 1 else -1
    result = 0
    for i in range(len(sh)):
        b = 1 if sh[i] >= 0 else 0
        result += b*(2**(127-i))
    return hex(result)[2:-1]

def createSimHashForAllLines(n, text, candidates):
    sh_lines = []
    for count in range(n):
        candidates[count] = set()
        sh_lines.append(simhash(text.readline()))
    return sh_lines

def hash2int(band, hash):
    start = band * 4
    end = (band + 1) * 4
    return int((hash[start:end]), 16)
            
def lhs(n, simHash, candidates):
    for bucket in range(8):
        buckets = {}
        for i in range(n):
            hash = simHash[i]
            val = hash2int(bucket, hash)
            
            if val in buckets:
                text_in_bucket = buckets[val]
                for text_id in text_in_bucket:
                    candidates[i].add(text_id)
                    candidates[text_id].add(i)
            else:
                text_in_bucket = set()
            text_in_bucket.add(i)
            buckets[val] = text_in_bucket
    
def hammingDistance(x, y, k):
    ans = 0
    x = int(x, 16)
    y = int(y, 16)
    for i in range(127,-1,-1):
        b1= x>>i&1
        b2 = y>>i&1
        ans += not(b1==b2)
        if ans > k: return 0
    return 1

def main():
    file = sys.stdin
    n = int(file.readline())
    candidates = {}
    simHash = createSimHashForAllLines(n, file, candidates)

    lhs(n, simHash, candidates)

    q = int(file.readline())
    for count in range(q):
        line = file.readline()
        [i, k] = [int(l) for l in line.split()]
        print sum([hammingDistance(simHash[i], simHash[candidate], k) for candidate in candidates[i]])


if __name__== "__main__":
    main()
    
