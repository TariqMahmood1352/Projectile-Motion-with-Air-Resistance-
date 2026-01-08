# Projectile-Motion-with-Air-Resistance-
Simulates projectile motion in vacuum and with air resistance. Compares trajectories, range, and flight time, highlighting how drag affects real-world motion. Includes code, visualizations, and analytical insights for learning and experimentation.


Projectile Motion with Air Resistance
A Computational Physics Simulation and Visualization in Python
🔬 Overview

This project presents a numerical simulation and animation of projectile motion under two physical scenarios:

Ideal motion in vacuum

Realistic motion with quadratic air resistance

Both cases use identical initial conditions, allowing a direct and physically meaningful comparison.
The simulation demonstrates how air resistance significantly affects range, maximum height, and time of flight, and highlights why idealized projectile motion fails to describe real-world dynamics.

The output includes a high-quality MP4 animation, suitable for teaching, presentations, LinkedIn posts, and YouTube demonstrations.

🎯 Objectives

Compare ideal and realistic projectile motion under identical initial conditions

Demonstrate the effect of quadratic drag force

Enforce physically correct ground-impact conditions (y ≥ 0)

Compute and display key physical quantities:

Horizontal range

Maximum height

Time of flight

Generate a smooth, publication-quality animation

🧠 Physical Model
1. Vacuum (Ideal Case)

The projectile follows analytical equations of motion under constant gravity:

Horizontal motion: constant velocity

Vertical motion: uniformly accelerated motion

Key assumptions:

No air resistance

Point mass

Uniform gravitational field

2. Air Resistance (Realistic Case)

The projectile experiences a quadratic drag force proportional to the square of its speed:

Drag force opposes velocity

Equations of motion are nonlinear

No closed-form solution exists

Therefore, the system is solved using numerical time integration.

Key features:

Velocity-dependent acceleration

Asymmetric trajectory

Reduced range and height

Shorter time of flight

🧮 Numerical Method

Time integration: Explicit forward Euler method

Time step: Small and fixed for stability

Termination condition:
The simulation stops exactly when the projectile reaches the ground (y ≤ 0)

Post-processing:
Trajectories are clipped to prevent non-physical motion below ground

Each trajectory (vacuum and drag) is handled independently, ensuring physically correct comparison despite different flight times.

🎥 Animation Strategy

Precompute both trajectories before animation

Animate motion frame-by-frame

Freeze each projectile at ground impact

Overlay numerical results directly on the animation:

Range

Maximum height

Time of flight

Export animation as MP4 using FFmpeg

This approach guarantees:

Numerical stability

Visual clarity

Physically meaningful termination

📊 Key Outputs

Trajectory comparison plot (vacuum vs air resistance)

Real-time animated motion

On-screen numerical metrics

MP4 video output suitable for sharing

🧪 Results and Physical Insights

Air resistance dramatically reduces the projectile range

Maximum height is lower in realistic motion

The trajectory becomes asymmetric

Time of flight decreases due to energy dissipation

Identical initial conditions lead to fundamentally different outcomes

This highlights the importance of nonlinear forces in realistic physical systems.
