import matplotlib.pyplot as plt
import numpy as np

def edge_table(vertices):
    edges = []
    ymin = min(vertices, key=lambda x: x[1])[1]
    ymax = max(vertices, key=lambda x: x[1])[1]

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        if y1 != y2:
            if y1 < y2:
                edges.append((x1, y1, x2, y2))
            else:
                edges.append((x2, y2, x1, y1))

    return edges, ymin, ymax


def intersect_x(edge, y):
    x1, y1, x2, y2 = edge
    if y1 == y2:
        return x1
    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)


def fill_polygon(vertices):
    edges, ymin, ymax = edge_table(vertices)
    active_edges = []
    scanline_points = {}

    for y in range(ymin, ymax + 1):
        for edge in edges:
            x1, y1, x2, y2 = edge
            if y1 <= y < y2 or y2 <= y < y1:
                x_int = intersect_x(edge, y)
                if y not in scanline_points:
                    scanline_points[y] = []
                scanline_points[y].append(x_int)

        if y in scanline_points:
            active_edges.extend(scanline_points[y])
            active_edges.sort()
            for i in range(0, len(active_edges), 2):
                x1 = int(active_edges[i])
                x2 = int(active_edges[i + 1])
                plt.plot(range(x1, x2+1), [y] * (x2 - x1 + 1), color='r')
            print("Active edges at y =", y, ":", active_edges)

        active_edges = [x for x in active_edges if x not in scanline_points[y]]

# Example usage
vertices = [(50, 5), (110, 10), (150, 5), (110, 25),(50,5)]
plt.figure()
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(*zip(*vertices), marker='o', color='b')
fill_polygon(vertices)
plt.show()
