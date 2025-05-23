import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
X_np = np.random.uniform(-10, 10, 100)
epsilon = np.random.normal(0, 0.1, 100)
y_np = 3 * X_np + 4 + epsilon

X = torch.tensor(X_np, dtype=torch.float32).view(-1, 1)
y = torch.tensor(y_np, dtype=torch.float32).view(-1, 1)

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # Jeden wejściowy, jeden wyjściowy (wejście x, wyjscie pred y)
        # y=w⋅x+b (weight i bias)
    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()
learning_rate = 0.01

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)  # Sochastyczny spadek gradientu na podstawie wag i biasu oraz lr

epochs = 1000
losses = []

for epoch in range(epochs):
    y_pred = model(X)
    
    loss = criterion(y_pred, y)
    losses.append(loss.item())
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over Epochs')
plt.show()

with torch.no_grad():
    predicted = model(X)

plt.scatter(X_np, y_np, label='Dane rzeczywiste', color='blue')
plt.plot(X_np, predicted.numpy(), label='Prosta regresji', color='red', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Dane vs. Model regresji liniowej')
plt.show()

print(f"Współczynnik kierunkowy (slope): {model.linear.weight.item()}")
print(f"Wyraz wolny (intercept): {model.linear.bias.item()}")
