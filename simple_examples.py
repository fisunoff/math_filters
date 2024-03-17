import matplotlib.pyplot as plt
from math import sin
from filters import *

# Generals variables
length = 30
resolution = 20

# Creating arrays with graphic
sinus_g = [sin(i / resolution) for i in range(length * resolution)]

square_g = [(1 if p > 0 else -1) for p in sinus_g]

triangle_g = []
t = -1
for _ in range(length * resolution):
    t = t+0.035 if t < 1 else -1
    triangle_g.append(t)

# Output of graphs
graphics = [sinus_g, square_g, triangle_g]

fig, axs = plt.subplots(3, 1)

for i in range(len(graphics)):
    noised_f = noised(graphics[i])

    axs[i].plot(noised_f, color='blue')
    axs[i].plot(graphics[i], color='black')
    axs[i].plot(normalise(noised_f), linewidth=3, color='red')

    axs[i].set_ylim([-2, 2]), axs[i].set_xlim([0, length*resolution]),
    axs[i].set_yticklabels([]), axs[i].set_xticklabels([])

plt.show()