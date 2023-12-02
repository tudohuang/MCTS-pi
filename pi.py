import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#param
n_points = 500000
points_inside = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# plot
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 1, color='blue', fill=False)
ax.add_artist(circle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# update
def update(frame):
    global points_inside, x_inside, y_inside, x_outside, y_outside
    x, y = np.random.rand(2)
    distance = np.sqrt(x**2 + y**2)

    if distance <= 1:
        points_inside += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

    ax.clear()
    ax.add_artist(circle)
    ax.plot(x_inside, y_inside, 'b.', x_outside, y_outside, 'r.')
    ax.set_title(f'Estimation of Pi: {4 * points_inside / (frame+1):.4f}')


ani = animation.FuncAnimation(fig, update, frames=n_points, repeat=False, interval=1)

plt.show()
