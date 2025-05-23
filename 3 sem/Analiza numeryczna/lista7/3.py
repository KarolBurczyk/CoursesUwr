import matplotlib.pyplot as plt
import numpy as np
from math import ceil

# Wielomian
def polynomial(arg, x_list):
    result = 1
    for x in x_list:
        result *= (arg - x)
    return result

# Węzły Czebyszewa w przedziale [-1, 1]
def chebyshev_nodes(n):
    return np.cos((2 * np.arange(1, n + 2) - 1) * np.pi / (2 * (n + 1)))

# Węzły równoodległe w przedziale [-1, 1]
def equidistant_nodes(n):
    return np.linspace(-1, 1, n + 1)

def draw(start, end, in_row):
    figure, axis = plt.subplots(ceil((end-start)/in_row), in_row)

    for n in range(start, end + 1): 
        x_values = np.linspace(-1, 1, 1000)  # Dla płynniejszego wykresu

        # Rysowanie wykresu dla węzłów Czebyszewa
        y_chebyshev = [polynomial(arg, chebyshev_nodes(n)) for arg in x_values]
        axis[(n-start)//in_row, (n-start)%in_row].plot(x_values, y_chebyshev, label=f'Czebyszew, n={n}', linestyle='--')

        # Rysowanie wykresu dla węzłów równoodległych
        y_equidistant = [polynomial(arg, equidistant_nodes(n)) for arg in x_values]
        axis[(n-start)//in_row, (n-start)%in_row].plot(x_values, y_equidistant, label=f'Equidistant, n={n}')

        # Dodanie etykiet i legendy
        axis[(n-start)//in_row, (n-start)%in_row].set_xlabel('x')
        axis[(n-start)//in_row, (n-start)%in_row].set_ylabel('p(x)')
        axis[(n-start)//in_row, (n-start)%in_row].legend()

    plt.show()

 
draw(5, 20, 4)
