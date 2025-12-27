#plot the orbit
satellite_plot= ax.plot([],[],[],'ro',color='yellow',linewidth=1,markersize=6)[0]
#to store past satellite position
orbit_path=ax.plot([],[],[],'r-',linewidth=1)[0]
#Real-time animation
def update(frame):
    position,_=get_position_velocity()
    satellite_plot.set_xdata([position[0]])
    satellite_plot.set_ydata([position[1]])
    satellite_plot.set_3d_properties(position[2])
    #update orbit path
    if not hasattr(update,'orbit_positions'):
        update.orbit_positions={'x':[],'y':[],'z':[]}
    update.orbit_positions['x'].append(position[0])
    update.orbit_positions['y'].append(position[1])
    update.orbit_positions['z'].append(position[2])
    orbit_x=update.orbit_positions['x']
    orbit_y=update.orbit_positions['y']
    orbit_z=update.orbit_positions['z']
    
    orbit_path.set_data(orbit_x,orbit_y)
    orbit_path.set_3d_properties(orbit_z)
    return satellite_plot, orbit_path
ani=FuncAnimation(fig,update,interval=1000)

plt.show()