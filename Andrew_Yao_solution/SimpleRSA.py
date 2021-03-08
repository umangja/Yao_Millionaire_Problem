import numpy as np
import random

## Any two random prime
p = 61
q = 53

## n = p*q
n = 3233

## e is any number coprime to phi(n) = (p-1)*(q-1)
e = 17

## d is number such that (d*e) % phi(n) == 1
d = 2753


## C = (m^e)%n

## compute (a^b)%mod
def powerMod(a, b, mod):
	ans = 1;
	while b>0 :
		if b%2 == 1:
			ans = (ans * a)%mod
		b = b//2
		a = (a*a)%mod
			
	return ans

## C = (m^e)%n
def encrypt(m):
	m = m + 10
	m = m%n 	
	return powerMod(m,e,n)	

# M = (c^d)%n
def decrypt(c):
	c = c%n
	m = powerMod(c,d,n)
	m = (m-10)%n
	return m

def Mulmod(c1,c2):
	m1 = decrypt(c1)
	m2 = decrypt(c2)

	return encrypt( (m1*m2) )


# def encrypt(m):
# 	return m	

# def decrypt(c):
# 	return c

# def Mulmod(c1,c2):
# 	return c1*c2