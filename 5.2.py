import random
sp=[]
dlsp=random.randint(2,10)
for i in range(dlsp):
    ch=random.randint(0,10)
    sp.append(ch)
print(sp)
povtorch=[]
for i in range(len(sp)-1):
    for j in range(i+1, len(sp)):
        if (sp[i]==sp[j]) and (sp[i] not in povtorch):
            povtorch.append(sp[i])
res=""
for i in range(len(povtorch)):
    res += str(povtorch[i])+ " "
print(res)

