from sympy import prime
from sympy import factorint
from sympy import mod_inverse

p, q = prime(50), prime(54)
n = p * q

print(p, q, n)

phi = (p-1)*(q-1)
print(factorint(phi))           # -> {19:1, 2:3, 3:1, 5:3}
e = 7 * 11 * 13
print(e)

d = mod_inverse(e, phi)
print(d)

# e -> encrypt
# d -> decrypt
# e und n öffentliche Schlüssel

# Verschlüsseln
crypt = lambda M, k: M ** k % n
N = 51234                       # Nachricht
S = crypt(N, e)
print(S)

# Entschlüsseln
D = crypt(S, d)

print(D)
