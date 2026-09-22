import numpy as np

# Marks of 10 students
marks = np.array([78, 65, 82, 90, 55, 72, 88, 60, 75, 95])

# Calculate values
mean = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)
maximum = np.max(marks)
minimum = np.min(marks)

print("Internal Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Maximum:", maximum)
print("Minimum:", minimum)