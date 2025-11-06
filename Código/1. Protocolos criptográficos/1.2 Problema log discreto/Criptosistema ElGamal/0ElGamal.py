import random 
import sympy 

# Generador de claves (Alice) 
# Es lo mismo que en la firma digital ElGamal 
def key_generation():
     # empiezo por buscar q primo de 160 bits.

    found = False
    while not found:
       q = random.randint(2**159, (2**160)-1)
       found = sympy.isprime(q)

   # Ahora elijo p de L = 512 bits
   # Busco p = q * 2z + 1 y que sea primo, tq z sea primo también y distinto de q 
   
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
   
   # Calcular y = g^x(modp)
    y = pow(g,x,p)
   
    #La clave publica es pk = (p,g,y), la clave secreta sk = x
    pk = (p,g,y) 
    sk = x
    return (pk, sk)

# Cifrado del mensaje (Bob)  
def cifradoEG(g,p,y,m):
    b = random.randint(1,p-1)
    m1 = int.from_bytes(m, byteorder ='big', signed = False) 
    n = len(m)
    y1 = pow(g,b,p)
    y2 = ((pow(y,b,p))*m1)%p 
    
    c = (y1,y2)
     
    return (c,n)

# Descifrado del mensaje (Alicia)   
def descifradoEG(y1,y2,x,p,n):
    
    m = ( pow(y1,-x,p) * y2 ) % p
    return m.to_bytes(n,byteorder = 'big', signed = False)
