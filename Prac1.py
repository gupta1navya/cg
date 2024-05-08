import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    plt.plot(x, y, 'ro')
    print("Intermediate points using DDA:")
    for _ in range(steps):
        x += x_increment
        y += y_increment
        plt.plot(round(x), round(y), 'ro')
        print(f"({round(x)}, {round(y)})")
    plt.plot([x1, x2], [y1, y2], 'b')

def draw_line_Bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    x = x1
    y = y1
    plt.plot(x, y, 'ro')
    print("Intermediate points using Bresenham:")
    if x1 < x2:
        x_increment = 1
    else:
        x_increment = -1
    if y1 < y2:
        y_increment = 1
    else:
        y_increment = -1
    while x != x2:
        x += x_increment
        if p < 0:
            p += 2 * dy
        else:
            y += y_increment
            p += 2 * (dy - dx)
        plt.plot(x, y, 'ro')
        print(f"({x}, {y})")
    plt.plot([x1, x2], [y1, y2], 'g')

# Test the functions
x1, y1 = 9, 18
x2, y2 = 14, 22

plt.figure(figsize=(8, 6))

# Plotting using DDA
plt.subplot(1, 2, 1)
plt.title('DDA Algorithm')
draw_line_DDA(x1, y1, x2, y2)
plt.grid(True)
plt.axis('equal')

# Plotting using Bresenham's
plt.subplot(1, 2, 2)
plt.title('Bresenham Algorithm')
draw_line_Bresenham(x1, y1, x2, y2)
plt.grid(True)
plt.axis('equal')

plt.show()
