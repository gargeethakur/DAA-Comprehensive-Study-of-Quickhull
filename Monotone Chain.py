import matplotlib.pyplot as plt
import numpy as np

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def monotone_chain(points):
    points = sorted(points)
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)

    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)

    return lower_hull[:-1] + upper_hull[:-1]

def plot_convex_hull(points, hull):
    plt.scatter(*zip(*points), color='blue', label='Points')
    hull.append(hull[0])  # Close the hull
    hull_x, hull_y = zip(*hull)
    plt.plot(hull_x, hull_y, 'r-', label='Convex Hull')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    num_points = 1000  # Number of random points
    points = [(x, y) for x, y in np.random.rand(num_points, 2) * 100]
    convex_hull = monotone_chain(points)
    print("Convex Hull:", convex_hull)
    plot_convex_hull(points, convex_hull)
