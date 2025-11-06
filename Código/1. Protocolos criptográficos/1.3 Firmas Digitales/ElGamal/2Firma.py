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