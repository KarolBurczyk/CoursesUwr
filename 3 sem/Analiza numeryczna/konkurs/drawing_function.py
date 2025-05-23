# Karol Burczyk
# Za pomocą programu points_getter.py napisanego w pygame uzyskałem wszystkie punkty potrzebne do podrobienia podpisu
# i zapisałem je w signature_data.py w postaci listy.
# Następnie za ich pomocą stworzyłem odpowiednie funkcje nifs3 w function_creator.py i w tym programie narysowałem je za pomocą pyplot.
# W poniższym programie korzystam z punktów zapisanych w signature_data, jednak program points_getter zapisuje wyniki do dane_2, żeby nie nadpisać już
# zebranych punktów.

from signatue_data import s as s_data
from function_creator import get_s
import matplotlib.pyplot as plt

M = 50
tk = [k / M for k in range(M)]
fig, ax = plt.subplots()

points_counter = 0

with open("Data.txt", 'w') as file:
    file.write(f"Punkty tk: \n")
    for t in tk:
        file.write(str(t) + " ")
    file.write(f"\n pary [x, y]: \n")
    for xy in s_data:
        points_counter += len(xy[0])
        x = xy[0]
        y = xy[1]
        for i in range(len(x)):
            s = "[" + str(x[i]) + ', ' + str(y[i]) + ']'
            file.write(s)
        file.write(f'\n')

        ts_data = [k / len(x) for k in range(len(x))]
        sx = get_s(ts_data, x)
        sy = get_s(ts_data, y)

        ax.plot([sx(t) for t in tk], [sy(t) for t in tk], color = 'black', linewidth=1.7)

print("Użyłem", points_counter, "punktów")

ax.set_xlim(0, 2560)
ax.set_ylim(0, 1440)
plt.show()

