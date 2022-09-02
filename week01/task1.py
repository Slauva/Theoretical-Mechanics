import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation, PillowWriter

matplotlib.use("TkAgg")


def vector(point):
    b, e = point
    return e - b


metadata = dict(title='Task 1', artist='Matplotlib', comment='Movie support!')
writer = PillowWriter(fps=15, metadata=metadata)

t0, tn, step = -5, 5, 100
T = np.linspace(t0, tn, step)

X = lambda t: 3 * t
Y = lambda t: 4 * (t ** 2) + 1
P = lambda t: np.array([X(t), Y(t)])

V = lambda t: np.array([P(t), P(t) + np.array([3, 8 * t])])
A = lambda t: np.array([P(t), P(t) + np.array([0, 8])])

At = lambda t: np.array([P(t), P(t) + vector(A(t)).dot(vector(V(t))) / vector(V(t)).dot(vector(V(t))) * vector(V(t))])
An = lambda t: np.array([P(t), P(t) + vector(A(t)) - vector(At(t))])

plt.style.use("seaborn")
fig, ax = plt.subplots()
# ax.grid()

parable, = ax.plot([X(i) for i in T], [Y(i) for i in T], 'r', label='y(x)=(4*x^2)/9+1')
point, = ax.plot(1, 1, 'bo')
velocity, = ax.plot([], [], marker='.', label='velocity')
acc, = ax.plot([], [], marker='.', label='acceleration')
acc_t, = ax.plot([], [], marker='.', label='tangential acceleration component')
acc_n, = ax.plot([], [], marker='.', label='normal acceleration component')
hlegend = ax.legend(loc='upper right')


def animate(t):
    px, py = P(t)
    vx, vy = V(t).T
    ax, ay = A(t).T
    atx, aty = At(t).T
    anx, any = An(t).T

    point.set_data(px, py)
    velocity.set_data(vx, vy)
    acc.set_data(ax, ay)
    acc_t.set_data(atx, aty)
    acc_n.set_data(anx, any)

    return parable, point, velocity, acc, acc_t, acc_n


ani = FuncAnimation(fig, animate, frames=T, blit=True, repeat=True, interval=50)

# ani.save("task1.gif", writer=writer)
plt.show()
