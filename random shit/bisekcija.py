def f(x):
    return 3*x**2 + 2*x - 10


def bisekcija(a, b, funkcija, st_korakov):
    c = (a + b)/2
    for i in range(0, st_korakov):
        if funkcija(a) > 0 > funkcija(c) or funkcija(a) < 0 < funkcija(c):
            b = c
            c = (a + c)/2
        elif funkcija(b) > 0 > funkcija(c) or funkcija(b) < 0 < funkcija(c):
            a = c
            c = (b + c)/2

    return c

print(bisekcija(-3, -1, f, 10))
