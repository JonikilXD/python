def hw2():
    x = int(input("Введите число от 3 до 23\n"))
    y = int(input("Введите число от 3 до 23\n"))
    znak = input("Введите операцию +,-,*,/\n")

    q = {
        "+": (x + y),
        "-": (x - y),
        "*": (x * y),
        "/": (x // y),
    }
    if (x in range(3, 24)) and (y in range(3, 24)):
        print(q.get(znak, None))
    else:
        print("Вне диапозона")


def hw3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [a[i] for i in range(len(a)) if a[i] < 5]
    print(b)


def hw4():
    choise = input('''
    Введите площадь какой фигуры хотите найти
    1 - Прямоугольник
    2 - треугольник
    3 - круг
    ''')

    def pram():
        x = int(input("Введите длину прямоугольника\n"))
        y = int(input("Введите ширину прямоугольника\n"))
        z = x * y
        return z

    def treu():
        a = int(input("Введите 1 сторону треугольника\n"))
        b = int(input("Введите 2 сторону треугольника\n"))
        c = int(input("Введите 3 сторону треугольника\n"))
        pol = (a + b + c) // 2
        z = (pol * (pol - a) * (pol - b) * (pol - c)) ** 0.5
        return z

    def krug():
        x = int(input("Введите радиус круга\n"))
        z = 3.14 * x * 2
        return z

    if choise == "1":
        print(pram())
    elif choise == "2":
        print(treu())
    elif choise == "3":
        print(krug())
    else:
        print("Нет такого пункта")


def hw5():
    number = input("Введите число\n")
    q = 0
    for i in range(len(number)):
        x = int(number[i])
        q = q + x
    print(q)


def hw6():
    x = int(input("Введите число\n"))
    y = int(input("Введите число\n"))
    z = 0
    while x or y > 0:
        if x > y > 0:
            x = x - y
            z = x
        elif y > x > 0:
            y = y - x
            z = y
        else:
            break
    print("НОД этих чисел", z)


def hw7():
    def bank(a, years):
        for i in range(years):
            a = a + (a * 0.1)
        return a

    print(f"Ваш счет",bank(1000, 15))

