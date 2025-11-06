#Quiero resolver logb(n) = x con b y n conocidos en Zp
# logb(n) = x sii b^x = n modp

def fuerzaBruta(b,n,p,limite):
    a = 1
    for i in range(limite):
        a = a%p
        if a == n:
            #print ('a')
            return i 
        else:
            #print('b')
            a *= b