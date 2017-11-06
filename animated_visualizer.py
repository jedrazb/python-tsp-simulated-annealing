import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animateTSP(paths, points, num_iters=1):

    print(len(paths))

    fig, ax = plt.subplots()

    x = []
    y = []

    for i in paths[0]:
        x.append(points[i][0])
        y.append(points[i][1])

    extra_x = (max(x) - min(x)) * 0.05
    extra_y = (max(y) - min(y)) * 0.05

    ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
    ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

    plt.plot(x, y, 'co')

    line, = plt.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        x = []; y = []
        x.append(points[paths[frame * 20][-1]][0])
        y.append(points[paths[frame * 20][-1]][1])
        for i in paths[frame * 20]:
            x.append(points[i][0])
            y.append(points[i][1])

        line.set_data(x, y)
        return line

    ani = FuncAnimation(fig, update, frames=(len(paths) // 20), init_func=init, interval=3)

    plt.show()
