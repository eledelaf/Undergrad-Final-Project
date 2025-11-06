from math import isqrt
from sympy import mod_inverse

def baby_step_giant_step(g, h, p):
    # Calcular m
    m = isqrt(p) + 1

    # Precomputación (Baby-steps)
    baby_steps = {}
    for j in range(m):
        baby_step = pow(g, j, p)
        baby_steps[baby_step] = j

    # Calcular el inverso multiplicativo de g^m
    g_m = pow(g, m, p)
    g_m_inv = mod_inverse(g_m, p)

    # Búsqueda (Giant-steps)
    for i in range(m):
        giant_step = (h * pow(g_m_inv, i, p)) % p
        if giant_step in baby_steps:
            j = baby_steps[giant_step]
            return i * m + j
    
    return None  # Si no se encuentra una solución