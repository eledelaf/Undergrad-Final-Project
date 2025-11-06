import random 
import hashlib 
import sympy 
from gmpy2 import powmod

# Firma digital DSA
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


   # elegir x en (1,q-1) aleatorio y hacer y = g**x mod p
   x = random.randint(2,q-2)
   y = pow(g, x, p)
   pk = (p,q,g,y)
   sk = x
   return (pk, sk)


# Firma 
def H(m):
    # Función hash SHA1
    # m tiene que ser de la forma b'mensaje'
    return int(hashlib.sha1(m).hexdigest(), base=16)
  
def firmaDSA(p, q, g, x, m):
    k = random.randint(2, q-1)
    r = (pow(g,k,p))%q
    s = (pow(k,-1,q) * (H(m) + x * r)) % q
    return (r,s)


# Verificación
def verDSA(r, s, m, p, q, g, y):
    if (1<r<(q-1)) and (1<s<(q-1)):
        w = pow(s,-1,q)
        u1 = (H(m)*w)%q 
        u2 = (r*w)%q
        v = ((powmod(g, u1, p) * powmod(y,u2,p)) % p) % q
        return v==r
    else:
        return False 