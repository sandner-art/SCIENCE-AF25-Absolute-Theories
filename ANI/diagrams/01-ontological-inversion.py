# Full Python Code for Generating Diagrams

import matplotlib.pyplot as plt
import numpy as np

# Figure 1: Structure vs. Agency Dynamics
def plot_structure_agency():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Nodes
    structure = plt.Circle((0.3, 0.7), 0.1, color='skyblue', ec='black')
    agency = plt.Circle((0.7, 0.7), 0.1, color='lightgreen', ec='black')
    
    # Arrows
    ax.arrow(0.3, 0.6, 0.35, 0, head_width=0.05, head_length=0.05, fc='gray', ec='gray')
    ax.arrow(0.7, 0.6, -0.35, 0, head_width=0.05, head_length=0.05, fc='gray', ec='gray')
    
    # Labels
    ax.text(0.3, 0.7, 'Structure\n(I)', ha='center', va='center')
    ax.text(0.7, 0.7, 'Agency\n(↦)', ha='center', va='center')
    ax.text(0.5, 0.65, 'Performative\nEnactment', ha='center', va='center', fontsize=9)
    ax.text(0.5, 0.55, 'Axiomatic\nValidation', ha='center', va='center', fontsize=9)
    
    # Add circles and set limits
    ax.add_patch(structure)
    ax.add_patch(agency)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Structure vs. Agency Dynamics")
    plt.show()

# Figure 2: Macro vs. Micro Scale Invariance
def plot_scale_invariance():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Fractal-like pattern
    levels = 3
    scale = 0.5
    
    def draw_fractal(x, y, size, level):
        if level > 0:
            ax.add_patch(plt.Rectangle((x, y), size, size, color='lightcoral'))
            new_size = size * scale
            draw_fractal(x, y, new_size, level-1)
            draw_fractal(x + size - new_size, y, new_size, level-1)
            draw_fractal(x, y + size - new_size, new_size, level-1)
            draw_fractal(x + size - new_size, y + size - new_size, new_size, level-1)
    
    draw_fractal(0.1, 0.1, 0.8, levels)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Macro vs. Micro Scale Invariance")
    plt.show()

# Figure 3: Objective vs. Subjective Perception
def plot_objective_subjective():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Venn diagram
    objective = plt.Circle((0.4, 0.5), 0.25, color='lightblue', alpha=0.5, ec='black')
    subjective = plt.Circle((0.6, 0.5), 0.25, color='lightgray', alpha=0.5, ec='black')
    
    # Labels
    ax.text(0.4, 0.5, 'Objective\n(Functional Outcome)', ha='center', va='center')
    ax.text(0.6, 0.5, 'Subjective\n(Situated Perspective)', ha='center', va='center')
    ax.text(0.5, 0.5, 'Intersubjective\nReality', ha='center', va='center', fontsize=9)
    
    # Add circles and set limits
    ax.add_patch(objective)
    ax.add_patch(subjective)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Objective vs. Subjective Perception")
    plt.show()

# Figure 4: Totalitarian Is-ness Lifecycle
def plot_totalitarian_lifecycle():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Phase space diagram
    x = np.linspace(0, 1, 400)
    y1 = 0.2 * np.sin(2 * np.pi * x) + 0.5
    y2 = 0.1 * np.sin(4 * np.pi * x) + 0.5
    
    ax.plot(x, y1, label='Stable State (In_T)', color='blue')
    ax.plot(x, y2, label='Unstable State', color='red', linestyle='--')
    
    # Potential well
    ax.plot([0.5, 0.5], [0.3, 0.7], color='gray', linestyle='--')
    ax.text(0.5, 0.3, 'Potential Well\n(In_T)', ha='center', va='center', fontsize=9)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Axiomatic Stress')
    ax.set_ylabel('System State')
    ax.legend()
    
    plt.title("Totalitarian Is-ness Lifecycle")
    plt.savefig('ani_Totalitarian-Lifecycle.png', dpi=300)
    plt.show()

# Figure 5: Simulated Ontological Inversion Event (Axial Realignment)
def plot_ontological_inversion():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Bifurcation diagram
    x = np.linspace(0, 1, 400)
    y1 = 0.2 * np.sin(2 * np.pi * x) + 0.5
    y2 = 0.1 * np.sin(4 * np.pi * x) + 0.5
    
    ax.plot(x, y1, label='Stable State (In)', color='blue')
    ax.plot(x, y2, label='Unstable State (Out)', color='red', linestyle='--')
    
    # Bifurcation points
    ax.axvline(x=0.5, color='gray', linestyle='--', label='Bifurcation Point')
    ax.text(0.51, 0.3, 'Bifurcation Point', ha='left', va='center', fontsize=10, color='gray')
    
    # System trajectory
    trajectory_x = [0.2, 0.4, 0.6, 0.8]
    trajectory_y = [0.5, 0.6, 0.4, 0.55]
    ax.plot(trajectory_x, trajectory_y, color='purple', linestyle='-', marker='o', label='System Trajectory')
    
    # Annotations for trajectory
    for i, (xi, yi) in enumerate(zip(trajectory_x, trajectory_y)):
        ax.annotate(f'State {i+1}', (xi, yi), textcoords="offset points", xytext=(0,10),
                    ha='center', fontsize=9, color='purple')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Control Parameter (External Pressure)')
    ax.set_ylabel('System State')
    ax.legend(loc='upper right')
    
    plt.title("Simulated Ontological Inversion Event (Axial Realignment)")
    plt.savefig('ani_Ontological_Inversion.png', dpi=300)
    plt.show()

