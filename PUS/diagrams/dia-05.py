import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Polygon

# --- Plotting Setup ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(16, 8)) # Side-by-side
fig.suptitle('Figure 4: PUS Equivalence: Invariance of Geometric Identity under Representational Complexity', fontsize=16, fontweight='bold')

common_limits = [-3, 3]
common_aspect = 'equal'

# --- Helper function for text equations (Corrected) ---
def add_equation_text(ax, text, position, fontsize=10):
    # Pass the raw string 'text' directly to ax.text
    # Let the input string handle its own math delimiters '$'
    ax.text(position[0], position[1], text,
            fontsize=fontsize, ha='left', va='top',
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="gray", alpha=0.8))

# --- Shape Parameters ---
radius = 1.0
side = 2.0
triangle_verts = np.array([[0, np.sqrt(3)], [-1, 0], [1, 0]]) * 0.8 # Equilateral triangle

# =========================================
# Panel (a): Obfuscated Representations
# =========================================
ax0 = axes[0]
ax0.set_title('(a) Obfuscated Geometric Representations', fontsize=13)
ax0.set_xlim(common_limits)
ax0.set_ylim(common_limits)
ax0.set_aspect(common_aspect)
ax0.set_xticks([])
ax0.set_yticks([])
ax0.grid(True, linestyle='--', alpha=0.4)

# --- Circle (Obfuscated) ---
shape_pos_a1 = (-1.5, 1.5)
circle_a = Circle((shape_pos_a1[0], shape_pos_a1[1]), radius, color='blue', alpha=0.6)
ax0.add_patch(circle_a)
# Convoluted Equation (Corrected math delimiters)
eq_circle_a = r"$\oint_{\partial D} \mathbf{F} \cdot d\mathbf{r} = \iint_D (\nabla \times \mathbf{F}) \cdot d\mathbf{A} \Rightarrow \pi r^2$" \
              + "\n" + r"where $\int_0^{2\pi} \sqrt{r^2 + (\frac{dr}{d\theta})^2} d\theta = 2\pi r$"
add_equation_text(ax0, eq_circle_a, (shape_pos_a1[0] + radius + 0.2, shape_pos_a1[1] + radius*0.8)) # Adjusted text position slightly

# --- Square (Obfuscated) ---
shape_pos_a2 = (1.5, 1.5)
square_a = Rectangle((shape_pos_a2[0]-side/2, shape_pos_a2[1]-side/2), side, side, color='green', alpha=0.6)
ax0.add_patch(square_a)
# Convoluted Equation (Corrected math delimiters)
eq_square_a = r"$x(t) = \lim_{N\to\infty} \sum_{n=1,3,..}^{N} \frac{4s}{\pi n} \sin(\frac{n\pi t}{L})$" \
              + "\n" + r"$y(t) = \dots$ (orthogonal series)" \
              + "\n" + r"defines $|x|<= s/2, |y|<= s/2$" # Assume |..| renders okay, else use $..$
add_equation_text(ax0, eq_square_a, (shape_pos_a2[0] + side/2 + 0.2, shape_pos_a2[1] + side/2*0.8)) # Adjusted text position slightly

# --- Triangle (Obfuscated) ---
shape_pos_a3 = (0, -1.5)
triangle_a = Polygon(triangle_verts + shape_pos_a3, closed=True, color='red', alpha=0.6)
ax0.add_patch(triangle_a)
# Convoluted Equation (Corrected math delimiters)
eq_triangle_a = r"$\mathbf{p} = \alpha \mathbf{v}_1 + \beta \mathbf{v}_2 + \gamma \mathbf{v}_3$" \
                + "\n" + r"where $\alpha, \beta, \gamma >= 0, \alpha+\beta+\gamma=1$" \
                + "\n" + r"derived from iterative affine map limit"
add_equation_text(ax0, eq_triangle_a, (shape_pos_a3[0] + 1.0 + 0.2, shape_pos_a3[1] + np.sqrt(3)*0.8*0.7)) # Adjusted text position slightly

ax0.text(0, 0, "Complex Descriptions...\nSame Shapes?", ha='center', va='center', style='italic', color='darkred', fontsize=11)

# ==========================================
# Panel (b): PUS Clarification
# ==========================================
ax1 = axes[1]
ax1.set_title('(b) PUS Clarification: Essential Identity', fontsize=13)
ax1.set_xlim(common_limits)
ax1.set_ylim(common_limits)
ax1.set_aspect(common_aspect)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.grid(True, linestyle='--', alpha=0.4)

# --- Circle (Simple) ---
shape_pos_b1 = (-1.5, 1.5)
circle_b = Circle((shape_pos_b1[0], shape_pos_b1[1]), radius, color='blue', alpha=0.8) # Slightly more solid
ax1.add_patch(circle_b)
# Simple Equation
eq_circle_b = r"$x^2 + y^2 = r^2$"
add_equation_text(ax1, eq_circle_b, (shape_pos_b1[0] + radius + 0.2, shape_pos_b1[1] + radius*0.8)) # Adjusted text position slightly

# --- Square (Simple) ---
shape_pos_b2 = (1.5, 1.5)
square_b = Rectangle((shape_pos_b2[0]-side/2, shape_pos_b2[1]-side/2), side, side, color='green', alpha=0.8)
ax1.add_patch(square_b)
# Simple Equation
eq_square_b = r"$|x| <= s/2$" + "\n" + r"$|y| <= s/2$"
add_equation_text(ax1, eq_square_b, (shape_pos_b2[0] + side/2 + 0.2, shape_pos_b2[1] + side/2*0.8)) # Adjusted text position slightly

# --- Triangle (Simple) ---
shape_pos_b3 = (0, -1.5)
triangle_b = Polygon(triangle_verts + shape_pos_b3, closed=True, color='red', alpha=0.8)
ax1.add_patch(triangle_b)
# Simple Equation (Corrected)
eq_triangle_b = r"Vertices: $V_1, V_2, V_3$"
add_equation_text(ax1, eq_triangle_b, (shape_pos_b3[0] + 1.0 + 0.2, shape_pos_b3[1] + np.sqrt(3)*0.8*0.7)) # Adjusted text position slightly

ax1.text(0, 0, "PUS Reveals:\nObject $\equiv$ Object\nRegardless of Description!", ha='center', va='center', style='normal', color='darkgreen', fontsize=11,
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="lightgreen", alpha=0.9))

# --- Final Adjustments ---
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('pus_figure4_geometric_identity.png', dpi=300)
plt.show()
