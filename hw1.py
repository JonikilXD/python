def hw1decorator(type):
    def tata(func):
        def toto(*args, **kwargs):
            def a(arg1, arg2):
                if arg1 and arg2 is int:
                    print("Тот же тип")
                    return arg1, arg2
                elif arg1 and arg2 is str:
                    arg1 = hash(arg1)
                    arg2 = hash(arg2)
                    print("Первое значение", arg1)
                    print("Второе значение", arg2)
                    return arg1, arg2
                elif arg1 and arg2 is float:
                    arg1 = int(arg1)
                    arg2 = int(arg2)
                    print("Первое значение", arg1)
                    print("Второе значение", arg2)
                    return arg1, arg2
                elif arg1 and arg2 is tuple:
                    for i in range(len(arg1)):
                        if arg1[i] is int:
                            return arg1[i]
                        elif arg1[i] is str:
                            arg1[i] = hash(arg1[i])
                            return arg1[i]
                        elif arg1[i] is float:
                            arg1[i] = int(arg1)
                            return arg1[i]
                    for i in range(len(arg2)):
                        if arg2[i] is int:
                            return arg2[i]
                        elif arg2[i] is str:
                            arg2[i] = hash(arg2[i])
                            return arg2[i]
                        elif arg2[i] is float:
                            arg2[i] = int(arg2)
                            return arg2[i]
                elif arg1 and arg2 is list:
                    for i in range(len(arg1)):
                        if arg1[i] is int:
                            return arg1[i]
                        elif arg1[i] is str:
                            arg1[i] = hash(arg1[i])
                            return arg1[i]
                        elif arg1[i] is float:
                            arg1[i] = int(arg1)
                            return arg1[i]
                    for i in range(len(arg2)):
                        if arg2[i] is int:
                            return arg2[i]
                        elif arg2[i] is str:
                            arg2[i] = hash(arg2[i])
                            return arg2[i]
                        elif arg2[i] is float:
                            arg2[i] = int(arg2)
                            return arg2[i]

            def b(arg1, arg2):
                if arg1 and arg2 is int:
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    print("Первое значение", arg1)
                    print("Второе значение", arg2)
                    return arg1, arg2
                elif arg1 and arg2 is str:
                    arg1 = float(hash(arg1))
                    arg2 = float(hash(arg2))
                    print("Первое значение", arg1)
                    print("Второе значение", arg2)
                    return arg1, arg2
                elif arg1 and arg2 is float:
                    print("Тот же тип")
                    return arg1, arg2
                elif arg1 and arg2 is tuple:
                    for i in range(len(arg1)):
                        if arg1[i] is int:
                            arg1[i] = float(arg1[i])
                            return arg1[i]
                        elif arg1[i] is str:
                            arg1[i] = float(hash(arg1[i]))
                            return arg1[i]
                        elif arg1[i] is float:
                            return arg1[i]
                    for i in range(len(arg2)):
                        if arg2[i] is int:
                            arg2[i] = float(arg2[i])
                            return arg2[i]
                        elif arg2[i] is str:
                            arg2[i] = float(hash(arg2[i]))
                            return arg2[i]
                        elif arg2[i] is float:
                            return arg2[i]
                elif arg1 and arg2 is list:
                    for i in range(len(arg1)):
                        if arg1[i] is int:
                            arg1[i] = float(arg1[i])
                            return arg1[i]
                        elif arg1[i] is str:
                            arg1[i] = float(hash(arg1[i]))
                            return arg1[i]
                        elif arg1[i] is float:
                            return arg1[i]
                    for i in range(len(arg2)):
                        if arg2[i] is int:
                            arg2[i] = float(arg2[i])
                            return arg2[i]
                        elif arg2[i] is str:
                            arg2[i] = float(hash(arg2[i]))
                            return arg2[i]
                        elif arg2[i] is float:
                            return arg2[i]

            def c(arg1, arg2):
                if arg1 and arg2 is int:
                    arg1 = str(arg1)
                    arg2 = str(arg2)
                    print("Первое значение", arg1)
                    print("Второе значение", arg2)
                    return arg1, arg2
                elif arg1 and arg2 is str:
                    return arg1, arg2
                elif arg1 and arg2 is float:
                    arg1 = str(arg1)
                    arg2 = str(arg2)
                    print("Первое значение", arg1)
                    print("Второе значение", arg2)
                    return arg1, arg2
                elif arg1 and arg2 is tuple:
                    for i in range(len(arg1)):
                        if arg1[i] is int:
                            arg1[i] = str(arg1[i])
                            return arg1[i]
                        elif arg1[i] is str:
                            return arg1[i]
                        elif arg1[i] is float:
                            arg1[i] = str(arg1[i])
                            return arg1[i]
                    for i in range(len(arg2)):
                        if arg2[i] is int:
                            arg2[i] = str(arg2[i])
                            return arg2[i]
                        elif arg2[i] is str:
                            return arg2[i]
                        elif arg2[i] is float:
                            arg2[i] = str(arg2[i])
                            return arg2[i]
                elif arg1 and arg2 is list:
                    for i in range(len(arg1)):
                        if arg1[i] is int:
                            arg1[i] = str(arg1[i])
                            return arg1[i]
                        elif arg1[i] is str:
                            return arg1[i]
                        elif arg1[i] is float:
                            arg1[i] = str(arg1[i])
                            return arg1[i]
                    for i in range(len(arg2)):
                        if arg2[i] is int:
                            arg2[i] = str(arg2[i])
                            return arg2[i]
                        elif arg2[i] is str:
                            return arg2[i]
                        elif arg2[i] is float:
                            arg2[i] = str(arg2[i])
                            return arg2[i]

            def d(arg1, arg2):
                if arg1 and arg2 is int:
                    arg1 = []
                    arg2 = []
                    return arg1, arg2
                elif arg1 and arg2 is str:
                    arg1 = []
                    arg2 = []
                    return arg1, arg2
                elif arg1 and arg2 is float:
                    arg1 = []
                    arg2 = []
                    return arg1, arg2
                elif arg1 and arg2 is tuple:
                    v = None
                    z = None
                    arg1 = v
                    arg2 = z
                    arg1 = (v)
                    arg2 = (z)
                    return arg1, arg2
                elif arg1 and arg2 is list:
                    return arg1, arg2

            def e(arg1, arg2):
                if arg1 and arg2 is int:
                    arg1 = ()
                    arg2 = ()
                    return arg1, arg2
                elif arg1 and arg2 is str:
                    arg1 = ()
                    arg2 = ()
                    return arg1, arg2
                elif arg1 and arg2 is float:
                    arg1 = ()
                    arg2 = ()
                    return arg1, arg2
                elif arg1 and arg2 is tuple:
                    return arg1, arg2
                elif arg1 and arg2 is list:
                    v = None
                    z = None
                    arg1 = v
                    arg2 = z
                    arg1 = (v)
                    arg2 = (z)
                    return arg1, arg2

            pool = {
                "int": a(*args, **kwargs),
                "float": b(*args, **kwargs),
                "str": c(*args, **kwargs),
                "tuple": d(*args, **kwargs),
                "list": e(*args, **kwargs),
            }
            pool.get(type, None)
            func(*args, **kwargs)

        return toto

    return tata


