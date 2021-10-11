a1 = int(input('a = '))
b1 = int(input('b = '))

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)

gcd(a1, b1)
