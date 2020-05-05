for i in range(int(input())):
    s=input()
    w1=w2=""
    for j in range(len(s)):
        if j%2==0:
            w1+=s[j]
        else:
            w2+=s[j]
    print(w1+" "+w2)
