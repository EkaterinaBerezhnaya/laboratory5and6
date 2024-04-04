import random
st = []
for i in range(5):
    ch = random.randint(0, 50)
    st.append(ch)
#print(st)
pch = int(input("Введите число "))
if pch in st:
    print(st, pch, "Поздравляю, Вы угадали число!")
else:
    print(st, pch, "Нет такого числа!")
