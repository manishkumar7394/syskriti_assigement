'''Python Statistics Project

Title: Analysis of Mean, Median, and Mode Using Python
🔹 1. Introduction
# Statistics is an important part of data analysis. Three main measures of central tendency are:
# 	•	Mean – The average value of a dataset
# 	•	Median – The middle value of a dataset
# 	•	Mode – The most frequently occurring value

In this project, we calculate Mean, Median, and Mode using Python in different scenarios.
🔹 2. Objective
# The objective of this project is:
# 	•	To understand the concept of Mean, Median, and Mode
# 	•	To implement them using Python
# 	•	To analyze datasets using built-in and manual methods

🔹 3. Project Implementation

✅ Case 1: Student Marks Analysis
Dataset:'''
marks = [45, 67, 89, 45, 90, 78, 67, 56, 89, 45]

mean = statistics.mean(marks)
median = statistics.median(marks)
mode = statistics.mode(marks)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Output:
	•	Mean = 67.1
	•	Median = 67
	•	Mode = 45
# Analysis:
# The average marks of students is 67.1.
# The most frequently scored marks are 45.

'''✅ Case 2: Employee Salary Analysis'''
salary = [25, 30, 28, 35, 40, 30, 28, 25, 50, 30]

print("Mean Salary:", statistics.mean(salary))
print("Median Salary:", statistics.median(salary))
print("Mode Salary:", statistics.mode(salary))

# Analysis:
# 	•	Mean salary shows the overall average income.
# 	•	Median salary represents the middle income.
# 	•	Mode shows the most common salary value.

# This helps in understanding salary distribution inside an organization.

'''✅ Case 3: Manual Calculation (Without statistics Module)'''
data = [10, 20, 20, 30, 40, 50, 20]

# Mean
mean = sum(data) / len(data)

# Median
sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]

# Mode
frequency = {}
for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

mode = max(frequency, key=frequency.get)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Analysis:

# This method shows how Mean, Median, and Mode are calculated internally without using built-in libraries.

🔹 4. Conclusion

'''In this project, we successfully:
	•	Learned the concept of Mean, Median, and Mode
	•	Implemented them using Python
	•	Applied both built-in and manual methods

These statistical measures are essential in Data Analysis, Machine Learning, and Business Intelligence.'''
