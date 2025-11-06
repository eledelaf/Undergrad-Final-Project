def H(m):
    # Función hash SHA1
    # m tiene que ser de la forma b'mensaje'
    return int(hashlib.sha1(m).hexdigest(), base=16)
  
def firmaDSA(p, q, g, x, m):
    k = random.randint(2, q-1)
    r = (pow(g,k,p))%q
    s = (pow(k,-1,q) * (H(m) + x * r)) % q
    return (r,s)