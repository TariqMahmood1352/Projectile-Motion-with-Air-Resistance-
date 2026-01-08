import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# ---------------- PARAMETERS ----------------
g = 9.81
m = 0.15
c = 0.008
v0 = 50.0
theta = np.deg2rad(45)
dt = 0.02

vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)

# ---------------- VACUUM ----------------
t = np.arange(0, 10, dt)
x_v = vx0 * t
y_v = vy0 * t - 0.5 * g * t**2

mask = y_v >= 0
x_v, y_v, t_v = x_v[mask], y_v[mask], t[mask]

Rv, Hv, Tv = x_v[-1], y_v.max(), t_v[-1]

# ---------------- AIR DRAG ----------------
x_d, y_d = [0], [0]
vx, vy = vx0, vy0
t_d = [0]

while y_d[-1] >= 0:
    v = np.sqrt(vx**2 + vy**2)
    ax = -(c/m) * v * vx
    ay = -g - (c/m) * v * vy

    vx += ax * dt
    vy += ay * dt

    x_d.append(x_d[-1] + vx * dt)
    y_d.append(y_d[-1] + vy * dt)
    t_d.append(t_d[-1] + dt)

# remove last point below ground
x_d = np.array(x_d[:-1])
y_d = np.array(y_d[:-1])
t_d = np.array(t_d[:-1])

Rd, Hd, Td = x_d[-1], y_d.max(), t_d[-1]

# ---------------- ANIMATION ----------------
fig, ax = plt.subplots(figsize=(9,5))
ax.set_xlim(0, Rv*1.1)
ax.set_ylim(0, Hv*1.1)
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Height (m)")
ax.set_title("Projectile Motion: Vacuum vs Air Resistance")

line_v, = ax.plot([], [], lw=2, label="Vacuum")
line_d, = ax.plot([], [], lw=2, label="With Air Resistance")
pt_v, = ax.plot([], [], 'o')
pt_d, = ax.plot([], [], 'o')

ax.legend()
text = ax.text(0.02, 0.95, "", transform=ax.transAxes,
               va="top", bbox=dict(boxstyle="round", alpha=0.85))

N_v = len(x_v)
N_d = len(x_d)
N = max(N_v, N_d)

def update(i):
    if i < N_v:
        line_v.set_data(x_v[:i], y_v[:i])
        pt_v.set_data([x_v[i-1]], [y_v[i-1]])
    else:
        line_v.set_data(x_v, y_v)
        pt_v.set_data([x_v[-1]], [y_v[-1]])

    if i < N_d:
        line_d.set_data(x_d[:i], y_d[:i])
        pt_d.set_data([x_d[i-1]], [y_d[i-1]])
    else:
        line_d.set_data(x_d, y_d)
        pt_d.set_data([x_d[-1]], [y_d[-1]])

    text.set_text(
        f"VACUUM\n"
        f"Range: {Rv:.1f} m\n"
        f"Height: {Hv:.1f} m\n"
        f"Time: {Tv:.2f} s\n\n"
        f"AIR DRAG\n"
        f"Range: {Rd:.1f} m\n"
        f"Height: {Hd:.1f} m\n"
        f"Time: {Td:.2f} s"
    )

    return line_v, line_d, pt_v, pt_d, text

ani = FuncAnimation(fig, update, frames=N, interval=40)

# ---------------- SAVE VIDEO ----------------
writer = FFMpegWriter(fps=25)
ani.save("projectile_vacuum_vs_air_drag.mp4", writer=writer)
plt.show()
