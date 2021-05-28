## Easy-Peasy

* nc mercury.picoctf.net 58913.
* KEY_LEN looks suspicious lets overflow it.
* check for length of flag (which is 64 i.e. in hex it's 32 chars long).
* The loop encrypts every 50000 chars at a time (XOR one-time pad is used).
* Now we should use vuln in loop that is giving it more than 50000.
	```bash
	python -c print('a'*49968) ; print('a' * 32)| nc mercury.picoctf.net 58913. # 49968 = 50000 - 32 (it will be 50000 encrpyted characters)
	```
* Encrpyted flag of a = 0346071d3d1904593d1903573d1950033d1958592a3d1905593d1900573f3d19
* Logic behind xor.
* soln.py we get as plaintext_flag but in hex.
* Hex to ASCII boom.
* HEX = 3939303732393936653666376433393766366561303132386234353137633233
* flag = picoCTF{99072996e6f7d397f6ea0128b4517c23}
