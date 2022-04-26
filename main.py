def task_2():
    def f(x, y, z, w):
        return not (y <= (x == w)) and (z <= x)

    print('x y z w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if f(x, y, z, w):
                        print(x, y, z, w)


# task_2()
#

# print(hex(15)[2:])
# print(bin(15)[2:])
# print(int('f', 16))


def task_14():
    s = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1
    print(hex(s)[2:].count('0'))


# task_14()

def task_17():
    # data = list(map(int, open('17.txt').read().splitlines()))
    print(max([list(map(int, open('17.txt').read().splitlines()))[i] +
               list(map(int, open('17.txt').read().splitlines()))[i + 1] for i in
               range(len(list(map(int, open('17.txt').read().splitlines()))) - 1) if (
                       list(map(int, open('17.txt').read().splitlines()))[i] % 3 == 0 or
                       list(map(int, open('17.txt').read().splitlines()))[i + 1] % 3 == 0) and
               list(map(int, open('17.txt').read().splitlines()))[i] +
               list(map(int, open('17.txt').read().splitlines()))[i + 1] <= max(
            list(filter(lambda x: x % 3 == 0, list(map(int, open('17.txt').read().splitlines())))))]))
    # max3 = max(list(filter(lambda x: x % 3 == 0, data)))
    # res = [data[i] + data[i+1] for i in range(len(data)-1) if
    #        (data[i] % 3 == 0 or data[i+1] % 3 == 0) and data[i] + data[i+1] <= max3]
    # print(len(res))
    # print(max(res))


# task_17()

def task_22():
    x = 54
    while True:
        x -= 1
        Q = 9
        L = 0
        xc = x
        while xc >= Q:
            L += 1
            xc -= Q
        M = xc
        if M < L:
            M = L
            L = xc
        if L == 4 and M == 5:
            print(x)
            break


# task_22()
def task_23():
    def f(x, y):
        if x == y:
            return 1
        elif x > y:
            return 0
        else:
            return f(x + 1, y) + f(2 * x, y)

    print(f(1, 10) * f(10, 20))


# task_23()
# --------------------------------------------------
def t_1():
    def f(x, y, z, w):
        return not (x and y) and (y or z) or not w

    print('x y z w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if f(x, y, z, w) == 0:
                        print(x, y, z, w)


# t_1()
from itertools import product as easy100


def t_5():
    data = list(easy100('ИГРА', repeat=5))
    count = 0
    for item in data:
        tmp = ''.join(item)
        if tmp.count('А') == 2:
            count += 1
    print(count)


# t_5(
def t_9():
    s = '3' * 250
    while '3333' in s or '7777' in s:
        if '3333' in s:
            s = s.replace('3333', '7', 1)
        else:
            s = s.replace('777', '3', 1)
    print(s)


# t_9()
def t_10():
    print(oct(64 ** 9 + 8 ** 25 - 9)[2:].count('7'))


# t_10()
def t_11():
    def deli(n, m):
        return not (n % m)

    def f(x, A):
        return deli(A, 34) and \
               (deli(283, x) <= ((not deli(A, x)) <= (not deli(120, x))))

    A = 33
    while True:
        A += 1
        for x in range(1, 10000):
            if not f(x, A):
                break
        else:
            print(A)
            break
t_11()