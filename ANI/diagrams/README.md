# ANI Paper Figures (Tanaka)

### README Descriptions:

1.  **Figure 1: The ANI Cycle of Socio-Cultural Constitution (`ani_figure1_cycle_diagram.png`)**
    *   **Description:** This conceptual diagram illustrates the core theoretical framework of ANI. It maps the dynamic interrelationships between the foundational **Is-ness (I)**, the positions of **In-ness (In)** and **Out-ness (Out)**, the **Boundary (∂I)**, and key mediating concepts like **Praxis/Embodiment**, **Discourse/Signification**, **Habitus**, and **Axiomatic Validation (⊢<sub>I</sub>)**. Arrows depict the cycle of performative **Enactment (↦)** by subjects (primarily within **In**) reinforcing **I**, while **I** provides the axiomatic basis for validation, boundary work, and the constitution of the entire **Is-In-Out triad**.
    *   **Placement:** Essential in Section 3 (Conceptual Framework).

2.  **Figure 2: Simulated Trajectory of Axiomatic Convergence under ANI (with Doubting State) (`ani_figure2_abm_convergence_triple_3state_revised.png`)**
    *   **Description:** This figure presents results from a simple Agent-Based Model simulating ANI dynamics with three states: **Out** (salmon), **In** (lightblue), and **Doubting/Boundary** (lightyellow). The three panels show snapshots of the spatial grid at different time points (Initial, Consolidation, Near Convergence). It visually demonstrates how local influence and validation rules (agents potentially becoming 'Doubting' when influenced by the opposite state, then resolving 'Doubt' towards neighbors) can lead to the emergence and consolidation of a dominant **In-ness** configuration from an initially mixed state, with the 'Doubting' state transiently highlighting the active boundaries between clusters.
    *   **Placement:** Section 4 (Methodology - as example of simulation) or Section 5 (Case Studies - as abstract illustration).

3.  **Figure 3: Intensity Mapping of Boundary Work (∂I) under ANI (`ani_figure3_boundary_intensity.png`)**
    *   **Description:** This heatmap visualizes the spatial concentration of "interaction intensity" (representing validation events, boundary policing, symbolic negotiation) between two abstractly defined regions representing **In-ness** and **Out-ness**. Using simulated interaction points biased towards the interface and Kernel Density Estimation, the plot shows significantly higher intensity concentrated within the designated **Boundary Zone (∂I)** compared to deeper within the **In** or **Out** regions. This graphically supports ANI's theoretical emphasis on the boundary as a crucial site of active social work and validation efforts.
    *   **Placement:** Section 5 (Case Studies - applied to boundary work) or Section 7 (Discussion - on power/boundaries).

4.  **Figure 4: Simulated Ontological Inversion Event (Axial Realignment) under ANI (`ani_figure4_inversion_event.png`)**
    *   **Description:** This figure employs a cusp catastrophe model to visualize an "Ontological Inversion Event" or "Axial Realignment" as predicted by ANI. The plot shows system state trajectories (Y-axis: representing alignment, e.g., In vs. Out) evolving as a control parameter changes (X-axis: representing external pressure or internal stress). It demonstrates how a gradual change in the control parameter can cause the system to suddenly jump from one stable branch (e.g., high alignment, **In-ness**) to the other (e.g., low alignment, **Out-ness**), or vice versa, marked by asterisks. This illustrates ANI's capacity to explain non-linear, abrupt shifts in social status or identity configuration under critical conditions.
    *   **Placement:** Section 6 (Social Change) or Section 7 (Discussion).

### LaTeX Code Snippets:

```latex
% --- Figure 1 ---
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{ani_figure1_cycle_diagram.png} % Replace with your filename
    \caption{The ANI Cycle of Socio-Cultural Constitution. This diagram illustrates the core framework of the Axiomatic Nature of Is-ness (ANI). It depicts the central role of the axiomatic field of Is-ness ($\mathbf{I}$) in constituting the positions of In-ness ($\mathbf{In}$) and Out-ness ($\mathbf{Out}$) via the dynamic Boundary ($\partial\mathbf{I}$). Praxis and Discourse performatively enact ($\mapsto$) and reproduce $\mathbf{I}$, shaping Habitus. In-ness status subjects phenomena to Axiomatic Validation ($\vdash_{\mathbf{I}}$), which reinforces prevailing Praxis and Discourse, completing the self-sustaining cycle.}
    \label{fig:ani_cycle}
\end{figure}

% --- Figure 2 (Requires \usepackage{subcaption} if placing side-by-side, otherwise adjust width) ---
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{ani_figure2_abm_convergence_triple_3state_revised.png} % Replace with your filename
    \caption{Simulated Trajectory of Axiomatic Convergence under ANI (with Doubting State). Agent-Based Model results showing the spatial distribution of states over time: (a) Initial random configuration with low $\mathbf{In}$-ness. (b) Intermediate consolidation phase, showing clustering and the emergence of the Doubting/Boundary state ($\partial\mathbf{I}$, yellow) at interfaces. (c) Near convergence towards a dominant $\mathbf{In}$-ness configuration, demonstrating how local performative validation dynamics can lead to global axiomatic stabilization. States: $\mathbf{Out}$ (salmon), $\mathbf{In}$ (lightblue), Doubting/$\partial\mathbf{I}$ (yellow).}
    \label{fig:ani_convergence}
\end{figure}

% --- Figure 3 ---
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{ani_figure3_boundary_intensity.png} % Replace with your filename
    \caption{Intensity Mapping of Boundary Work ($\partial\mathbf{I}$) under ANI. Kernel Density Estimation plot visualizing the spatial concentration of simulated interaction/validation events ("Intensity") across abstract socio-symbolic dimensions. The heatmap (inferno colormap, higher values indicate more intensity) clearly shows activity concentrated within the designated Boundary Zone ($\partial\mathbf{I}$) separating the regions of $\mathbf{In}$-ness and $\mathbf{Out}$-ness. This supports ANI's proposition that boundaries are active sites of social negotiation and axiomatic enforcement.}
    \label{fig:ani_boundary}
\end{figure}

% --- Figure 4 ---
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{ani_figure4_inversion_event.png} % Replace with your filename
    \caption{Simulated Ontological Inversion Event (Axial Realignment) under ANI. Visualization based on the cusp catastrophe model. The Y-axis represents the system state (e.g., degree of alignment with $\mathbf{I}$), and the X-axis represents a changing control parameter (e.g., stress/pressure). Trajectories show how gradual changes in the parameter can lead to sudden, discontinuous jumps (marked by '*') between stable states (upper branch $\approx \mathbf{In}$, lower branch $\approx \mathbf{Out}$). This models the Axial Realignment or Ontological Inversion Event predicted by ANI, where subjects experience abrupt shifts between $\mathbf{In}$-ness and $\mathbf{Out}$-ness under critical conditions.}
    \label{fig:ani_inversion}
\end{figure}
```

