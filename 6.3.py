import random
students={"Иванов", "Сидоров", "Сёменова"}
langs=["китайский", "французский", "немецкий", "японский","корейский", "русский", "английский"]
slovar={}
spstudents=[]
for i in students:
    val=[]
    ch=random.randint(1,3) # задаём количество языков, которые знает студент
    while ch!=0:
        indlangs=random.randint(0,6)
        if langs[indlangs] not in val:
            val.append(langs[indlangs])
            ch-=1
            if langs[indlangs]=="китайский":
                spstudents.append(i)
    slovar[i]=val
print(slovar)
raznlangs=[]
for val in slovar.values():
    for i in val:
        if i not in raznlangs:
            raznlangs.append(i)
print(len(raznlangs), sorted(raznlangs), spstudents, sep="\n")
