import pandas as pd
import numpy as np
# import tensorflow as tf

# Load the dataset
students_data = pd.read_csv('students_data.csv')

# Convert DataFrame to NumPy array
scores_array = students_data[['Math', 'Science', 'English']].values

# Calculate the average mean score per student using NumPy
average_mean_per_student = np.mean(scores_array, axis=1)

# Add the average mean per student as a new column in the DataFrame
students_data['Average'] = average_mean_per_student

# Display the updated DataFrame
print(students_data)

# Calculate the overall average mean score for all students using TensorFlow
# overall_average_mean = tf.reduce_mean(average_mean_per_student)

# Start a TensorFlow session to evaluate the tensor
# with tf.compat.v1.Session() as sess:
#     overall_average_mean_value = sess.run(overall_average_mean)

# print("\nOverall Average Mean Score for all students:", overall_average_mean_value)
