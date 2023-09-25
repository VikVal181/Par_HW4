import math


def calc_average(list):
    avr = 0
    for li in list:
        avr += li
    avr = avr / len(list)
    return avr

def calc_product(x, y, Mx, My):
    return (x - Mx) * (y - My)

def calc_product_of_squares(x, y, Mx, My):
    return ((x - Mx)**2) * ((y - My)**2)

# main
import numpy as np
np.random.seed(100)
#создать массив из 50 случайных целых чисел от 0 до 10
x = np.random.randint(0, 15, 50)
#создать положительно коррелированный массив с некоторым случайным шумом
y = x + np.random.normal(0, 10, 50)

Mx = calc_average(x)
My = calc_average(y)

numerator = 0
denominator = 0

for i in range(len(x)):
    numerator += calc_product(x[i], Mx, y[i], My)
    denominator += calc_product_of_squares(x[i], Mx, y[i], My)

if denominator == 0:
    print("ERROR! Denominator = 0")
    exit(1)

rxy = numerator / math.sqrt(denominator)

print("Rxy = ", rxy)