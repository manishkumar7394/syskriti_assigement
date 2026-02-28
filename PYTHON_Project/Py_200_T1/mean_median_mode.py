'''Python Code (Without Inbuilt Functions)'''

'''# PY200_T1
# Implementation of Mean, Median, and Mode using basic constructs only'''

# Sample Data
data = [10, 20, 30, 40, 50, 20]

# -------------------------
# MEAN (Average)                        The Mean is the average of all values in a dataset.It tells us the central value of the data
# -------------------------                 
total = 0
count = 0

for num in data:
    total = total + num
    count = count + 1
                                         #  mean formula= (Σx = Sum of all values)/(n = Total number of values)
                                          
 mean = total / count                           
print("Mean:", mean)
                                #  outpur mean = 30



# -------------------------
# MEDIAN                                   The Median is the middle value after arranging the data in ascending order.
# -------------------------

# Step 1: Sort the list manually (Bubble Sort)
n = 0
for i in data:
    n = n + 1

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

# Step 2: Find Median
if n % 2 == 0:
    mid1 = data[n // 2]
    mid2 = data[(n // 2) - 1]
    median = (mid1 + mid2) / 2
else:
    median = data[n // 2]

print("Median:", median)

# -------------------------
# MODE                          the Mode is the value that appears most frequently in the dataset.
# -------------------------
                                # Mode = x_i  such that  f(x_i) is maximum
max_count = 0
mode = None

for i in range(n):
    current = data[i]
    freq = 0
    
    for j in range(n):
        if data[j] == current:
            freq = freq + 1
    
    if freq > max_count:
        max_count = freq
        mode = current

print("Mode:", mode)                    
                            #  output mode = 20

                            