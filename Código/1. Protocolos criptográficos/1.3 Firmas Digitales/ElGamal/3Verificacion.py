def verificarEG(p,g,y,r,s,m):
    if (0<r<p) and (0<s<(p-1)):
        # Resolver la congruencia:
        # g^H(m) congruente ((y^r)*(r^s))modp
        u1 = pow(g,H(m),p)
        u2 = (pow(y,r,p) * pow(r,s,p)) % p
        return u1 == u2
    
    else:
        return False 