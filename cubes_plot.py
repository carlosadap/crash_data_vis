import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuRd, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=16)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=10)

plt.plot()