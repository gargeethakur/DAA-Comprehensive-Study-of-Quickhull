import numpy as np
import matplotlib.pyplot as plt

# QuickHull Algorithm to find the convex hull
def quickhull(points):
    def find_side(p1, p2, p):
        return (p[0] - p1[0]) * (p2[1] - p1[1]) - (p2[0] - p1[0]) * (p[1] - p1[1])

    def distance(p1, p2, p):
        return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))

    def farthest_point(p1, p2, points):
        max_dist = -1
        farthest = None
        for p in points:
            dist = distance(p1, p2, p)
            if dist > max_dist:
                max_dist = dist
                farthest = p
        return farthest

    def hull_set(p1, p2, points, hull):
        if not points:
            return
        fp = farthest_point(p1, p2, points)
        hull.append(fp)
        left_set1 = [p for p in points if find_side(p1, fp, p) > 0]
        left_set2 = [p for p in points if find_side(fp, p2, p) > 0]
        hull_set(p1, fp, left_set1, hull)
        hull_set(fp, p2, left_set2, hull)

    points = sorted(points, key=lambda x: x[0])
    leftmost, rightmost = points[0], points[-1]
    hull = [leftmost, rightmost]

    left_set = [p for p in points if find_side(leftmost, rightmost, p) > 0]
    right_set = [p for p in points if find_side(rightmost, leftmost, p) > 0]

    hull_set(leftmost, rightmost, left_set, hull)
    hull_set(rightmost, leftmost, right_set, hull)

    return np.array(sorted(hull, key=lambda x: (x[0], x[1])))

# Generate a set of random points forming a simple polygon
np.random.seed(42)
points = np.random.rand(1000, 2) * 100

# Compute the convex hull using QuickHull
hull_points = quickhull(points)

# Plot the points and convex hull
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], label="Points", color="blue")
plt.plot(*zip(*np.vstack([hull_points, hull_points[0]])), 'r-', label="Convex Hull", linewidth=2)
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Convex Hull using QuickHull Algorithm")
plt.grid()
plt.show()