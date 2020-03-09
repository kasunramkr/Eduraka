import matplotlib.pylab as plt

x = [1, 3, 6, 9]
y1 = [i * 3 for i in x]
y2 = [i ** 2 for i in x]
plt.plot(x, y1, label="Plot 1")
plt.plot(x, y2, label="Plot 2")
plt.legend()
plt.grid()
plt.xlim(1, 9)
plt.ylim(1, 81)
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.title("My Graph")
plt.savefig("plot.png")
plt.show()
