def fun(type):
    if isinstance(type, list):
        sr_geom = 1
        for i in type:
            sr_geom *= i
        sr_geom = sr_geom ** (1 / len(type))
        return sr_geom
    if isinstance(type, dict):
        sorted_dict = {}
        for i in reversed(sorted(type.values())):
            for k in type.keys():
                if type[k] == i:
                    sorted_dict[k] = type[k]
                    break
        return sorted_dict
    if isinstance(type, int):
        for i in range(2, type):
            if type % i == 0:
                return "Составное"
        return "Простое"
    if isinstance(type, str):
        a = 0
        words = type.split()
        for i in words:
            if len(i) > a:
                a = len(i)
                ind = words.index(i)
        return len(words), words[ind]


print("Выберите какой аргумент будете передавать в функцию:")
print("1-Список из чисел")
print("2-Словарь")
print("3-Число")
print("4-Строку")
while True:
    try:
        choice = int(input("Ваш выбор: "))
        break
    except ValueError:
        print("Введено некорректное значение!")
if choice == 1:
    spis = [5, 8, 12, 39, 45]
    print(fun(spis))
elif choice == 2:
    slovar = {'а': 12, 'б': 54, 'в': 23,
              'г': 1, 'д': 83}
    print(fun(slovar))
elif choice == 3:
    while True:
        try:
            a = int(input("Ваше число: "))
            break
        except ValueError:
            print("Введено некорректное значение!")
    print(fun(a))
elif choice == 4:
    bool = True
    while bool:
        s = input("Введите строку: ")
        bool = s.isspace()
    l, word = fun(s)
    print("Количество слов: ", l, " Длинное слово: ", word)
else:
    print("Введено некорректное значение")
