import pandas as pd

# Load CSV file
file = 'student_activity_data.csv'

# Read dataset
students = pd.read_csv(file)

# Productivity score calculation
students['productivity_score'] = (
    students['study_hours'] * 10 +
    students['attendance_percentage'] * 0.3 +
    students['assignments_completed'] * 5 -
    students['mobile_usage_hours'] * 2
)

# Stress level logic
stress_level = []

for sleep in students['sleep_hours']:
    if sleep < 5:
        stress_level.append('High')
    elif sleep < 7:
        stress_level.append('Medium')
    else:
        stress_level.append('Low')

students['stress_level'] = stress_level

# Sort students by productivity
students = students.sort_values(by='productivity_score', ascending=False)

# Display results
print(students[['name', 'productivity_score', 'stress_level']])

# Save analyzed data
students.to_csv('final_student_analysis.csv', index=False)

print('\nAnalysis completed successfully.')