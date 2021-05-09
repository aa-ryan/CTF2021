estr = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"

for i in range(len(estr)):
    print(chr(ord(estr[i])>>8), end="")
    print(chr((ord(estr[i]))-((ord(estr[i])>>8)<<8)), end="")

