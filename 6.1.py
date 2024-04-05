slovar={"Россия":"Москва",
        "Казахстан":"Астана",
        "Норвегия":"Осло",
        "Испания":"Мадрид",
        "Китай":"Пекин"}
def a():
    for keyi in slovar:
        print(keyi, " - ", slovar[keyi])
def b():
    key=input("Введите название страны, чтобы узнать ее столицу ")
    print(slovar.get(key, " Такой страны не существует"))
# slovar[key]
def b2():
    key=input("Введите страну/столицу ")
    for i in slovar.keys():
        if key==i:
            print(slovar[i])
        elif key==slovar[i]:
            print(i)
def c():
    print(slovar)
    otsortsp=sorted(slovar)
    res = {}
    for i in otsortsp:
        slovar_element = {i: slovar[i]}
        res.update(slovar_element)
    print(res)
b2()