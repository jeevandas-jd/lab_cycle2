def encrypt():
    x='learning python is fun'
    k=int(input("enter key \n>>>"))
    d=[]
    m=len(x)//k
    tk=k
    if len(x)%k != 0:
        m=m+1
        x=x+("~"*m)

    j=0
    for i in range(m):
        d.append(list(x[j:tk]))
        tk=tk+k
        j=j+k
    ns=""
    print(d)
    for q in range(k):
        for p in range(len(d)):
             ns=ns+(d[p][q])
    print(ns)
encrypt()
