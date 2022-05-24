# Mithen

import time


def kare(x):
    return int(x ** 2) if int(x) == x else x ** 2


def karekok(x):
    return int(x ** (1/2)) if int(x) == x else x ** (1/2)


def kup(x):
    return int(x ** 3) if int(x) == x else x ** 3


def kupkok(x):
    return int(x ** (1/3)) if int(x) == x else x ** (1/3)


def mutlak(x):
    return abs(int(x)) if int(x) == x else abs(x)


def us(x, y):
    return int(x ** y) if isinstance(x, int) else x ** y


def bekle(x: float):
    time.sleep(x)
