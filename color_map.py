# Gemini 5-1-2026 Color swatch of css colors
# Notes: This reference maps CSS4 named colors in Python/Matplotlib. RGB values are converted to the 0-255 standard
# for accessibility. In Python scripts, these can be used as strings or converted to 0.0-1.0 floats by dividing by 255.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def plot_colortable_255(colors, title):
    # Sort colors by hue, saturation, and value for a better visual flow
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name)
                    for name, color in colors.items())
    names = [name for hsv, name in by_hsv]

    n = len(names)
    ncols = 2 
    nrows = n // ncols + (1 if n % ncols > 0 else 0)

    fig, ax = plt.subplots(figsize=(14, 12))
    X, Y = fig.get_dpi() * fig.get_size_inches()
    h = Y / (nrows + 1)
    w = X / ncols

    for i, name in enumerate(names):
        col = i % ncols
        row = i // ncols
        y = Y - (row * h) - h

        swatch_x = col * w
        text_x = swatch_x + (w * 0.15)
        
        # 1. Get the float RGB and convert to 0-255 scale
        rgb_float = mcolors.to_rgb(colors[name])
        rgb_255 = tuple(int(c * 255) for c in rgb_float)
        hex_code = mcolors.to_hex(colors[name]).upper()
        
        # 2. Draw the color swatch
        ax.add_patch(plt.Rectangle((swatch_x, y), w * 0.1, h * 0.7, 
                                   facecolor=colors[name], edgecolor='0.7'))

        # 3. Add the Name, Hex, and RGB (0-255) info
        # Using f-string formatting to keep columns aligned
        full_label = f"{name:<18} | {hex_code} | RGB: {str(rgb_255):<15}"
        ax.text(text_x, y + h * 0.35, full_label, family='monospace', 
                fontsize=9, verticalalignment='center')

    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_axis_off()
    plt.title(title, fontsize=12, weight='bold', pad=10)
    plt.tight_layout()
    plt.show()

# Visualize the colors with 0-255 RGB values
plot_colortable_255(mcolors.CSS4_COLORS, "Matplotlib Colors: Name | Hex | RGB (0-255)")