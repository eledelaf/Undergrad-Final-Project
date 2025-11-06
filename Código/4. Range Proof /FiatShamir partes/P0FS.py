import random
import sympy
import hashlib

v  = 2024
L = 160 
n = 20 

def gen_resto_cuad(q):
    found = False
    while not found:
        x = random.randint(2,q-1)
        found = pow(x, (q-1)//2, q) == 1
    return x

def generarGH(n, L):
   found = False
   while not found:
      p = random.randint(2**(L-1), 2**L)
      q = 2*p+1
      found = sympy.isprime(p) and sympy.isprime(q)
   g = gen_resto_cuad(q)
   h = gen_resto_cuad(q)
   gi = [gen_resto_cuad(q) for i in range(n)]
   hi = [gen_resto_cuad(q) for i in range(n)]
   return (p, q, g, h, gi, hi)

(p, q, g, h, gi, hi) = generarGH(n, L)