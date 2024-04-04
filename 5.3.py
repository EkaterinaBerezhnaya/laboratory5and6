kort=("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
koldney=int(input("Введите желаемое количество выходных "))
rabdni=7-koldney
spv=[]
sprab=[]
for i in range(rabdni):
    sprab.append(kort[i])
for i in range(len(kort)):
    if kort[i] not in sprab:
        spv.append(kort[i])
print("Ваши выходные дни: ", spv)
print("Ваши рабочие дни: ", sprab)
