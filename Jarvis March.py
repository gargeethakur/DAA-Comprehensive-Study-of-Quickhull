import matplotlib.pyplot as plt
import numpy as np

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def jarvis_march(points):
    if len(points) < 3:
        return points
    hull = []
    leftmost = min(points)
    p = leftmost
    while True:
        hull.append(p)
        q = points[0]
        for r in points[1:]:
            if q == p or cross_product(p, q, r) < 0:
                q = r
        p = q
        if p == leftmost:
            break
    return hull

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
    convex_hull = jarvis_march(points)
    print("Convex Hull:", convex_hull)
    plot_convex_hull(points, convex_hull)
