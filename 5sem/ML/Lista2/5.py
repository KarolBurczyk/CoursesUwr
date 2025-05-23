import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Tworzenie danych
np.random.seed(2)
X_np = np.random.uniform(-10, 10, 150)
epsilon = np.random.normal(0, 1, 150)
y_np = 2 * X_np**2 + 3 * X_np + 1 + epsilon

learning_rate = 0.001
epochs = 1000

split_idx = int(0.8 * len(X_np))
indices = np.random.permutation(len(X_np))
train_idx, val_idx = indices[:split_idx], indices[split_idx:]

X_train_np, y_train_np = X_np[train_idx], y_np[train_idx]
X_val_np, y_val_np = X_np[val_idx], y_np[val_idx]

X_train = torch.tensor(X_train_np, dtype=torch.float32).view(-1, 1)
y_train = torch.tensor(y_train_np, dtype=torch.float32).view(-1, 1)
X_val = torch.tensor(X_val_np, dtype=torch.float32).view(-1, 1)
y_val = torch.tensor(y_val_np, dtype=torch.float32).view(-1, 1)

def polynomial_features(X, degree):
    return torch.cat([X**i for i in range(1, degree + 1)], dim=1)

class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, 1)
    def forward(self, x):
        return self.linear(x)

def train_model(model, X_train, y_train, X_val, y_val, learning_rate, epochs, l2_reg=0.0):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=l2_reg)

    
    train_losses = []
    val_losses = []
    
    for epoch in range(epochs):
        y_pred = model(X_train)
        train_loss = criterion(y_pred, y_train)
        
        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()
        
        with torch.no_grad():
            y_val_pred = model(X_val)
            val_loss = criterion(y_val_pred, y_val)
        
        train_losses.append(train_loss.item())
        val_losses.append(val_loss.item())
    
    return train_losses, val_losses

linear_model = LinearRegressionModel(input_dim=1)
train_losses_lin, val_losses_lin = train_model(
    linear_model, X_train, y_train, X_val, y_val, learning_rate, epochs
)

degree = 10
X_train_poly = polynomial_features(X_train, degree)
X_val_poly = polynomial_features(X_val, degree)
poly_model = LinearRegressionModel(input_dim=degree)
train_losses_poly, val_losses_poly = train_model(
    poly_model, X_train_poly, y_train, X_val_poly, y_val, learning_rate, epochs
)

poly_model_l2 = LinearRegressionModel(input_dim=degree)
train_losses_poly_l2, val_losses_poly_l2 = train_model(
    poly_model_l2, X_train_poly, y_train, X_val_poly, y_val, learning_rate, epochs, l2_reg=0.9,
)

plt.figure(figsize=(12, 6))
plt.plot(train_losses_lin, label="Trenowanie - liniowa", color="blue")
plt.plot(val_losses_lin, label="Walidacja - liniowa", color="blue", linestyle="dashed")
plt.plot(train_losses_poly, label="Trenowanie - wielomian", color="green")
plt.plot(val_losses_poly, label="Walidacja - wielomian", color="green", linestyle="dashed")
plt.plot(train_losses_poly_l2, label="Trenowanie - wielomian (L2)", color="red")
plt.plot(val_losses_poly_l2, label="Walidacja - wielomian (L2)", color="red", linestyle="dashed")
plt.xlabel("Epoka")
plt.ylabel("Strata")
plt.title("Porównanie strat treningowych i walidacyjnych")
plt.legend()
plt.grid()
plt.show()

with torch.no_grad():
    X_plot = np.linspace(-10, 10, 200)
    X_plot_tensor = torch.tensor(X_plot, dtype=torch.float32).view(-1, 1)
    X_plot_poly = polynomial_features(X_plot_tensor, degree)
    
    y_pred_lin = linear_model(X_plot_tensor)
    y_pred_poly = poly_model(X_plot_poly)
    y_pred_poly_l2 = poly_model_l2(X_plot_poly)

plt.figure(figsize=(12, 6))
plt.scatter(X_np, y_np, label="Dane rzeczywiste", color="blue", alpha=0.6)
plt.plot(X_plot, y_pred_lin.numpy(), label="Regresja liniowa", color="orange", linewidth=2)
plt.plot(X_plot, y_pred_poly.numpy(), label="Regresja wielomianowa", color="green", linewidth=2)
plt.plot(X_plot, y_pred_poly_l2.numpy(), label="Regresja wielomianowa (L2)", color="red", linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Modele regresji")
plt.legend()
plt.grid()
# plt.ylim(0, 300)
plt.show()
