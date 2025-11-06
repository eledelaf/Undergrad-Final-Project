#Firma de Schnorr multiparty
import random 
import hashlib 
import sympy 
from gmpy2 import powmod

def key_generation(n):
   # empiezo por buscar q primo de 160 bits.
   found = False
   while not found:
       q = random.randint(2**159, (2**160)-1)
       found = sympy.isprime(q)
   # ahora elijo p de L = 512 bits
   L = 512
   izq = (2**(L-1)-1)//q
   der = ((2**L)-1)//q
   found = False
   while not found:
       z = random.randint(izq, der-1)
       p = q*z+1
       found = sympy.isprime(p)
   # ahora elijo h en (1,p-1) tal que g = h**z mod p > 1
   found = False
   while not found:
       h = random.randint(2,p-2)
       g = pow(h, z, p)
       found = g > 1
   # elegir x en (1,q-1) aleatorio y hacer y = g**(x) mod p
   lx = []
   Y=1
   for i in range(0,n):
       x = random.randint(2,q-2)
       lx.append(x)
       y = pow(g, x, p)
       Y =( Y*y )%p 
       
   pk = (p,q,g,Y)
   sk = lx
   return (pk, sk)