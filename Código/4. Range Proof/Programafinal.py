import random
import sympy

v  = 2024
L = 160 # Numero de bits
n = 20 #Longitud de los vectores

def gen_resto_cuad(q):
    found = False
    while not found:
        x = random.randint(2,q-1)
        found = pow(x, (q-1)//2, q) == 1
    return x

def generarGH(n, L):
   found = False
   while not found:
      p = random.randint(2**(L-1), 2**L)
      q = 2*p+1
      found = sympy.isprime(p) and sympy.isprime(q)
   g = gen_resto_cuad(q)
   h = gen_resto_cuad(q)
   gi = [gen_resto_cuad(q) for i in range(n)]
   hi = [gen_resto_cuad(q) for i in range(n)]
   return (p, q, g, h, gi, hi)

(p, q, g, h, gi, hi) = generarGH(n, L)

def Alice1(v):
    # Calculo V
    gamma = random.randint(0,p-1)
    V = (pow(h, gamma, q) * pow(g, v, q)) % q
    
    # Calculo A
    #Calculo aL y aR
    a = bin(v)[2:]
    if len(a) < n:
        a = "0"*(n-len(a)) + a
    aL = []
    for i in range(n):
        if a[n-1-i] == '0':
            aL.append(0)
        else:
            aL.append(1)   
    aR = [(aL[i]-1) % p for i in range(n)]
    alpha = random.randint(0, p-1)
    A = pow(h, alpha, q)
    for i in range(n):
        A = (A * pow(gi[i], aL[i], q)) % q
        A = (A * pow(hi[i], aR[i], q)) % q
    
    # Calculo S
    # Calculo sL y sR
    [sL, sR ]= [[],[]]
    for i in range(n):
        sL.append(random.randint(0,p-1))
        sR.append(random.randint(0,p-1))
        
    rho = random.randint(0,p-1) 
    S = pow(h, rho, q)
    for i in range(n):
        S = (S * pow(gi[i], sL[i], q)) % q
        S = (S * pow(hi[i], sR[i], q)) % q
    return (gamma,V, aL, aR, alpha, A, sL, sR, rho, S)

def Bob1():
    [y, z]= [random.randint(1, p-1),random.randint(1, p-1)]
    return (y,z)

def Alice2(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z):
    # Calculo t0, t1, t2
    t0 = 0
    for i in range(n):
        t0 += (aL[i]-z) * (pow(y,i,p)*(aR[i]+z) + pow(z,2,p)*pow(2,i,p))
        t0 %= p
        
    t1 = 0
    for i in range(n):
        t1 += (aL[i]-z)*sR[i]*pow(y,i,p)
        t1 += sL[i] * (pow(y,i,p)*(aR[i]+z) + pow(z,2,p)*pow(2,i,p))
        t1  %= p
        
    t2 = 0
    for i in range(n):
        t2 = (t2 + sL[i]*pow(y,i,p)*sR[i]) % p
    
    # Calculo tao1, tao2
    tao1 = random.randint(0, p-1)
    tao2 = random.randint(0, p-1)
    
    # Calculo T1, T2
    T1 = (pow(g, t1, q) * pow(h, tao1, q)) % q
    T2 = (pow(g, t2, q) * pow(h, tao2, q)) % q
    return (t0, t1, t2, tao1, tao2, T1,T2)

def Bob2(T1,T2):
    x = random.randint(1, p-1)
    return x
    
def Alice3(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z,t0, t1, t2, tao1, tao2, T1,T2,x):
    # 1. Calculo l(x) = aL-z+sLx
    l = [(aL[i]-z+sL[i]*x)%p for i in range(n)]
    
    # 2. Calculo r(x)=(1,y,...,y^(n-1))*(aR+z+sRx)+z^2*(1,2,...,2^(n-1))   
    r = [(pow(y,i,p) * (aR[i] + z + sR[i]*x) + z**2 * pow(2, i, p)) % p for i in range(n)]
    
    # 3. Calculo t = <l,r>
    t = sum([l[i]*r[i] % p for i in range(n)]) % p
    
    # 4. taox = tao2 * x^2+ tao1 * x + z^2 *gamma
    taox = (tao2 * x**2 + tao1 * x + z**2 * gamma) % p
    
    # 5. mu = delta + rho*x 
    mu = (alpha + rho*x) % p 
    return (l,r,t,taox, mu)

def Bob3(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z,t0, t1, t2, tao1, tao2, T1,T2,x,l,r,t,taox, mu):
    #1.Primera igualdad g^t * h^taox = V^(z^2) * g ^(delta(y,z))*T1(^x)*T2(^x^2)
    # a1 = g^t * h^taox
    a1 = (pow(g, t, q) * pow(h, taox, q)) % q
    #1.1 Caclulo  delta que pertenece a Zp
    d = ((z-z**2) * sum([pow(y,i,p) for i in range(n)]) - z**3 * sum([pow(2,i,p) for i in range(n)])) % p
    
    # delta(y,z) = (z-z^2)<(1,...,1),(1,y,...,y^(n-1)>-z^3<(1,...,1),(1,2,...,2^(n-1)>
    # a2 = V^(z^2) * g ^(delta(y,z))*T1(^x)*T2(^x^2)
    a2 = pow(V, pow(z,2,p), q) * pow(g, d, q) * pow(T1, x, q) * pow(T2, pow(x,2,p), q) % q
    if a1 != a2:
        print("error1")
        
    # 2. Segunda igualdad 
    # 2.1 Sacar el vector h= hi^(y^(-i+1))
    vh = [pow(hi[i], pow(y, -i, p), q) for i in range(n)]
    
    b1 = A * pow(S, x, q) % q
    for i in range(n):
        b1 = b1 * pow(gi[i], -z, q) % q
        b1 = b1 * pow(vh[i], (z*pow(y,i,p) + pow(z,2,p)*pow(2,i,p))%p, q) % q
        
    b2 = pow(h, mu, q)
    for i in range(n):
        b2 = b2 * pow(gi[i], l[i], q) % q
        b2 = b2 * pow(vh[i], r[i], q) % q
    if b1 != b2:
       print("error2")
    
    # 3. Tercera igualdad
    c1 = t
    c2 = sum([l[i] * r[i] % p for i in range(n)]) % p
    if c1 != c2:
       print("error3")
    print("ok")
 

(gamma,V, aL, aR, alpha, A, sL, sR, rho, S) = Alice1(v)
(y,z) = Bob1()
(t0, t1, t2, tao1, tao2, T1,T2) = Alice2(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z)
x = Bob2(T1, T2)
(l,r,t,taox, mu) = Alice3(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z,t0, t1, t2, tao1, tao2, T1,T2,x)
Bob3(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z,t0, t1, t2, tao1, tao2, T1,T2,x,l,r,t,taox, mu)
