import random
from middlewares.Conversion import bytes_to_int


def E(pk, m):
    m = bytes_to_int(m)
    n = pk['n']
    g = pk['g']
    h = pk['h']
    r = random.randint(1, n - 1)
    n2 = n * n
    c1 = 1 + m * n
    c1 = (c1 * pow(h, r, n2)) % n2
    c2 = pow(g, r, n2)
    return {'c1': c1, 'c2': c2}


def DE(pk, skp1, skp2, c):
    n = pk['n']
    g = pk['g']
    h = pk['h']
    n2 = n * n
    c1 = c['c1']
    c2 = c['c2']
    gskp1 = pow(c2, skp1, n2)
    c1 = (c1 * pow(gskp1, -1, n2)) % n2
    gskp2 = pow(c2, skp2, n2)
    c1 = (c1 * pow(gskp2, -1, n2)) % n2
    m = (c1 - 1) // n
    return m
