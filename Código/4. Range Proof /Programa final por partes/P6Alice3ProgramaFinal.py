def Alice3(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z,
           t0, t1, t2, tao1, tao2, T1,T2,x):
    
    l = [(aL[i]-z+sL[i]*x)%p for i in range(n)]
       
    r = [(pow(y,i,p) * (aR[i] + z + sR[i]*x) 
          + z**2 * pow(2, i, p)) % p for i in range(n)]
    
    t = sum([l[i]*r[i] % p for i in range(n)]) % p
    
    taox = (tao2 * x**2 + tao1 * x + z**2 * gamma) % p

    mu = (alpha + rho*x) % p 
    return (l,r,t,taox, mu)