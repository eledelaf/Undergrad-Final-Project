def Bob3(gamma,V, aL, aR, alpha, A, sL, sR, rho, S, y, z,
         t0, t1, t2, tao1, tao2, T1,T2,x,l,r,t,taox, mu):
    
    a1 = (pow(g, t, q) * pow(h, taox, q)) % q
    
    d = ((z-z**2) * sum([pow(y,i,p) for i in range(n)]) 
         - z**3 * sum([pow(2,i,p) for i in range(n)])) % p
    
    a2 = pow(V, pow(z,2,p), q) * pow(g, d, q) 
        * pow(T1, x, q) * pow(T2, pow(x,2,p), q) % q
        
    if a1 != a2:
        print("error1")
        
    vh = [pow(hi[i], pow(y, -i, p), q) for i in range(n)]
    
    b1 = A * pow(S, x, q) % q
    for i in range(n):
        b1 = b1 * pow(gi[i], -z, q) % q
        b1 = b1 * pow(vh[i], (z*pow(y,i,p) 
                              + pow(z,2,p)*pow(2,i,p))%p, q) % q
        
    b2 = pow(h, mu, q)
    for i in range(n):
        b2 = b2 * pow(gi[i], l[i], q) % q
        b2 = b2 * pow(vh[i], r[i], q) % q
    if b1 != b2:
       print("error2")
    
    c1 = t
    c2 = sum([l[i] * r[i] % p for i in range(n)]) % p
    if c1 != c2:
       print("error3")
       
    print("ok")