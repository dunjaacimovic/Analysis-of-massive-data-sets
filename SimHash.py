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
        binary_result += str(sh[i])

    hex_result = hex(int(binary_result, 2))
    return str(hex_result[2:-1])


def hammingDistance(x, y):

    ans = 0
    x = int(x, 16)
    y = int(y, 16)
    for i in range(127,-1,-1):
     b1= x>>i&1
     b2 = y>>i&1
     ans+= not(b1==b2)
    
#      if not(b1==b2):
#         print(b1,b2,i, "diff")
#      else:
#         print(b1,b2,i)
    return ans

# def main():

sh_lines = []
#     file = open(file, "r")
file = sys.stdin
n = file.readline()

for count in range(0, int(n)): 
    line = file.readline()
    sh_lines.append(simhash(line))
    
#     s1 = simhash("fakultet elektrotehnike i racunarstva")
#     s2 = simhash("fakultet elektronike i racunarstva")
#     print s1
#     print s2
#     ham = hammingDistance(s1, s2)
#     print ham
#     print type(ham)
#     print sh_lines


q = int(file.readline())
for count in range(1, q): 
    result = 0
    line = file.readline()
#     print(line)

    [i, k] =  line.split()
#         print i, k
    i = int(i)
    k = int(k)
    
    s1 = sh_lines[i]
    for index in range(0, q):
        if index == i: continue
        s2 = sh_lines[index]
        ham_dist = hammingDistance(s1, s2)
        if ham_dist <= k:
#                 print ham_dist
            result += 1
    sys.stdout.write(str(result) + "\n")
    sys.stdout.write("hello")
    # file.close()

  
# if __name__== "__main__":
#     main()
#     sys.stdout.write("hello")