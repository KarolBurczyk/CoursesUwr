import torch
import matplotlib.pyplot as plt

def f(x):
    return -(x**4) + 4*x**2 - 2*x + 1

x = torch.tensor([0.0], requires_grad=True)
learning_rate = 0.01
iterations = 50

values = []

for _ in range(iterations):
    y = f(x)
    y.backward()
    with torch.no_grad():
        x += learning_rate * x.grad
        x.grad.zero_()
    values.append(y.item())

plt.figure(figsize=(8, 5))
plt.plot(values, label="Wartość funkcji $f(x)$")
plt.xlabel("Iteracja")
plt.ylabel("$f(x)$")
plt.legend()
plt.grid()
plt.show()
