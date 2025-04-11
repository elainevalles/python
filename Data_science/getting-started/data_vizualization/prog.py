import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for headless environments

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the CSV with full path
full_health_data = pd.read_csv("/home/eparra-v/Documents/Python/Data_science/getting-started/data_vizualization/data.csv", header=0, sep=",")

# Independent and dependent variables
x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

# Linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x_val):
    return slope * x_val + intercept

mymodel = list(map(myfunc, x))

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y)
plt.plot(x, mymodel, color='red')
plt.ylim(0, 2000)
plt.xlim(0, 200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.title("Pulse vs Calorie Burnage")

# Save the chart to a file
plt.savefig("output.png")  # Will be saved in the current working directory
