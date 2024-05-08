import numpy as np
import matplotlib.pyplot as plt

# Hermite curve function
def hermite_curve(P0, P1, T0, T1, num_points=100):
    t = np.linspace(0, 1, num_points)
    H = np.zeros((num_points, 2))
    for i in range(num_points):
        H[i] = (2*t[i]**3 - 3*t[i]**2 + 1) * P0 + \
               (-2*t[i]**3 + 3*t[i]**2) * P1 + \
               (t[i]**3 - 2*t[i]**2 + t[i]) * T0 + \
               (t[i]**3 - t[i]**2) * T1
    return H

# Bezier curve function
def bezier_curve(P0, P1, P2, P3, num_points=100):
    t = np.linspace(0, 1, num_points)
    B = np.zeros((num_points, 2))
    for i in range(num_points):
        B[i] = (1-t[i])**3 * P0 + \
               3*t[i]*(1-t[i])**2 * P1 + \
               3*t[i]**2*(1-t[i]) * P2 + \
               t[i]**3 * P3
    return B

# Control points for Hermite curve
P0_hermite = np.array([1, 1])
P1_hermite = np.array([3, 3])
T0_hermite = np.array([2, 0])
T1_hermite = np.array([0, 2])

# Control points for Bezier curve
P0_bezier = np.array([1, 1])
P1_bezier = np.array([2, 3])
P2_bezier = np.array([4, 2])
P3_bezier = np.array([5, 5])

# Calculate Hermite curve points
H = hermite_curve(P0_hermite, P1_hermite, T0_hermite, T1_hermite)

# Calculate Bezier curve points
B = bezier_curve(P0_bezier, P1_bezier, P2_bezier, P3_bezier)

# Plot Hermite curve
plt.plot(H[:,0], H[:,1], label='Hermite Curve', color='blue')

# Plot Bezier curve
plt.plot(B[:,0], B[:,1], label='Bezier Curve', color='red')

# Plot control points
plt.scatter([P0_hermite[0], P1_hermite[0], T0_hermite[0], T1_hermite[0]], 
            [P0_hermite[1], P1_hermite[1], T0_hermite[1], T1_hermite[1]], 
            color='blue')
plt.scatter([P0_bezier[0], P1_bezier[0], P2_bezier[0], P3_bezier[0]], 
            [P0_bezier[1], P1_bezier[1], P2_bezier[1], P3_bezier[1]], 
            color='red')

# Plot lines connecting control points for Hermite curve
plt.plot([P0_hermite[0], T0_hermite[0]], [P0_hermite[1], T0_hermite[1]], 'b--')
plt.plot([P1_hermite[0], T1_hermite[0]], [P1_hermite[1], T1_hermite[1]], 'b--')

# Plot lines connecting control points for Bezier curve
plt.plot([P0_bezier[0], P1_bezier[0], P2_bezier[0], P3_bezier[0]], 
         [P0_bezier[1], P1_bezier[1], P2_bezier[1], P3_bezier[1]], 'r--')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hermite and Bezier Curves')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
