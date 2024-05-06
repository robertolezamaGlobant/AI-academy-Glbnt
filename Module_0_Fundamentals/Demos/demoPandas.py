import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
students_data = pd.read_csv('0_Module_Fundamentals/students_data.csv')

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(students_data.head())

# Basic statistics
print("\nBasic statistics:")
print(students_data.describe())

# Calculate average score for each subject
average_scores = students_data[['Math', 'Science', 'English']].mean(axis=1)

# Plot average scores
plt.figure(figsize=(10, 6))
average_scores.plot(kind='bar', color='skyblue')
plt.title('Average Scores of Students')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
