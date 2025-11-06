#Firma de Schnorr 
import random 
import hashlib 
import sympy 
from gmpy2 import powmod

def key_generation():
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
       
   # elegir x en (1,q-1) aleatorio y hacer y = g**(-x) mod p
   x = random.randint(2,q-2)
   y = pow(g, -x, p)
   pk = (p,q,g,y)
   sk = x
   return (pk, sk)

# Firma 
def H(m):
    return int(hashlib.sha1(m).hexdigest(), base=16)
  
def firmaSchnorr(p, q, g, x, m):
    k = random.randint(2, q-1)
    r1 = pow(g,k,p)
    r = str(r1).encode()
    m1 =  r + m
    e = H(m1) % q
    s = (k + x* e)%p 
    
    return (r1,s)

# Verificación 
def verSchnorr(r, s, m, p, q, g, y):
    e = H(str(r).encode()+m) %q
    rv = (powmod(g,s,p)*powmod(y,e,p))%p  
    return r==rv