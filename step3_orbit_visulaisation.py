import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from step2_orbit_calculation import get_position_velocity


class OrbitAnimation:
    def __init__(self):
        # --- Figure & axes ---
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.ax.set_xlim([-7000, 7000])
        self.ax.set_ylim([-7000, 7000])
        self.ax.set_zlim([-7000, 7000])
        self.ax.set_xlabel('X (km)')
        self.ax.set_ylabel('Y (km)')
        self.ax.set_zlabel('Z (km)')

        # --- Draw Earth ---
        self._draw_earth()

        # --- Satellite point ---
        self.satellite_plot = self.ax.plot(
            [], [], [],
            marker='o',
            color='yellow',
            markersize=6
        )[0]

        # --- Orbit trail ---
        self.orbit_path = self.ax.plot(
            [], [], [],
            'r-',
            linewidth=1
        )[0]

        # --- Store orbit history ---
        self.orbit_x = []
        self.orbit_y = []
        self.orbit_z = []

        # --- Animation ---
        self.ani = FuncAnimation(
            self.fig,
            self.update,
            interval=1000
        )

    def _draw_earth(self):
        u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
        earth_radius = 6371  # km

        x = earth_radius * np.sin(v) * np.cos(u)
        y = earth_radius * np.sin(v) * np.sin(u)
        z = earth_radius * np.cos(v)

        self.ax.plot_surface(x, y, z, color='blue', alpha=0.4)

    def update(self, frame):
        position, _ = get_position_velocity()

        # --- Update satellite position ---
        self.satellite_plot.set_xdata([position[0]])
        self.satellite_plot.set_ydata([position[1]])
        self.satellite_plot.set_3d_properties([position[2]])

        # --- Update orbit trail ---
        self.orbit_x.append(position[0])
        self.orbit_y.append(position[1])
        self.orbit_z.append(position[2])

        self.orbit_path.set_data(self.orbit_x, self.orbit_y)
        self.orbit_path.set_3d_properties(self.orbit_z)

        return self.satellite_plot, self.orbit_path


# ---- Run ----
orbit_anim = OrbitAnimation()
plt.show()
