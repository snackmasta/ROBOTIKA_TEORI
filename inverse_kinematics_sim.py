import math

def inverse_kinematics_3dof(x, y, z, l1, l2, l3):
    # Shoulder angle (theta1)
    theta1 = math.degrees(math.atan2(y, x))

    # r1, r2, r3
    r1 = math.sqrt(x**2 + y**2)
    r2 = z - l1
    r3 = math.sqrt(r1**2 + r2**2)

    # Elbow angle (theta3)
    cos_theta3 = (l2**2 + l3**2 - r3**2) / (2 * l2 * l3)
    theta3 = math.degrees(math.acos(cos_theta3))
    theta3 = -(180 - theta3)  # as in the handwritten solution

    # Shoulder-lift angle (theta2)
    theta4 = math.degrees(math.atan2(r2, r1))
    cos_theta2_1 = (l2**2 + r3**2 - l3**2) / (2 * l2 * r3)
    theta2_1 = math.degrees(math.acos(cos_theta2_1))
    theta2 = theta4 + theta2_1

    return theta1, theta2, theta3

if __name__ == "__main__":
    # Example values from the markdown
    x = 8
    y = 14
    z = 10
    l1 = 4
    l2 = 7
    l3 = 11

    theta1, theta2, theta3 = inverse_kinematics_3dof(x, y, z, l1, l2, l3)
    print(f"Theta1 (base): {theta1:.2f}°")
    print(f"Theta2 (shoulder): {theta2:.2f}°")
    print(f"Theta3 (elbow): {theta3:.2f}°")
