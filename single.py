import matplotlib.pyplot as plt
import random

style = random.choice(plt.style.available)
plt.style.use(style)
fig, ax = plt.subplots()

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()