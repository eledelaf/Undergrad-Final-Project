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