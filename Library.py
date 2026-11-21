# pip :
#     PIP is a kind of package library that we can use to install and manage
#         Python packages.

    # Syntax :
    #     pip install package_name

# Numpy :
#     Numpy presents - Numerical Python.
#     It is use to perform mathemertical operation.
#     To use numpy we need to import it first.

#     Example :

import numpy as np

# Array with numpy library
arr = np.array([10,30,50,40])
print(arr)

print(arr + 5)

arr = arr + 5

print(arr)

# Pandas : 
    # Pandas is a library that use to manage, organize and manipulate data.
    # It provides two data structure :
    #     1. Series : One dimensional data.
    #     2. DataFrame : Two dimensional data.

    # Example :
import pandas as pd

# Creating data frame
data = {
    "Name":["Sourav","Dwij","Shwet","Ankit"],
    "Age":[25,20,21,24],
    "City":["Baroda","Anand","Bharuch","Ahmedabad"]
}

df = pd.DataFrame(data)

print(df)

# Matplot :
    # Matplotlib is a library used for creating visualizations in Python.
    # It provides various functions to plot different types of graphs.

    # Example :
import matplotlib.pyplot as plt

x =[1,2,3,4,5]
y =[10,20,30,40,50]

plt.plot(x,y)
plt.title("Simple example of graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Create data for bar chart
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(categories, values)
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Creating pie chart
labels = ["A", "B", "C", "D"]
sizes = [10, 20, 15, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Simple Pie Chart")
plt.show()