import random;import math;import copy
def zadaj_n():                          #funkcia pre input n
    n=int(input("Zadaj n="))
    if n%2!=0:
        return n
    if n%2==0:
        print("Číslo je párne")
        zadaj_n()
    return n
n=zadaj_n()
m=int((n-3)/2)
pocet_hviezdiciek=6*n-10-3*m            #pocet hviezdiciek hraca (vratane domcekov)
plocha=[]                               #prázdne pole pre plochu
def funkcia_pre_plochu():               #funkcia, ktorá mi vypíše plochu
    for i in range(n):
        plocha.append(n*[" "])
    for i in range(n):
        for j in range(m,m+3):
            plocha[i][j]="*"
    for i in range(1,n-1):
        for j in range(m+1,m+2):
            plocha[i][j]="D"
    for i in range(3):
        for j in range(n):
            if j==m+1:
                continue
            plocha[m+i][j]="*"
    for i in range(m+1,m+2):
        for j in range(1,n-1):
            if j==m+1:
                plocha[i][j]="X"
                continue
            plocha[i][j]="D"
funkcia_pre_plochu()
pA=[];pB=[]                             #prázdne pole pre súradnice hráča A a pre súradnice hráča B
for i in range(pocet_hviezdiciek):      
    pA.append(2*[" "])
    pB.append(2*[" "])
def suradniceA():
    for i in range(m):
        pA[i][0]=i
        pA[i][1]=m+2
    for i in range(m+1):
        pA[m+i][0]=m
        pA[m+i][1]=m+2+i
    pA[2*m+1][0]=m+1;pA[2*m+1][1]=n-1
    for i in range(m+1):
        pA[2*m+2+i][0]=m+2
        pA[2*m+2+i][1]=n-i-1
    for i in range(m):
        pA[3*m+3+i][0]=m+3+i 
        pA[3*m+3+i][1]=m+3-1
    pA[4*m+3][0]=n-1;pA[4*m+3][1]=m+1
    for i in range(m):
        pA[4*m+4+i][0]=n-1-i
        pA[4*m+4+i][1]=m
    for i in range(m+1):
        pA[5*m+4+i][0]=m+2
        pA[5*m+4+i][1]=m-i    
    pA[6*m+5][0]=m+1;pA[6*m+5][1]=0
    for i in range(m+1):
        pA[6*m+6+i][0]=m
        pA[6*m+6+i][1]=i
    for i in range(m):
        pA[7*m+7+i][0]=m-1-i
        pA[7*m+7+i][1]=m
    pA[8*m+7][0]=0;pA[8*m+7][1]=m+1
    for i in range(m):
        pA[8*m+8+i][0]=1+i
        pA[8*m+8+i][1]=m+1
suradniceA()                            #vyplnenie súradníc do polí pA a pB
def suradniceB():
    for i in range(m):
        pB[i][0]=n-1-i
        pB[i][1]=m
    for i in range(m+1):
        pB[m+i][0]=m+2
        pB[m+i][1]=m-i
    pB[2*m+1][0]=m+1;pB[2*m+1][1]=0
    for i in range(m+1):
        pB[2*m+2+i][0]=m
        pB[2*m+2+i][1]=i
    for i in range(m):
        pB[3*m+3+i][0]=m-1-i
        pB[3*m+3+i][1]=m
    pB[4*m+3][0]=0;pB[4*m+3][1]=m+1
    for i in range(m):
        pB[4*m+4+i][0]=i
        pB[4*m+4+i][1]=m+2
    for i in range(m+1):
        pB[5*m+4+i][0]=m
        pB[5*m+4+i][1]=m+2+i   
    pB[6*m+5][0]=m+1;pB[6*m+5][1]=n-1
    for i in range(m+1):
        pB[6*m+6+i][0]=m+2
        pB[6*m+6+i][1]=n-1-i
    for i in range(m):
        pB[7*m+7+i][0]=m+3+i
        pB[7*m+7+i][1]=m+3-1
    pB[8*m+7][0]=n-1;pB[8*m+7][1]=m+1
    for i in range(m):
        pB[8*m+8+i][0]=n-2-i
        pB[8*m+8+i][1]=m+1
suradniceB()
def pohybA(x,y):                        
    b=copy.deepcopy(plocha)
    b[x][y]="A"
    for i in range(n):
        print(" ".join(b[i]))
def pohybB(x,y):                         #funkcia, ktorá posunie hráča na zadané súradnice
    b=copy.deepcopy(plocha)
    b[x][y]="B"
    for i in range(n):
        print(" ".join(b[i]))
b=copy.deepcopy(plocha)
kA=0;sA=0;kB=0;sB=0                 #kocka hráča A, súradnice hráča A, kocka hráča B, súradnice hráča B
b[pA[sA][0]][pA[sA][1]]="A"
b[pB[sB][0]][pB[sB][1]]="B" 

for i in range(n):                  #výpis plochy s hráčmi na štarte
    print(" ".join(b[i]))
print("\n \n")
A=[]
B=[]

while (sA or sB) not in range(pocet_hviezdiciek-m,pocet_hviezdiciek):      #cyklus pre celú simuláciu
    if int(len(A))==m:
        break 
    if int(len(B))==m:
        break
    b=copy.deepcopy(plocha)
    kA=random.randint(1,6)
    if sA+kA>=pocet_hviezdiciek:
        sA-=kA
    sA+=kA
    if sA in range(pocet_hviezdiciek-m,pocet_hviezdiciek):
        if b[pA[sA][0]][pA[sA][1]]!="A":
            A.append("A")
        b[pA[sA][0]][pA[sA][1]]="A"
        b[pB[sB][0]][pB[sB][1]]="B"
        plocha[pA[sA][0]][pA[sA][1]]="A"
        sA=0
        print("Hráč A hodil="+str(kA)) 
        for i in range(n):
            print(" ".join(b[i]))
        print("\n \n")
        continue
    if pA[sA][0]==pB[sB][0] and pA[sA][1]==pB[sB][1]:
        sB=0
    print("Hráč A hodil="+str(kA))
    b[pA[sA][0]][pA[sA][1]]="A"
    b[pB[sB][0]][pB[sB][1]]="B"
    for i in range(n):
        print(" ".join(b[i]))
    print("\n \n")
    kB=random.randint(1,6)
    if sB+kB>=pocet_hviezdiciek:
        sB-=kB
    sB+=kB
    b=copy.deepcopy(plocha)
    if sB in range(pocet_hviezdiciek-m,pocet_hviezdiciek):
        if b[pB[sB][0]][pB[sB][1]]!="B":
            B.append("B")
        b[pA[sA][0]][pA[sA][1]]="A"
        b[pB[sB][0]][pB[sB][1]]="B"
        plocha[pB[sB][0]][pB[sB][1]]="B"
        sB=0
        print("Hráč B hodil="+str(kB))
        for i in range(n):
            print(" ".join(b[i]))
        print("\n \n")
        continue
    if pA[sA][0]==pB[sB][0] and pA[sA][1]==pB[sB][1]:
        sA=0
    b=copy.deepcopy(plocha)
    print("Hráč B hodil="+str(kB))
    b[pA[sA][0]][pA[sA][1]]="A"
    b[pB[sB][0]][pB[sB][1]]="B"
    for i in range(n):
        print(" ".join(b[i]))
    print("\n \n")
