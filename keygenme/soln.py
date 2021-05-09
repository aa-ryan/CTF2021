from hashlib import sha256
from importlib import import_module

keygen = import_module("keygenmepy")
# print(keygen.bUsername_trial)

h = sha256(keygen.bUsername_trial).hexdigest()

print(f"{keygen.key_part_static1_trial} {''.join([h[4],h[5],h[3],h[6],h[2],h[7],h[1],h[8]])}}") # just need to decode dynamic part

