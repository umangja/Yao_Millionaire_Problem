from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util import number
import numpy as np
import random
import SimpleRSA

import elgamal
import primes

# from simpleRSA.py import encrypt, decrypt
def get_TMatrix(x,pk):
    n = len(x)
    T = [[0] * n for i in range(2)]
    for j in range(n):
        T[x[j]][j]   = elgamal.encrypt(pk,1)
        T[1-x[j]][j] = elgamal.random_cipher(pk)     
    return T

def computeCt(T, y, pk):
    n = len(y)

    C = [0 for i in range(n)]
    c = 0

    for i in range(n):
        if y[i] == 0:
            y[i] = 1
            c_t = T[y[0]][0]
            for k in range(1, i + 1):
                c_t = elgamal.c_mul(pk, c_t, T[y[k]][k])
            c_t = elgamal.scalarize(pk, c_t)
            C[c] = c_t
            c =c + 1
            y[i] = 0

    for i in range(c,n):
        C[i] = elgamal.random_cipher(pk)

    random.shuffle(C)
    return C

def IsAliceRicher(C, sk):
    ansTemp = 0
    for c in C:
        if elgamal.decrypt(sk, c) == 1:
            ansTemp =  1 # x >y
    return ansTemp;


## works for numbers greter than 0 and less than < 1024
if __name__ == '__main__':

    sk, pk = elgamal.generate_keys(256)

    n = 11
    
    # Alice has x 
    # x -->[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    x = [random.randint(0,1) for i in range(n)] 
    y = [random.randint(0,1) for i in range(n)]

    GT = -1 
    for i in range(n):
        if x[i] > y[i]:
            GT = 1 
            break
        elif x[i] < y[i]:
            GT = 0 
            break
    else:
        GT = 0 


    T = get_TMatrix(x, pk)
    print("Alice T matrix is ") 
    print(T)
    C = computeCt(T, y, pk)
    print("Bob's C matrix is ")
    print(C)
    isAliceRicher = IsAliceRicher(C, sk)

    assert( isAliceRicher == GT)

    if isAliceRicher == 1: 
        print("Alice is Richer than Bob")
    else :
        print("Alice is poorer than Bob")




