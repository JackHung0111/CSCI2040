# 1155108381 1155110154 
# lab 4 p3

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

# Histogram
plt.figure(1,figsize = (8,8))
random_numbers = np.random.normal(0, 1, 1000)
plt.title("Histogram")
plt.xlabel("Random Numbers")
plt.ylabel("Probability Density")
plt.hist(random_numbers, bins = 100)
plt.savefig("histogram.png")


# Pie chart
plt.figure(2)
# Chung Chi College 3193
# New Asia College 3424
# United College 3324
plt.title("Pie chart")
numbers = [3193,3424,3324]
names = ["CC", "NA", "UC"]
plt.pie(numbers, labels = names, autopct='%1.1f%%')
plt.savefig("pie.png")


# Bar chart
plt.figure(3, figsize = (12,12))
# Chung Chi College 3193
# New Asia College 3424
# United College 3324
# Shaw College 3595
# Morningside College 300
# S.H. Ho College 600
# CW Chu College 300
# Wu Yee Sun College 1258
# Lee Woo Sing College 1322
plt.title("Bar chart")
numbers = [3193,3424,3324,3595,300,600,300,1258,1322]
names = ["CC","NA","UC","SC","Morningside","S.H. Ho","CW Chu","WYS","LWS"]
plt.xlabel("Colleges")
plt.ylabel("Number of Students")
plt.bar(names,numbers)
plt.savefig("bar.png")


# Scatter plot and line chart
plt.figure(4,figsize = (10,10))
x_list = np.linspace(0, 1, 100)
y_list = x_list + np.random.rand(100)
plt.title("Scatter plot")
plt.scatter(x_list, y_list, marker='*', color = 'red', alpha = 0.3)
plt.plot(x_list, x_list, linestyle='dashed')
plt.savefig("scatter_line.png")

