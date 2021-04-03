import numpy as np

class Triplet_Generator():
    def __init__(self, seed=None):
        self.n = seed

    def __next__(self):
        return (- self.N + self.t**2, 2*self.t*self.n, self.N + self.t**2)

    def __iter__(self):
        if self.n is None:
            self.n = np.random.randint(0,100000, dtype=np.int64)

        # NOTE: starting from t = 0 will generate also triplets with negative integers (triplets in the first two
        # quadrants of the 2D-plane). Starting from t = n the first triplet is trivial (of the type 0 + k^2 = k^2).
        # Starting from t = n + 1 all the triplets are in the first quadrant.
        self.t = self.n + 0
        self.N = np.power(self.n, 2)

        while True:
            yield self.__next__()
            self.t += 1


    def random(self):
        self.t = np.random.randint(0, 100000, dtype=np.int64)
        self.n = np.random.randint(0, 100000, dtype=np.int64)
        self.N = np.power(self.n, 2)
        return self.__next__()



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()

    fig, ax = plt.subplots(figsize=(16, 9))

    for seed in range(1, 15):
        points = []
        i = 0
        pyt_gen = Triplet_Generator(seed=seed)
        for a, b, c in pyt_gen:
            print(f"New pythagorean triplet -> ({a}, {b}, {c})")

            if a**2 + b**2 - c**2 != 0:
                print(f"Not triplet!!!!!")
            points.append((a,b))
            i += 1
            if i > 20:
                break

            line = ax.axline((0, 0), slope=b/a, color="gray", alpha =0.2,  linestyle=(0, (5, 5)), marker='o', markevery=0.1)
            #
            line_points = np.array([(t*a, t*b) for t in range(-100, 100)])
            # line.data = line_points.T
            # line.marker = 'o'
            # ax.plot(*zip(*line_points), color="gray", alpha =0.1, marker='o', linestyle=(0, (5, 5)))
            ax.scatter(*zip(*line_points), color="gray", alpha =0.6, marker='o')

            line = ax.axline((0, 0), slope=-b / a, color="gray", alpha=0.2, linestyle=(0, (5, 5)), marker='o',
                             markevery=0.1)
            line_points = np.array([(t * a, -t * b) for t in range(-100, 100)])
            ax.scatter(*zip(*line_points), color="gray", alpha=0.6, marker='o')
        # ax.plot(*zip(*points), label=f"seed {seed}", marker='o', linewidth=2, markersize=10)

    POINTS = 1000

    for i in range(1, 15):
        parab = lambda y: y ** 2 / (2 * i) ** 2 - i ** 2
        inv_par = lambda y: -y ** 2 / (2 * i) ** 2 + i ** 2

        points_par = [(parab(y), y) for y in range(-POINTS, POINTS, 2)]
        points_inv_par = [(inv_par(y), y) for y in range(-POINTS, POINTS, 2)]

        ax.plot(*zip(*points_par))
        ax.plot(*zip(*points_inv_par))


    X_LIM = 50
    Y_LIM = 50

    ax.set_xlim(-X_LIM, X_LIM)
    ax.set_ylim(-Y_LIM, Y_LIM)

    ax.set_xticks(range(-X_LIM,X_LIM, 5))
    ax.set_yticks(range(-Y_LIM, Y_LIM, 5))
    ax.legend()
    fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)
    plt.show()





    ### par
    # fig, ax = plt.subplots(figsize=(16, 9))
    # X_LIM = 100
    # Y_LIM = 100
    # POINTS = 1000
    #
    # for i in range(1, 15):
    #     parab = lambda y: y ** 2 / (2 * i) ** 2 - i ** 2
    #     inv_par = lambda y: -y ** 2 / (2 * i) ** 2 + i ** 2
    #
    #     points_par = [(parab(y), y) for y in range(-POINTS, POINTS, 2)]
    #     points_inv_par = [(inv_par(y), y) for y in range(-POINTS, POINTS, 2)]
    #
    #     ax.plot(*zip(*points_par))
    #     ax.plot(*zip(*points_inv_par))
    #
    # ax.set_xlim(-X_LIM, X_LIM)
    # ax.set_ylim(-Y_LIM, Y_LIM)
    #
    # ax.set_xticks(range(-X_LIM, X_LIM, 5))
    # ax.set_yticks(range(-Y_LIM, Y_LIM, 5))
    # plt.show()