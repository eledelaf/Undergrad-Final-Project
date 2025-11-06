import random 
import sympy 

# El numero secreto es x
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

# 1. Alice busca c perteneciente Zq y calcula w = g^c (modp) 
c = random.randint(0,q-1)
w = pow(g,c,p)

# 2. Bob escoge de forma aleatoria e perteneciente Zq 
# y 1 <= r <= 2^t
e = random.randint(0,q-1)

# 3. Alice calcula s = c + x*e (modq)
s =(c + x*e) % q

# 4. Se tiene que verificar que w = g^s * y^e (modp)
print( (pow(g,s, p)*pow(y,e,p))%p == w )
"""