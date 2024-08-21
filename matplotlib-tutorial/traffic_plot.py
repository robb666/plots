import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def plot_learning_curve(x, costs, filename=None):
    fig = plt.figure(figsize=(10, 5))

    ax = fig.add_subplot(111, label='1')

    costs = -costs
    N = len(costs)
    running_avg = np.empty(N)
    for t in range(N):
        running_avg[t] = np.mean(costs[max(0, t - 100):(t + 1)])

    ax.scatter(x, running_avg, color='C1', s=6)

    ax.axes.get_xaxis().set_visible(True)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    ax.yaxis.tick_right()
    ax.set_ylabel('current_cost', color='C1')
    ax.yaxis.set_label_position('right')
    ax.tick_params(axis='y', colors='C1')

    if filename:
        plt.savefig(filename)

    plt.grid(True, which='both', axis='both', color='grey', linestyle='--', linewidth=0.4)
    ax.grid(True, which='both', axis='x', color='grey', linestyle='--', linewidth=0.4)

    plt.show()


costs = np.array([3935, 2733, 5724, 8840, 1003, 15859, 2415, 3825, 4243, 2728, 2394, 5100, 4039, 28677, 5026, 20885, 7623, 1427, 1713, 2995, 4335, 13817, 16108, 4814, 4027, 8297, 5824, 5942, 8456, 3345, 3220, 6520, 3121, 1439, 23920, 1851, 9828, 7023, 12647, 1107, 1201, 3674, 2153, 20612, 2271, 2597, 7971, 1237, 4328, 3773, 5528, 2267, 15519, 8984, 11579, 7615, 1820, 3076, 6038, 3959, 8274, 3346, 24783, 2277, 6524, 2066, 12808, 5510, 11840, 1473, 3065, 6480, 1982, 1046, 1847, 6884, 1070, 1763, 2259, 19333, 3216, 1797, 10240, 2083, 1196, 6387, 3415, 6167, 2323, 2453, 4109, 1006, 2234, 3259, 2979, 3060, 5071, 5101, 3003, 9518, 2190, 5020, 2051, 3198, 1123, 2218, 7295, 2942, 735, 17191, 3334, 2139, 6999, 727, 9305, 5007, 11079, 5118, 16651, 11235, 2979, 6067, 361, 5679, 2238, 16920, 5175, 1540, 3358, 3370, 3203, 1845, 2198, 2320, 7476, 1211, 7510, 1332, 15918, 1549, 9269, 3111, 4243, 3289, 6328, 4864, 2244, 1559, 2696, 5366, 8463, 6896, 4404, 1892, 2857, 5644, 981, 11910, 2538, 4425, 3641, 1307, 3422, 3210, 2050, 5095, 6024, 2936, 1327, 6478, 2560, 4782, 2426, 895, 3800, 17444, 2756, 5435, 2575, 2949, 7549, 5, 1711, 3382, 4424, 8964, 5508, 3411, 3389, 1793, 5081, 7711, 7603, 3306, 4574, 751, 2631, 1023, 1535, 2859, 4759, 2830, 12978, 2688, 1958, 6319, 5011, 3341, 4498, 15406, 2690, 2963, 24760, 3167, 1177, 3584, 1097, 1675, 14305, 3728, 28176, 2828, 7640])
x = np.arange(len(costs))
time = 123
print(x)


plot_learning_curve(x, costs, 'plot_traffic.jpeg')