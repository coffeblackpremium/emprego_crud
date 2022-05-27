import random

def generate_ra():
    numbers_ra = 0
    for i in range(0, 7):
        number_random = random.randrange(1000, 200000)
        numbers_ra += int(str(number_random) + str(i))
    return numbers_ra