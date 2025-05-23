import math
x = [0, 2, 4, 6, 8, 10]
y = [1, 1.6, 1.4, 0.6, 0.2, 0.8]

s = 0
for i in range(6):
    s = s + math.cos((2*math.pi*x[i])/12)*y[i]
    # print(round(14/15 + (math.sqrt(3)/3)*math.sin((2*math.pi*x[i])/12) + (4/15)*math.cos((2*math.pi*x[i])/12), 10), y[i])

print(s)
