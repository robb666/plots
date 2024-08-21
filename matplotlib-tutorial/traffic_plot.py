import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(x, costs, filename=None):
    fig = plt.figure(figsize=(10, 5))

    x = np.array(x)

    ax = fig.add_subplot(111, label='1')
    ax2 = fig.add_subplot(111, label='2', frame_on=False)

    # ax.plot(x, epsilons, color='C0')
    # ax.set_xlabel(f'Training episodes | Total steps: {steps} | Time: {time} min.', color='C0')
    ax.set_ylabel('Epsilon', color='C0')
    ax.tick_params(axis='x', colors='C0')
    ax.tick_params(axis='y', colors='C0')

    costs = -costs
    N = len(costs)
    running_avg = np.empty(N)
    for t in range(N):
        running_avg[t] = np.mean(costs[max(0, t-100):(t+1)])

    ax2.scatter(x, running_avg, color='C1', s=6)
    ax2.axes.get_xaxis().set_visible(False)
    ax2.yaxis.tick_right()
    ax2.set_ylabel('current_cost', color='C1')
    ax2.yaxis.set_label_position('right')
    ax2.tick_params(axis='y', colors='C1')

    # if termination:
    # ax2.scatter(x[termination == 1], termination[termination == 1], c='r', s=2, label='terminated')
    # plt.legend(loc='lower left')

    if filename:
        plt.savefig(filename)

    plt.grid(True, which='both', axis='both', color='grey', linestyle='--', linewidth=0.4)
    ax.grid(True, which='both', axis='x', color='grey', linestyle='--', linewidth=0.4)
    plt.show()


# x = np.linspace(0, 100, 100)
# costs = np.linspace(100, 0, 100)

# print(termination)
# #
#



costs = np.array([3935, 2733, 5724, 8840, 1003, 15859, 2415, 3825, 4243, 2728, 2394, 5100, 4039, 28677, 5026, 20885, 7623, 1427, 1713, 2995, 4335, 13817, 16108, 4814, 4027, 8297, 5824, 5942, 8456, 3345, 3220, 6520, 3121, 1439, 23920, 1851, 9828, 7023, 12647, 1107, 1201, 3674, 2153, 20612, 2271, 2597, 7971, 1237, 4328, 3773, 5528, 2267, 15519, 8984, 11579, 7615, 1820, 3076, 6038, 3959, 8274, 3346, 24783, 2277, 6524, 2066, 12808, 5510, 11840, 1473, 3065, 6480, 1982, 1046, 1847, 6884, 1070, 1763, 2259, 19333, 3216, 1797, 10240, 2083, 1196, 6387, 3415, 6167, 2323, 2453, 4109, 1006, 2234, 3259, 2979, 3060, 5071, 5101, 3003, 9518, 2190, 5020, 2051, 3198, 1123, 2218, 7295, 2942, 735, 17191, 3334, 2139, 6999, 727, 9305, 5007, 11079, 5118, 16651, 11235, 2979, 6067, 361, 5679, 2238, 16920, 5175, 1540, 3358, 3370, 3203, 1845, 2198, 2320, 7476, 1211, 7510, 1332, 15918, 1549, 9269, 3111, 4243, 3289, 6328, 4864, 2244, 1559, 2696, 5366, 8463, 6896, 4404, 1892, 2857, 5644, 981, 11910, 2538, 4425, 3641, 1307])
x = np.arange(len(costs))

# eps = np.random.standard_normal(x)
# termination = np.random.choice([False], size=x)
# steps = 110_000
time = 123

print(x)





plot_learning_curve(x, costs)