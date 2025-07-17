# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data setup
subjects = ['Data Analytics', 'Cloud Computing', 'Software Development']
years = [f'Year {i}' for i in range(1, 6)]
np.random.seed(42)
data = {
    'Year': years,
    'Data Analytics': [50, 60, 75, 95, 120],
    'Cloud Computing': [30, 55, 80, 100, 130],
    'Software Development': [90, 85, 80, 75, 70]
}
df = pd.DataFrame(data)

# Display the table
print("\n📊 Simulated Student Interests Over 5 Years:\n")
print(df)

# Visualization
plt.figure(figsize=(10, 6))
for subject in subjects:
    plt.plot(df['Year'], df[subject], marker='o', label=subject)

plt.title('Trend in Student Interests Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Number of Students Interested')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()