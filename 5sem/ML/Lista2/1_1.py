import torch
import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z):
    return -(x**2) - (y**2) - (z**2) + 2*x*y - y*z + 3*z

x = torch.tensor([0.0], requires_grad=True)
y = torch.tensor([0.0], requires_grad=True)
z = torch.tensor([0.0], requires_grad=True)

learning_rate = 0.3
iterations = 1000

values = []

for _ in range(iterations):
    value = f(x, y, z)
    value.backward()

    with torch.no_grad():
        x += learning_rate * x.grad
        y += learning_rate * y.grad
        z += learning_rate * z.grad

        x.grad.zero_()
        y.grad.zero_()
        z.grad.zero_()

    values.append((x.item(), y.item(), z.item()))

values = np.array(values)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(values[:, 0], values[:, 1], values[:, 2], marker='o', label='Ścieżka optymalizacji')
ax.scatter(values[-1, 0], values[-1, 1], values[-1, 2], color='red', label='maksimum', s=100)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Trajektoria optymalizacji gradient ascent')
ax.legend()
plt.show()
