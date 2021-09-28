import matplotlib.pyplot as plt
import random
input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

style = random.choice(plt.style.available)
plt.style.use(style)

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#Set Chart title and label axes.
ax.set_title("Square numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()