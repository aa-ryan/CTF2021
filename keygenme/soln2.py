import base64
from hashlib import sha256


HASH = sha256(b"GOUGH").hexdigest()
LIST = [4, 5, 3, 6, 2, 7, 1, 8]

print("picoCTF{1n_7h3_|<3y_of_", end="")

for i in LIST:
  print(HASH[i], end = "")
print("}")
