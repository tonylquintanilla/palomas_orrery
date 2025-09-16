import numpy as np

def rotation_matrix_x(angle):
    """Create rotation matrix around X axis"""
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def rotation_matrix_z(angle):
    """Create rotation matrix around Z axis"""
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

# --- Parameters for Mercury ---
i_deg = 7.0
omega_deg = 29.1
i_rad = np.radians(i_deg)
omega_rad = np.radians(omega_deg)

# --- The Transformation Matrices from your script ---
R1 = rotation_matrix_z(omega_rad) # ω rotation
R2 = rotation_matrix_x(i_rad)     # i rotation

# 1. Transformation for the purple frame
R_after_omega = R1

# 2. CORRECTED transformation for the orange frame (Intrinsic rotation)
R_after_inclination = R1 @ R2 # <--- THE FIX IS HERE

# --- The initial X-axis vector of the purple frame ---
# This is the original X-axis rotated by ω
purple_x_axis_vector = R_after_omega @ np.array([1, 0, 0])

# --- Calculate the position of the orange X-axis ---
# This is the original X-axis after BOTH transformations
orange_x_axis_vector = R_after_inclination @ np.array([1, 0, 0])

# --- Print the results ---
print("Coordinates of the purple X-axis tip:")
print(f"X={purple_x_axis_vector[0]:.4f}, Y={purple_x_axis_vector[1]:.4f}, Z={purple_x_axis_vector[2]:.4f}")
print("\nCoordinates of the orange X-axis tip (after the 'i' tilt):")
print(f"X={orange_x_axis_vector[0]:.4f}, Y={orange_x_axis_vector[1]:.4f}, Z={orange_x_axis_vector[2]:.4f}")

# --- Check if they are identical ---
if np.allclose(purple_x_axis_vector, orange_x_axis_vector):
    print("\n\nConclusion: The purple and orange X-axes are in the exact same position.")
    print("This proves the tilt only happens around the X-axis.")
else:
    print("\n\nConclusion: The X-axes are in different positions.")