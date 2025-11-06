def Alice2(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z):
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
    return (t0, t1, t2, tao1, tao2, T1,T2)