def partirnum(num,p):
    n = 10**p
    lista = []
    
    while num > n:
        l = num % n
        lista = [l] + lista
        num = num // n   
    lista = [num] + lista
    
    return lista

def conv(m,p):
    # Primero pasamos la cadena de caracteres a un numero
    n = int.from_bytes(m, byteorder ='big', signed = False)
    l = partirnum(n,p)

    return l 
 
def cifradoEG(g,p,y,m):
    b = random.randint(1,p-1)
    m1 = conv(m,math.floor(math.log(p,10)))
    n = len(m)
    y1 = pow(g,b,p)
    y2 =[((pow(y,b,p))* i )%p for i in m1]
    c = (y1,y2)
     
    return (c,n)