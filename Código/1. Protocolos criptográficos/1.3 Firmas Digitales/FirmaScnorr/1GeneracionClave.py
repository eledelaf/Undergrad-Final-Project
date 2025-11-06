import random 
import hashlib 
import sympy 
from gmpy2 import powmod

def key_generation():
   found = False
   while not found:
       q = random.randint(2**159, (2**160)-1)
       found = sympy.isprime(q)
   L = 512
   izq = (2**(L-1)-1)//q
   der = ((2**L)-1)//q
   found = False
   while not found:
       z = random.randint(izq, der-1)
       p = q*z+1
       found = sympy.isprime(p)

   found = False
   while not found:
       h = random.randint(2,p-2)
       g = pow(h, z, p)
       found = g > 1
   x = random.randint(2,q-2)
   y = pow(g, -x, p)
   pk = (p,q,g,y)
   sk = x
   return (pk, sk)