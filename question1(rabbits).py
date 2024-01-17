"""def decode(x,n):
    if n>26:
        n=n%26
    ls=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ns=""
    for i in range(len(x)):
        for j in range(len(ls)):
            if (str(x[i]).upper())==ls[j]:
                ns=ns+ls[j+n]

    return ns

jd=decode("hello", 6)
print(jd)"""
def decode(x,n):
    ls=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    tx=x.split()
    ns=""
    for e in range(len(x)):
        if x[e].isalpha() :
            ind=ls.index(x[e].upper())
            if (ind-n)>26:
                ns=ns+ls[(ind-n)-26]
            else:
                ns=ns+ls[ind-n]
        else:
            ns=ns+x[e]
    return ns

def encrypt():
    x=input("enter a string\n>>>")
    n=int(input('enter key value\n>>>'))
    l=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ns=""
    for i in range(len(x)):
        if x[i].isalpha() :
            ind=l.index(x[i].upper())
            if (ind+n)>26:
                ns=ns+l[(ind+n)-26]
            else:
                ns=ns+l[ind+n]
        else:
            ns=ns+x[i]
    return ns
x="icilehd  oy ganoasitasiv  sqcolhldultd'ltdetoouiuo w siiosiionhfmio uyap\nfcc fcc e etusdoyrsreisreit itesa useuaxouaxohsth \nye' cpgpupgpuoo iai nlsoeiiseiisuuintfiolocrlarla\ngnsgr tu uicil"

y=int(input("enter key value\n>>>"))
dec=decode(x,y)
print(dec)
nl=['Pneumonoultramicroscopicsilicovolcanoconiosis',' Hippopotomonstrosesquippedaliophobia',' Supercalifragilisticexpialidocious',' Dichlorodifluoromethane']

#print(dec.split())
ol=dec.split()
for i in ol:
    for j in nl:
        if i==j.upper():
            print(f'\'{j}\' founded')