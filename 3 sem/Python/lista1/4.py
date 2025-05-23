import random
from math import *

rzuty = 1000000
target = 0
for i in range(rzuty):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    if sqrt(pow(x - 5, 2) + pow(y - 5, 2)) <= 5:
        target += 1

print("Trafione: ", target)
print("W sumie rzutow: ", rzuty)
print((4 * target) / rzuty)

        