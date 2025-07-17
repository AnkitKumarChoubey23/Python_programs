import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Generate synthetic dataset (dots, stars, triangles)
np.random.seed(42)
X = np.random.rand(30, 2) * 10  # 30 points in 2D space
y = np.random.choice(["dot", "star", "triangle"], size=30)  # Assign classes

# Convert labels to numbers (dot=0, star=1, triangle=2)
label_map = {"dot": 0, "star": 1, "triangle": 2}
y_numeric = np.array([label_map[label] for label in y])

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y_numeric)

# Generate a grid for visualization
xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
grid_points = np.c_[xx.ravel(), yy.ravel()]
predictions = knn.predict(grid_points).reshape(xx.shape)

# Plot decision boundaries
plt.contourf(xx, yy, predictions, alpha=0.3, cmap='coolwarm')
plt.scatter(X[:, 0], X[:, 1], c=y_numeric, edgecolors='k', s=100, cmap='coolwarm')

# Mark classes
for i, txt in enumerate(y):
    plt.annotate(txt, (X[i, 0], X[i, 1]), fontsize=9, ha='right')

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("KNN Classification (Dots, Stars, Triangles)")
plt.show()
