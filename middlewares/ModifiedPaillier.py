from charm.core.math.integer import integer
from charm.toolbox.integergroup import RSAGroup

def E(pk,m):
    group = RSAGroup()
    n = pk['n']
    n2 = n * n
    h = pk['h']
    g = pk['g']
    r = group.random(n)
    m = integer(m) % n  
    c1 = integer(1) % n2 + (m % n2) * (n % n2)
    c1 = c1 * ((h % n2) ** r)
    c2 = (g % n2) ** r
    return {'c1' : c1,'c2' : c2}

def DE(pk, sk, c):
    group = RSAGroup()
    n = pk['n']
    n2 = n * n
    h = pk['h']
    g = pk['g']
    c1 = c['c1']
    c2 = c['c2']
    sk = integer(sk) % n2
    c2 = c2 ** sk
    c1 = c1 / c2
    m = (c1 - integer(1) % n2)
    n = n % n2

    inv = (integer(7) % n2) ** ((n2 - 2) % n2)
    print((integer(7) % n2) * inv)
    
    return m
    
    