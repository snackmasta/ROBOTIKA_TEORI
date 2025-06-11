import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.widgets import Slider, TextBox


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

def interactive_robot(l1, l2, l3, start_x, start_y, start_z):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    table_ax = fig.add_subplot(1, 2, 2)
    table_ax.axis('off')

    # Author info box
    author_text = (
        "Author:\n"
        "Agung Rambujana (221364002)\n"
        "Muhammad Farhan Danial (221364017)\n"
        "Toha Rohimat (221364031)"
    )
    fig.text(0.5, 0.01, author_text, ha='center', va='bottom', fontsize=12, bbox=dict(facecolor='lightyellow', edgecolor='gray', boxstyle='round,pad=0.5'))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3 DOF Robot Arm')
    ax.set_box_aspect([1,1,1])
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_zlim([0, 25])
    
    line, = ax.plot([], [], [], '-o', linewidth=3, markersize=8)
    end_eff, = ax.plot([], [], [], 'ro', markersize=10, label='End Effector')
    ax.legend()

    # Table setup
    col_labels = ["X", "Y", "Z", "θ1 (°)", "θ2 (°)", "θ3 (°)"]
    cell_text = [["", "", "", "", "", ""]]
    table = table_ax.table(cellText=cell_text, colLabels=col_labels, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2)

    # Sliders for x, y, z and 3D view angles
    plt.subplots_adjust(left=0.1, bottom=0.40, right=0.9, top=0.95)
    axcolor = 'lightgoldenrodyellow'
    ax_x = plt.axes([0.15, 0.27, 0.65, 0.03], facecolor=axcolor)
    ax_y = plt.axes([0.15, 0.23, 0.65, 0.03], facecolor=axcolor)
    ax_z = plt.axes([0.15, 0.19, 0.65, 0.03], facecolor=axcolor)
    ax_elev = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)
    ax_azim = plt.axes([0.15, 0.11, 0.65, 0.03], facecolor=axcolor)
    slider_x = Slider(ax_x, 'X', -15, 15, valinit=start_x)
    slider_y = Slider(ax_y, 'Y', -15, 15, valinit=start_y)
    slider_z = Slider(ax_z, 'Z', 0, 22, valinit=start_z)
    slider_elev = Slider(ax_elev, 'Viewport Elevation', 0, 90, valinit=30)
    slider_azim = Slider(ax_azim, 'Viewport Azimuth', -180, 180, valinit=-60)

    # Hide slider value indicators for x, y, z
    slider_x.valtext.set_visible(False)
    slider_y.valtext.set_visible(False)
    slider_z.valtext.set_visible(False)

    # Text boxes for x, y, z
    tb_x = plt.axes([0.82, 0.27, 0.08, 0.03])
    tb_y = plt.axes([0.82, 0.23, 0.08, 0.03])
    tb_z = plt.axes([0.82, 0.19, 0.08, 0.03])
    text_x = TextBox(tb_x, '', initial=str(start_x))
    text_y = TextBox(tb_y, '', initial=str(start_y))
    text_z = TextBox(tb_z, '', initial=str(start_z))

    def update(val=None):
        x = slider_x.val
        y = slider_y.val
        z = slider_z.val
        elev = slider_elev.val
        azim = slider_azim.val
        theta1, theta2, theta3 = inverse_kinematics_3dof(x, y, z, l1, l2, l3)
        joints = forward_kinematics_3dof(theta1, theta2, theta3, l1, l2, l3)
        xs, ys, zs = zip(*joints)
        line.set_data(xs, ys)
        line.set_3d_properties(zs)
        end_eff.set_data([xs[-1]], [ys[-1]])
        end_eff.set_3d_properties([zs[-1]])
        ax.view_init(elev=elev, azim=azim)
        # Update table
        deg1 = f"{math.degrees(theta1):.2f}"
        deg2 = f"{math.degrees(theta2):.2f}"
        deg3 = f"{math.degrees(theta3):.2f}"
        table._cells[(1,0)].get_text().set_text(f"{x:.2f}")
        table._cells[(1,1)].get_text().set_text(f"{y:.2f}")
        table._cells[(1,2)].get_text().set_text(f"{z:.2f}")
        table._cells[(1,3)].get_text().set_text(deg1)
        table._cells[(1,4)].get_text().set_text(deg2)
        table._cells[(1,5)].get_text().set_text(deg3)
        # Sync text boxes with sliders
        text_x.set_val(f"{x:.2f}")
        text_y.set_val(f"{y:.2f}")
        text_z.set_val(f"{z:.2f}")
        fig.canvas.draw_idle()

    def submit_x(text):
        try:
            val = float(text)
            slider_x.set_val(val)
        except ValueError:
            pass
    def submit_y(text):
        try:
            val = float(text)
            slider_y.set_val(val)
        except ValueError:
            pass
    def submit_z(text):
        try:
            val = float(text)
            slider_z.set_val(val)
        except ValueError:
            pass

    slider_x.on_changed(update)
    slider_y.on_changed(update)
    slider_z.on_changed(update)
    slider_elev.on_changed(update)
    slider_azim.on_changed(update)
    text_x.on_submit(submit_x)
    text_y.on_submit(submit_y)
    text_z.on_submit(submit_z)
    update()
    plt.show()

if __name__ == "__main__":
    # Hardcoded starting point and link lengths for easy modification
    start_x = 5  # Starting X position (cm)
    start_y = 12 # Starting Y position (cm)
    start_z = 14 # Starting Z position (cm)
    l1 = 4       # Link 1 length (cm)
    l2 = 7       # Link 2 length (cm)
    l3 = 11      # Link 3 length (cm)

    print(f"| Link Lengths: l1 = {l1} cm, l2 = {l2} cm, l3 = {l3} cm |\n")
    print("Use the sliders to move the end effector interactively.")
    interactive_robot(l1, l2, l3, start_x, start_y, start_z)
