# Verificación 
def verSchnorr(R, S, m, p, q, g, Y):
    
    e = H(str(R).encode()+m) %q
    a = pow(g,S,p)
    b = (R * pow(Y,e,p))%p
    
    return a==b