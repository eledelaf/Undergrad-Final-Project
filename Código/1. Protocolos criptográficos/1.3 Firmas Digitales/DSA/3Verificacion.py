def verDSA(r, s, m, p, q, g, y):
    if (1<r<(q-1)) and (1<s<(q-1)):
        w = pow(s,-1,q)
        u1 = (H(m)*w)%q 
        u2 = (r*w)%q
        v = ((powmod(g, u1, p) * powmod(y,u2,p)) % p) % q
        return v==r
    else:
        return False 