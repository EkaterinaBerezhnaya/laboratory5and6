import random

sp1 = ["Миронов", "Сидорова", "Иванов", "Петров", "Васильева"]
sp2 = ["Кузнецова", "Соколов", "Смирнова", "Михайлов", "Новикова"]
sp3 = []
# пункт а
j = 0
while j < 3:  # по три студента из каждой группы, всего 6
    ind = random.randint(0, 4)
    if sp1[ind] not in sp3:
        sp3.append(sp1[ind])
        j += 1
j = 0
while j < 3:
    ind = random.randint(0, 4)
    if sp2[ind] not in sp3:
        sp3.append(sp2[ind])
        j += 1
kort = tuple(sp3)
print(sp1, sp2, kort, sep="\n")  # пункт b
print(len(kort))  # пункт с
print(tuple(sorted(sp3)))  # пункт d
if "Иванов" in kort:
    print("Студент Иванов входит в полученную команду")
else:
    print("Студент Иванов НЕ входит в полученную команду")
