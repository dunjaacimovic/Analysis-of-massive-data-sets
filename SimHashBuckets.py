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
    for i in range(0, len(sh)):
        b = 1 if sh[i] >= 0 else 0
        result += b*(2**(127-i))
            
    return hex(result)[2:-1]


def createSimHashForAllLines(n, text):
    sh_lines = []
    
    for count in range(0, int(n)): 
        line = text.readline()
        sh_lines.append(simhash(line))
    
    return sh_lines

def hash2int(band, hash):
    start = (band-1) * 4
    end = band * 4
    
    return int((hash[start:end]), 16)

def addKeyToDictionary(dictionary, key1, key2):
        # if key1 in dictionary:
        #     print dictionary[key1]
        #     if key2 not in dictionary[key1]:
        #         dictionary[key1].append(key2)
        #     else:
        #         dictionary[key1] = [key2]
        if key1 not in dictionary:
            dictionary[key1] = [key2]
        elif key1 in dictionary and key2 not in dictionary[key1]:
            dictionary[key1].append(key2)
            
def lhs(n, simHash, num_of_bands, candidates):
    for band in range(1, num_of_bands+1):
        buckets = {}
        for current_key in range(0, n):
            hash = simHash[current_key]
            val = hash2int(band, hash)
            current_bucket = []

            if val in buckets  :
                current_bucket = buckets[val]
                for key in current_bucket:
                    addKeyToDictionary(candidates, current_key, key)
                    addKeyToDictionary(candidates, key, current_key)
            else:
                current_bucket = []
            
            if current_key not in current_bucket:
                current_bucket.append(current_key)
            buckets[val] = current_bucket
    
    return candidates
    
def hammingDistance(x, y):

    ans = 0
    x = int(x, 16)
    y = int(y, 16)
    for i in range(127,-1,-1):
        b1= x>>i&1
        b2 = y>>i&1
        ans+= not(b1==b2)
    
    return ans


def main():
    
    #otvaranje datoteke
    # file = open("R.in", "r")
    file = sys.stdin
    n = int(file.readline())

    simHash = createSimHashForAllLines(n, file)
    candidates = {}
    num_of_bands = 8

    candidates = lhs(n, simHash, num_of_bands, candidates)

    # cands4006 = candidates[2129]
    # print cands4006
    # k = 17


    
#     s1 = simHash[17]
#     print s1
#     print "candidates"
#     print candidates
#     print candidates[s1]

    q = int(file.readline())
    # for count in range(0, q): 
    result = 0  
    # line = file.readline()

    # [i, k] = line.split()
    # i = int(i); k = int(k)
    i = 4654
    k = 18

    print "i: " + str(i) + ", k: " + str(k)

    # i: 4654, k: 18
    # 32

    s1 = simHash[i]
    
    if i in candidates:
        print "\nkandidati: " 
        print candidates[i]
        print len(candidates[i])
        for candidate_index in range(0, len(candidates[i])):
            s2_index = candidates[i][candidate_index]
            s2 = simHash[s2_index]
            ham_dist = hammingDistance(s1, s2)
            # print ("ham_dist of " + str(i) + " and " + str(s2_index) + ": " + str(ham_dist))
            if ham_dist <= k:
                result += 1

# #             sys.stdout.write(str(result) + "\n")
    print str(result)

    file.close()

if __name__== "__main__":
    main()
    