import random 
import hashlib 
import sympy 
import math 

def key_generation():
   # empiezo por buscar q primo de 160 bits.
   found = False
   while not found:
       q = random.randint(2**159, (2**160)-1)
       found = sympy.isprime(q)

   # Ahora elijo p de L = 512 bits
   # Busco p = q * 2z + 1 y que sea primo, 
   # tq z sea primo también y distinto de q 
   L = 512
   izq = (2**(L-1)-1)//q
   der = ((2**L)-1)//q
   found = False
   while not found:
       z = random.randint(izq, der-1)
       if sympy.isprime(z):
           p = 2*q*z+1
           found = sympy.isprime(p)
   
   #  g es un generador de del grupo ciclico de orden p-1
   found = False 
   while not found:
       g = random.randint(1, p-1)
       if pow(g, 2*q, p) != 1 and pow(g, 2*z, p) != 1 and pow(g,q*z,p) != 1:
           found = True 
           
   # x es la clave secreta 
   x = random.randint(2,p-2)
    
   # Calculo y 
   y = pow(g,x,p)
    
   #La clave publica es pk = (p,g,y), la clave secreta sk = x
   pk = (p,g,y) 
   sk = x
   return (pk, sk)

def H(m):
    # Función hash SHA-512
    # m tiene que ser de la forma b'mensaje'
    return int(hashlib.sha512(m).hexdigest(), base=16)

def firmaEG(m, p, g, x):
   k = 0 
   while math.gcd(k, p-1) != 1:
       k = random.randint (1, p-2)
    
   r = pow(g,k, p)
   s = (((H(m) - (x*r)) % (p-1)) * pow(k,-1,p-1)) % (p-1)
   if s == 0 :
       return firmaEG(m,p,g,x)
   else: 
       return (r,s)

def verificarEG(p,g,y,r,s,m):
    if (0<r<p) and (0<s<(p-1)):
        # Resolver la congruencia:
        # g^H(m) congruente ((y^r)*(r^s))modp
        u1 = pow(g,H(m),p)
        u2 = (pow(y,r,p) * pow(r,s,p)) % p
              
        return u1 == u2
    else:
        return False 

    
    
    
    
