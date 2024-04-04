slovar = {1: "авеинорст",
          2: "дклмпу",
          3: "бгёья",
          4: "йы",
          5: "жзхцч",
          8: "шэю",
          10: "фщъ"}
sl = input("Введите слово ")
suma = 0
for i in range(len(sl)):
    for key in slovar.keys():
        if sl[i] in slovar[key]:
            suma += key

print(suma)