@hw1decorator("int")
def agg(n, m):
    print(n + m)


def generator(n):
    """Выводит числа Фибоначи в n диапазоне"""
    pool = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        pool[i] = pool[i - 1] + pool[i - 2]
        yield pool[i]
        i += i


val = generator(30)
print(next(val))


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("Точка создана", self.x, self.y, self.z)

    def ras(self):
        if self.x == self.y:
            self.dio = self.x ** 0.5
        else:
            self.dio = (self.x ** 2 + self.y ** 2)**0.5
        self.ras = (self.dio ** 2 + self.z ** 2)**0.5
        return print(self.ras)

    def razm(self):
        print("Теорема Пифагора c = (a**2 + b**2)**0.5")


class straight:

    def __init__(self, A, B):
        self.A = A
        self.B = B
        print(A[0])
        print(B[0])

    def ras(self):
        if self.A[0] > self.B[0]:
            self.raz = self.A[0] - self.B[0]
        else:
            self.raz = self.B[0] - self.A[0]
        if self.A[1] > self.B[1]:
            self.raz1 = self.A[1] - self.B[1]
        else:
            self.raz1 = self.B[1] - self.A[1]
        if self.A[2] > self.B[2]:
            self.raz2 = self.A[2] - self.B[2]
        else:
            self.raz2 = self.B[2] - self.A[2]
        self.dio = (self.raz ** 2 + self.raz1 ** 2)**0.5
        self.ras = (self.dio ** 2 + self.raz2 ** 2)**0.5
        return print(f"Длинна {self.ras} см")

    def perenos(self):
        for i in range(3):
            self.B[i] -= self.A[i]
            self.A[i] -= self.A[i]
        return print("точка", self.A, self.B)


p = Point(4, 6, 8)
p.ras()
p.razm()

s = straight([5, 9, 4], [9, 15, 24])
s.ras()
s.perenos()