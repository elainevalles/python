import numpy as np

Average_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
Average_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)

print("Average min")
print(Average_min)
print("Average max")
print(Average_max)


Calories_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Average_calories_burnage = np.mean(Calories_burnage)
print("Average calories burnage")
print(Average_calories_burnage)