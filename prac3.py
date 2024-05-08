import matplotlib.pyplot as plt

INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def computeCode(x, y):
    code = INSIDE
    if x < x_min:      # left of rectangle
        code |= LEFT
    elif x > x_max:    # right of rectangle
        code |= RIGHT
    if y < y_min:      # below
        code |= BOTTOM
    elif y > y_max:    # above
        code |= TOP
    return code

def cohenSutherlandClip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        print(f"Line accepted from {x1:.2f}, {y1:.2f} to {x2:.2f}, {y2:.2f}")
        plt.plot([x1, x2], [y1, y2], color='black', linewidth=2)  # Plot the accepted line
    else:
        print("Line rejected")

x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

# Plot the clipping window
plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='blue', linewidth=2)

# Test lines
cohenSutherlandClip(3, 5, 5, 7)
plt.plot([3, 5], [5, 7], color='green', linewidth=1)
cohenSutherlandClip(8, 2, 8, 6)
plt.plot([8, 8], [2, 6], color='green', linewidth=1)
cohenSutherlandClip(1, 5, 4, 1)
plt.plot([1, 5], [4, 1], color='green', linewidth=1)

# Set plot limits and aspect ratio
plt.xlim(0, 12)
plt.ylim(0, 10)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
