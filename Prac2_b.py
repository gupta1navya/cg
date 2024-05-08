import matplotlib.pyplot as plt

def draw_circle_midpoint(radius):
    x = 0
    y = radius
    p = 1 - radius  # Initial decision parameter
    points = set()
    draw_circle_points(x, y, points)
    print("Intermediate points:")
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        draw_circle_points(x, y, points)
        print(f"({x}, {y}), ({-x}, {y}), ({x}, {-y}), ({-x}, {-y}), ({y}, {x}), ({-y}, {x}), ({y}, {-x}), ({-y}, {-x})")
    plot_points(points)

def draw_circle_points(x, y, points):
    points.add((x, y))
    points.add((-x, y))
    points.add((x, -y))
    points.add((-x, -y))
    points.add((y, x))
    points.add((-y, x))
    points.add((y, -x))
    points.add((-y, -x))

def plot_points(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.plot(x_values, y_values, 'ro')
    plt.grid(True)
    plt.axis('equal')
    plt.title('Mid-Point Circle Drawing Algorithm')
    plt.show()

# Test the function
radius = 10
draw_circle_midpoint(radius)
