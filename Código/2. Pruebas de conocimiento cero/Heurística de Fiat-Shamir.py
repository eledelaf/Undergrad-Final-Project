
import random 
import sympy 
import hashlib

# Generar un numero primo de 10 digitos

def generar():    
    
    #Encontrar q primo de 10 digitos
    found = False
    while not found:
      q = random.randint(999999999, 9999999999)
      found = sympy.isprime(q)
      
    # Encontrar p primo de la forma p=q*2z+1 con z primo 
    found = False
    while not found:
      z = random.randint(99999, 999999)
      if sympy.isprime(z):
          p = q * 2 * z + 1
          found = sympy.isprime(p)
          
    # Encontrar g generador de el subgrupo cíclico de orden q
    found = False 
    while not found:
       g = random.randint(2, p-1)
       if pow(g, q, p) == 1:
           found = True
    
    # Encontrar a t, parametro de seguridad, tq q > 2**t
    found = False 
    while not found :
        t = random. randint(2,30)
        found = q > 2**t
        
    # Generar x totalmente random 
    x = random.randint(2,q-2)
    
    # Generar y 
    y = pow(g,-x,p)
    
    return (p,q,g,t,x,y)
"""
# Ejemplo 
(p,q,g,t,x,y) = generar()

# Alice busca c perteneciente a Zq y calcula w = g^c (modp)
c = random.randint(0,q-1)

w = pow(g,c,p)

# Alice calcula e = H(g|y|t)
m = str(g)+str(y)+str(t) 
m1 = m.encode('utf-8')
e = int(hashlib.sha1(m1).hexdigest(), base=16)

# Alice calcula s = c+xe (modq)
s =(c + x*e) % q

# Bob recive w y s. Comprueba que se cumple w = g^s * y^e (modp)
print( (pow(g,s, p)*pow(y,e,p))%p == w )

"""