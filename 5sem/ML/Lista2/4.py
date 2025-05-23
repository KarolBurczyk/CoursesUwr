import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

np.random.seed(1)
X_np = np.random.uniform(-5, 5, 100)
epsilon = np.random.normal(0, 0.5, 100)
y_np = 3 * X_np**3 - 2 * X_np**2 + 5 + epsilon

X = torch.tensor(X_np, dtype=torch.float32).view(-1, 1)
y = torch.tensor(y_np, dtype=torch.float32).view(-1, 1)

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

class PolynomialRegressionModel(nn.Module):
    def __init__(self):
        super(PolynomialRegressionModel, self).__init__()
        self.poly = nn.Linear(3, 1)  # Trzy cechy wejściowe: X, X^2, X^3

    def forward(self, x):
        # x[:, 0] = X, x[:, 1] = X^2, x[:, 2] = X^3
        return self.poly(x)

X_poly = torch.cat([X, X**2, X**3], dim=1)  # [X, X^2, X^3]

def train_model(model, X, y, learning_rate=0.0001, epochs=500):
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)
    losses = []

    for epoch in range(epochs):
        y_pred = model(X)
        loss = criterion(y_pred, y)
        losses.append(loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return losses

linear_model = LinearRegressionModel()
linear_losses = train_model(linear_model, X, y)

poly_model = PolynomialRegressionModel()
poly_losses = train_model(poly_model, X_poly, y)

plt.plot(linear_losses, label="Regresja liniowa")
plt.plot(poly_losses, label="Regresja wielomianowa (3. stopnia)")
plt.xlabel("Epoka")
plt.ylabel("Strata (Loss)")
plt.legend()
plt.title("Porównanie zbieżności strat")
plt.show()

with torch.no_grad():
    y_linear_pred = linear_model(X)
    y_poly_pred = poly_model(X_poly)

sorted_indices = X_np.argsort()
X_sorted = X_np[sorted_indices]
y_poly_sorted = y_poly_pred.numpy()[sorted_indices]

plt.scatter(X_np, y_np, label="Dane rzeczywiste", color="blue")
plt.plot(X_np, y_linear_pred.numpy(), label="Regresja liniowa", color="green", linewidth=2)
plt.plot(X_sorted, y_poly_sorted, label="Regresja wielomianowa", color="red", linewidth=2)

plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Porównanie wyników modeli")
plt.grid()
plt.show()

print("Współczynniki regresji wielomianowej:")
print(f"Waga dla X: {poly_model.poly.weight[0, 0].item()}")
print(f"Waga dla X^2: {poly_model.poly.weight[0, 1].item()}")
print(f"Waga dla X^3: {poly_model.poly.weight[0, 2].item()}")
print(f"Bias: {poly_model.poly.bias.item()}")
