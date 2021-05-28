encrpyted_flag = 0x5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b
encrpyted_a = 0x0346071d3d1904593d1903573d1950033d1958592a3d1905593d1900573f3d19
plaintext_a = 0x6161616161616161616161616161616161616161616161616161616161616161 # a = 61

# encrpyted_flag = flag ^ key 
# encrpyted_a = plaintext_a ^ key

plaintext_flag = encrpyted_flag ^ encrpyted_a ^ plaintext_a

print("{:x}".format(plaintext_flag))

