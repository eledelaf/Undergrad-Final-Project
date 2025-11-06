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