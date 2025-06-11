import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np


def inverse_kinematics_3dof(x, y, z, l1, l2, l3):
    theta1 = math.atan2(y, x)
    r1 = math.sqrt(x**2 + y**2)
    r2 = z - l1
    r3 = math.sqrt(r1**2 + r2**2)
    cos_theta3 = (l2**2 + l3**2 - r3**2) / (2 * l2 * l3)
    # Clamp agar tidak error jika di luar jangkauan
    cos_theta3 = max(-1.0, min(1.0, cos_theta3))
    theta3 = math.acos(cos_theta3)
    theta3 = -(math.pi - theta3)
    theta4 = math.atan2(r2, r1)
    cos_theta2_1 = (l2**2 + r3**2 - l3**2) / (2 * l2 * r3)
    cos_theta2_1 = max(-1.0, min(1.0, cos_theta2_1))
    theta2_1 = math.acos(cos_theta2_1)
    theta2 = theta4 + theta2_1
    return theta1, theta2, theta3

def forward_kinematics_3dof(theta1, theta2, theta3, l1, l2, l3):
    # Base
    x0, y0, z0 = 0, 0, 0
    # Joint 1 (shoulder)
    x1, y1, z1 = 0, 0, l1
    # Joint 2 (elbow)
    x2 = l2 * math.cos(theta2) * math.cos(theta1)
    y2 = l2 * math.cos(theta2) * math.sin(theta1)
    z2 = l1 + l2 * math.sin(theta2)
    # End effector
    x3 = x2 + l3 * math.cos(theta2 + theta3) * math.cos(theta1)
    y3 = y2 + l3 * math.cos(theta2 + theta3) * math.sin(theta1)
    z3 = z2 + l3 * math.sin(theta2 + theta3)
    return [(x0, y0, z0), (x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]

def plot_robot(joints):
    xs, ys, zs = zip(*joints)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, '-o', linewidth=3, markersize=8)
    ax.scatter(xs[-1], ys[-1], zs[-1], color='red', s=100, label='End Effector')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3 DOF Robot Arm Simulation')
    ax.legend()
    ax.set_box_aspect([1,1,1])
    plt.show()

def animate_robot(targets, l1, l2, l3):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3 DOF Robot Arm Animation')
    ax.set_box_aspect([1,1,1])
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_zlim([0, 25])
    
    line, = ax.plot([], [], [], '-o', linewidth=3, markersize=8)
    end_eff, = ax.plot([], [], [], 'ro', markersize=10, label='End Effector')
    ax.legend()

    # Interpolasi antar target agar animasi halus
    steps_per_segment = 30
    all_points = []
    for i in range(len(targets)-1):
        start = np.array(targets[i])
        end = np.array(targets[i+1])
        for t in np.linspace(0, 1, steps_per_segment, endpoint=False):
            pt = start * (1-t) + end * t
            all_points.append(tuple(pt))
    all_points.append(targets[-1])

    def update(frame):
        x, y, z = all_points[frame]
        theta1, theta2, theta3 = inverse_kinematics_3dof(x, y, z, l1, l2, l3)
        joints = forward_kinematics_3dof(theta1, theta2, theta3, l1, l2, l3)
        xs, ys, zs = zip(*joints)
        line.set_data(xs, ys)
        line.set_3d_properties(zs)
        end_eff.set_data([xs[-1]], [ys[-1]])
        end_eff.set_3d_properties([zs[-1]])
        return line, end_eff

    ani = FuncAnimation(fig, update, frames=len(all_points), interval=80, blit=False, repeat=True)
    plt.show()

if __name__ == "__main__":
    # Hardcoded starting point and link lengths for easy modification
    start_x = 8  # Starting X position (cm)
    start_y = 14 # Starting Y position (cm)
    start_z = 10 # Starting Z position (cm)
    l1 = 4       # Link 1 length (cm)
    l2 = 7       # Link 2 length (cm)
    l3 = 11      # Link 3 length (cm)
    radius = 4   # Circle radius (cm)
    num_points = 60  # Number of points along the circle

    # Add the starting point as the first target, then generate the circle
    targets = [
        (start_x, start_y, start_z)
    ] + [
        (
            start_x + radius * math.cos(2 * math.pi * t / num_points),
            start_y + radius * math.sin(2 * math.pi * t / num_points),
            start_z
        )
        for t in range(num_points)
    ]

    # Logging hasil ke tabel
    print(f"| Link Lengths: l1 = {l1} cm, l2 = {l2} cm, l3 = {l3} cm |\n")
    print("| Pos |    X   |   Y   |   Z   |   θ1   |   θ2   |   θ3   |")
    print("|-----|--------|-------|-------|--------|--------|--------|")
    for idx, (x, y, z) in enumerate(targets):
        theta1, theta2, theta3 = inverse_kinematics_3dof(x, y, z, l1, l2, l3)
        deg1 = math.degrees(theta1)
        deg2 = math.degrees(theta2)
        deg3 = math.degrees(theta3)
        print(f"|  {idx+1:2d} | {x:6.2f} | {y:5.2f} | {z:5.2f} | {deg1:6.2f} | {deg2:6.2f} | {deg3:6.2f} |")

    animate_robot(targets, l1, l2, l3)
