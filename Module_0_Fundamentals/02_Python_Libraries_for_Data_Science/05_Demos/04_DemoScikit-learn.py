############################################################################################
# Python code example for predicting heart disease using the Scikit-learn library. 
# We'll use the Cleveland Heart Disease dataset from the UCI Machine Learning Repository, 
# which is a popular dataset for this kind of task.

############################################################################################

# Install all necessary labraries
# pip install pandas scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
url = "Module_0_Fundamentals/02_Python_Libraries_for_Data_Science/05_Demos/heart.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())

# Define features (X) and target (y)
X = df.drop('target', axis=1)
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Generate a classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Generate a confusion matrix
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))
