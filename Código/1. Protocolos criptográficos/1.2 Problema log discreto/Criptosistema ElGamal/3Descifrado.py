def juntarnum(l,p):
    n = 0 
    while len(l)>1:
        n = n*(10**p) + l[0]*(10**p)
        l.pop(0)
    n = n + l[0]
        
    return n    

def dconv(l,n,p):
    # n el la longitud del mensaje 
    m = juntarnum(l,p)
    
    return m.to_bytes(n,byteorder = 'big', signed = False)

def descifradoEG(y1,y2,x,p,n):
    m = [( pow(y1,-x,p) * i ) % p for i in y2]
    
    return dconv(m,n,math.floor(math.log(p,10)))