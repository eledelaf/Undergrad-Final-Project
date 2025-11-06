def verSchnorr(r, s, m, p, q, g, y):
    e = H(str(r).encode()+m) %q
    rv = (pow(g,s,p)*pow(y,e,p))%p
    return r==rv