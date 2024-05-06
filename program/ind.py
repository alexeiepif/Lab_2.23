#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С использованием многопоточности для
# заданного значения x найти сумму ряда S с
# точностью члена ряда по абсолютному
# значению e=10^-7 и произвести сравнение полученной суммы
# с контрольным значением функции y
# для двух бесконечных рядов.
# Вырианты 9 и 10

import math
from threading import Thread


# 10 V
def sum1(x, eps, s_dict):
    s = 0
    n = 0
    while True:
        k = 2 * n
        term = x**k / math.factorial(k)
        if abs(term) < eps:
            break
        else:
            s += term
            n += 1

    s_dict["s1"] = s


# 9 V
def sum2(x, eps, s_dict):
    s = 0
    n = 0
    while True:
        k = 2 * n + 1
        term = (-1) ** n * x**k / math.factorial(k)
        if abs(term) < eps:
            break
        else:
            s += term
            n += 1

    s_dict["s2"] = s


def main():
    s = {}

    eps = 10**-7
    # 10 V
    x1 = 1 / 2
    y1 = (math.e**x1 + math.e**-x1) / 2
    # 9 V
    x2 = 1.4
    y2 = math.sin(x2)

    thread1 = Thread(target=sum1, args=(x1, eps, s))
    thread2 = Thread(target=sum2, args=(x2, eps, s))

    # Запуск потоков
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков
    thread1.join()
    thread2.join()

    s1 = s["s1"]
    s2 = s["s2"]

    print(
        f"Сумма 10 Варианта: {s1},"
        f" Ожидаемое значение y1: {y1}, Разница: {abs(s1 - y1)}"
    )
    print(
        f"Сумма 9 Варианта: {s2},"
        f" Ожидаемое значение y2: {y2}, Разница: {abs(s2 - y2)}"
    )


if __name__ == "__main__":
    main()
