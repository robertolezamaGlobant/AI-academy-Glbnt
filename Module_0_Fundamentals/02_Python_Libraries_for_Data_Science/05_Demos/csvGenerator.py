import csv
import random

# Generate some sample data
num_students = 20
students = []

for i in range(1, num_students + 1):
    student_id = i
    name = f"Student_{i}"
    math_score = random.randint(60, 100)
    science_score = random.randint(60, 100)
    english_score = random.randint(60, 100)
    students.append([student_id, name, math_score, science_score, english_score])

# Write the data to a CSV file
with open('students_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(['Student_ID', 'Name', 'Math', 'Science', 'English'])
    # Write the data
    writer.writerows(students)

print("CSV file generated successfully!")