# Additional Figures

# Figure 6: Is-In-Out Triad Topology
def plot_is_in_out_triad():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Circles for In, Out, and Boundary
    in_circle = plt.Circle((0.3, 0.5), 0.2, color='lightblue', ec='black', label='In-ness')
    out_circle = plt.Circle((0.7, 0.5), 0.2, color='lightgray', ec='black', label='Out-ness')
    boundary = plt.Circle((0.5, 0.5), 0.35, color='none', ec='black', linestyle='--', label='Boundary (∂I)')
    
    # Add circles and boundary
    ax.add_patch(in_circle)
    ax.add_patch(out_circle)
    ax.add_patch(boundary)
    
    # Labels
    ax.text(0.3, 0.5, 'In-ness (In)', ha='center', va='center')
    ax.text(0.7, 0.5, 'Out-ness (Out)', ha='center', va='center')
    ax.text(0.5, 0.15, 'Boundary (∂I)', ha='center', va='center')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Is-In-Out Triad Topology")
    plt.legend(loc='upper right')
    plt.savefig('ani_Is-In-Out-Triad.png', dpi=300)
    plt.show()

# Figure 7: Performative Enactment and Axiomatic Validation Loop
def plot_enactment_validation_loop():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Circular loop
    angles = np.linspace(0, 2 * np.pi, 100)
    ax.plot(0.5 + 0.4 * np.cos(angles), 0.5 + 0.4 * np.sin(angles), color='gray', linestyle='--')
    
    # Nodes
    enactment = plt.Circle((0.5, 0.7), 0.1, color='lightgreen', ec='black')
    validation = plt.Circle((0.5, 0.3), 0.1, color='lightcoral', ec='black')
    
    # Arrows
    ax.arrow(0.5, 0.6, 0, -0.2, head_width=0.05, head_length=0.05, fc='gray', ec='gray')
    ax.arrow(0.5, 0.4, 0, 0.2, head_width=0.05, head_length=0.05, fc='gray', ec='gray')
    
    # Labels
    ax.text(0.5, 0.7, 'Performative\nEnactment (↦)', ha='center', va='center')
    ax.text(0.5, 0.3, 'Axiomatic\nValidation (⊢I)', ha='center', va='center')
    
    # Add circles and set limits
    ax.add_patch(enactment)
    ax.add_patch(validation)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Performative Enactment and Axiomatic Validation Loop")
    plt.savefig('ani_Performative_Enactment.png', dpi=300)
    plt.show()

# Figure 8: Field Collapse and Reconstitution
def plot_field_collapse_reconstitution():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Initial and final states
    initial_state = plt.Circle((0.3, 0.6), 0.2, color='lightblue', ec='black', alpha=0.5, label='Initial State (I)')
    final_state = plt.Circle((0.7, 0.6), 0.2, color='lightgreen', ec='black', alpha=0.5, label='Reconstituted State (I")')
    
    # Arrow indicating collapse and reconstitution
    ax.arrow(0.3, 0.4, 0.4, 0, head_width=0.05, head_length=0.05, fc='gray', ec='gray')
    
    # Add circles and set limits
    ax.add_patch(initial_state)
    ax.add_patch(final_state)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Field Collapse and Reconstitution")
    plt.legend(loc='upper right')
    plt.savefig('ani_Field_Collapse.png', dpi=300)
    plt.show()

# Figure 9: Catastrophic Boundary Transgression
def plot_boundary_transgression():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Boundary and transgression arrow
    boundary = plt.Circle((0.5, 0.5), 0.3, color='none', ec='black', linestyle='--')
    transgression_arrow = plt.Arrow(0.4, 0.5, 0.2, 0, width=0.05, color='red')
    
    # Add boundary and arrow
    ax.add_patch(boundary)
    ax.add_patch(transgression_arrow)
    
    # Labels
    ax.text(0.5, 0.5, 'Boundary (∂I)', ha='center', va='center')
    ax.text(0.6, 0.5, 'Transgression', ha='center', va='center', color='red')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.title("Catastrophic Boundary Transgression")
    plt.show()

# Generate all figures
plot_structure_agency()
plot_scale_invariance()
plot_objective_subjective()
plot_totalitarian_lifecycle()
plot_ontological_inversion()
plot_is_in_out_triad()
plot_enactment_validation_loop()
plot_field_collapse_reconstitution()
plot_boundary_transgression()