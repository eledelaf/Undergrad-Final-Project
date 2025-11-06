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