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

    ym = str(V)+str(A)+str(S)+ str(1)
    ym1 = ym.encode('utf-8')
    y = (int(hashlib.sha1(ym1).hexdigest(), base=16))%p
    
    zm = str(V)+str(A)+str(S)+ str(2)
    zm1 = zm.encode('utf-8')
    z = (int(hashlib.sha1(zm1).hexdigest(), base=16))%p
        
    # Calculo t0, t1, t2
    t0 = 0
    for i in range(n):
        t0 += (aL[i]-z) * (pow(y,i,p)*(aR[i]+z) 
                           + pow(z,2,p)*pow(2,i,p))
        t0 %= p
        
    t1 = 0
    for i in range(n):
        t1 += (aL[i]-z)*sR[i]*pow(y,i,p)
        t1 += sL[i] * (pow(y,i,p)*(aR[i]+z) 
                       + pow(z,2,p)*pow(2,i,p))
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

    xm = str(T1)+str(T2)
    xm1 = xm.encode('utf-8')
    x = (int(hashlib.sha1(xm1).hexdigest(), base=16))%p

    # 1. Calculo l(x)
    l = [(aL[i]-z+sL[i]*x)%p for i in range(n)]
    
    # 2. Calculo r(x)   
    r = [(pow(y,i,p) * (aR[i] + z + sR[i]*x) 
          + z**2 * pow(2, i, p)) % p for i in range(n)]
    
    # 3. Calculo t 
    t = sum([l[i]*r[i] % p for i in range(n)]) % p
    
    # 4. taox 
    taox = (tao2 * x**2 + tao1 * x + z**2 * gamma) % p
    
    # 5. mu 
    mu = (alpha + rho*x) % p 
    return (gamma,V, aL, aR, alpha, A, sL, sR, 
            rho, S, y, z,t0, t1, t2, tao1, tao2, 
            T1,T2,x,l,r,t,taox, mu)
