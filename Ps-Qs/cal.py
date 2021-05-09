def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
phi = (p - 1)*(q - 1)
e = 65537

d = modinv(e, phi)
c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496

plain = pow(c, d, n) # c ^ d % n
print(plain)
print(hex(plain))
print(bytearray.fromhex(hex(plain)[2:]).decode())
