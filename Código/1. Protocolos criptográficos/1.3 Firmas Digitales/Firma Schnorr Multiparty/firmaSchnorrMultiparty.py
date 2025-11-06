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

# Firma 
def H(m):
    return int(hashlib.sha1(m).hexdigest(), base=16)
  
def firmaSchnorr(p, q, g, lx, m,n):
    lk = []
    R=1
    for i in range(0,n):
        k = random.randint(2, q-1)
        lk.append(k)
        r1 = pow(g,k,p)
        R = R*r1
    
    r = str(R).encode()
    
    m1 =  r + m
    e = H(m1) % q
    
    S= 0
    for i in range(0,n):
        s = (lk[i] + lx[i]* e)%p 
        S = S+s
    
    return (R,S)

# Verificación 
def verSchnorr(R, S, m, p, q, g, Y):
    
    e = H(str(R).encode()+m) %q
    a = pow(g,S,p)
    b = (R * pow(Y,e,p))%p
    
    return a==b