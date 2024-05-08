def inside(point, edge):
    # Check if a point is inside or outside an edge
    x, y = point
    x1, y1, x2, y2 = edge
    if (x2 - x1) * (y - y1) > (y2 - y1) * (x - x1):
        return True  # Point is inside the edge
    return False  # Point is outside the edge

def intersect(point1, point2, edge):
    # Calculate intersection point of a line segment with an edge
    x1, y1 = point1
    x2, y2 = point2
    x3, y3, x4, y4 = edge
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    denominator = dx1 * dy2 - dy1 * dx2
    if denominator == 0:
        return None  # Lines are parallel or coincident
    t = ((x1 - x3) * dy2 - (y1 - y3) * dx2) / denominator
    if 0 <= t <= 1:
        ix, iy = x1 + t * dx1, y1 + t * dy1
        return ix, iy  # Intersection point
    return None  # Intersection point is outside the segment

def clip_polygon(polygon, window):
    # Clip a polygon against a rectangular window
    output = []
    for edge in window:
        if len(edge) != 4:
            raise ValueError("Window edges must be defined by four coordinates (x1, y1, x2, y2).")
        input_polygon = output.copy() if output else polygon
        output = []
        prev_point = input_polygon[-1]
        for point in input_polygon:
            if len(point) != 2:
                raise ValueError("Polygon points must be defined by two coordinates (x, y).")
            if inside(point, edge):
                if not inside(prev_point, edge):
                    intersection = intersect(prev_point, point, edge)
                    if intersection:
                        output.append(intersection)
                output.append(point)
            elif inside(prev_point, edge):
                intersection = intersect(prev_point, point, edge)
                if intersection:
                    output.append(intersection)
            prev_point = point
    return output

polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 300), (200, 250), (150, 300), (50, 300)]
window = [(100, 100, 300, 200)]  # Rectangle window (x1, y1, x2, y2)
try:
    clipped_polygon = clip_polygon(polygon, window)
    print("Clipped Polygon:", clipped_polygon)
except ValueError as e:
    print("Error:", e)


