import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('train.csv')

# Display first 5 rows
print(data.head())

# Check missing values
print(data.isnull().sum())

# Fill missing Age values
data['Age'].fillna(data['Age'].median(), inplace=True)

# Survival count
survival_counts = data['Survived'].value_counts()

# Create bar chart
plt.figure(figsize=(6,4))
survival_counts.plot(kind='bar')

# Labels and title
plt.title('Survival Count of Titanic Passengers')
plt.xlabel('Survived')
plt.ylabel('Number of Passengers')

# Show graph
plt.show()
