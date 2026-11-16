import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
Ytr = np.eye(10)[ytr]

rng = np.random.default_rng(0)
W1, b1 = rng.standard_normal((64, 32)) * 0.1, np.zeros(32)
W2, b2 = rng.standard_normal((32, 10)) * 0.1, np.zeros(10)
lr = 0.5

def forward(X):
    h = np.maximum(0, X @ W1 + b1)                 # ReLU
    z = h @ W2 + b2
    z = z - z.max(axis=1, keepdims=True)           # stable softmax
    e = np.exp(z)
    return h, e / e.sum(axis=1, keepdims=True)

for epoch in range(300):
    h, p = forward(Xtr)
    d2 = (p - Ytr) / len(Xtr)                      # backprop
    d1 = (d2 @ W2.T) * (h > 0)
    W2 -= lr * h.T @ d2;   b2 -= lr * d2.sum(0)
    W1 -= lr * Xtr.T @ d1; b1 -= lr * d1.sum(0)
    if epoch % 50 == 0:
        print(epoch, "train acc:", (p.argmax(1) == ytr).mean())

_, p_test = forward(Xte)
print("test acc:", (p_test.argmax(1) == yte).mean())