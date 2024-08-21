import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def plot_learning_curve(x, costs, score, steps, time, filename=None):
    fig = plt.figure(figsize=(10, 5))

    ax = fig.add_subplot(111, label='1')
    ax2 = fig.add_subplot(111, label='2', frame_on=False)

    ax2.plot(x, score, color='g')
    ax2.set_xlabel(f'Training episodes \u2191 | Total steps: {steps} | Time: {time} min.', color='black')
    ax2.set_ylabel('Score', color='g')
    ax2.tick_params(axis='x', colors='black')
    ax2.tick_params(axis='y', colors='g')

    costs = -costs
    N = len(costs)
    running_avg = np.empty(N)
    for t in range(N):
        running_avg[t] = np.mean(costs[max(0, t - 100):(t + 1)])

    ax.scatter(x, running_avg, color='C1', s=6)

    ax.axes.get_xaxis().set_visible(False)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    ax.yaxis.tick_right()
    ax.set_ylabel('Current Cost', color='C1')
    ax.yaxis.set_label_position('right')
    ax.tick_params(axis='y', colors='C1')

    # if filename:
    #     plt.savefig(filename)

    plt.grid(True, which='both', axis='both', color='grey', linestyle='--', linewidth=0.4)
    ax.grid(True, which='both', axis='x', color='grey', linestyle='--', linewidth=0.4)

    plt.show()


costs = np.array([3051, 4082, 4248, 1824, 12637, 2719, 4843, 12590, 4823, 2261, 11698, 11610, 2502, 14366, 4855, 16492, 1091, 3904])
score = np.array([5883, 4260, 4620, 7324, -3092, 5806, 4229, -4451, 4430, 9712, -5585, -3724, 5137, -6459, 3251, -10426, 6856, 5018])
x = np.arange(len(costs))
steps = '446 332'
time = '199'
print(x)


plot_learning_curve(x, costs, score, steps,  time)
