import random


def RandomPesel(gender):
    # birth date
    p1 = random.randint(3, 9)
    p2 = random.randint(0, 9)
    p3 = random.randint(0, 2)
    p4 = random.randint(1, 9)
    p5 = random.randint(0, 1)
    p6 = random.randint(1, 7)
    pesel = str(p1) + str(p2) + str(p3) + str(p4) + str(p5) + str(p6)
    # + random number 000 - 999
    p7 = random.randint(0, 9)
    p8 = random.randint(0, 9)
    p9 = random.randint(0, 9)
    pesel = pesel + str(p7) + str(p8) + str(p9)
    # + gender
    if gender == "w":
        items = [0, 2, 4, 6, 8]
    else:
        items = [1, 3, 5, 7, 9]
    p10 = items[random.randrange(len(items))]
    pesel = pesel + str(p10)
    p11 = (9 * p1) + (7 * p2) + (3 * p3) + (1 * p4) + (9 * p5) + (7 * p6) + (3 * p7) + (1 * p8) + (9 * p9) + (7 * p10)
    p11 = p11 % 10
    pesel = pesel + str(p11)
    return pesel