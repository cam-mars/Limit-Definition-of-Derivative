import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def f(x): #define the f = e^x
    return np.exp(x)


x = 8.5  #initial x
h_values = np.linspace(1.5, 0.01, 50) #decreasing h
x_vals = np.linspace(5, 10, 100) #x range
fig, ax = plt.subplots(figsize=(8, 5)) #make fig

ax.plot(x_vals, f(x_vals), label=r'$e^x$', color='b') #graph f(x)
scatter_f_x = ax.scatter([], [], color='black', s=25, label="Intersection Points") #graph intersection pts
secant_line, = ax.plot([], [], color='r', label="Secant Line") #graph secant line
hLine, = ax.plot([], [], color='black', linestyle='--', label="h") #graph h line
#for tangent line
m_tangent = f(x)  #slope of e^x = e^x
tangent_x = np.linspace(min(x_vals), max(x_vals), 100)  #extend line across graph
tangent_y = m_tangent*(tangent_x - x) + f(x)  # Tangent line equation
ax.plot(tangent_x, tangent_y, color='g', label="Tangent Line") #graph


# Labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Secant Line Approaching the Tangent")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)
#x,x+h, etc labels
x1_label = ax.text(x, 0, r"$x$", ha='center', va='top', fontsize=12, color='black')
x2_label = ax.text(x + h_values[0], 0, r"$x+h$", ha='center', va='top', fontsize=12, color='black')
f_x_label = ax.text(x, f(x), r"$f(x)$", ha='right', va='bottom', fontsize=12, color='black')
f_xh_label = ax.text(x + h_values[0], f(x + h_values[0]), r"$f(x+h)$", ha='right', va='bottom', fontsize=12, color='black')
h_label = ax.text(x + h_values[0] / 2, 2000, r"$h$", ha='center', va='top', fontsize=12, color='black', fontweight = 'bold')

ax.text(
    5,  # Midpoint of x1 and x2
    7000,  # Slightly above the midpoint of f(x1) and f(x2)
    r"Slope of secant line = $\frac{rise}{run}$ = $\frac{f(x+h) - f(x)}{(x+h) - x}$",
    ha='left', fontsize=12, color='black'
)

def update(frame): #animation fcn
    h = h_values[frame]  # Get current h value
    x1, x2 = x, x+h  # Points on x-axis
    y1, y2 = f(x1), f(x2)  # Compute corresponding y-values
    m = (y2-y1)/(x2-x1) #slope

    secant_x = np.linspace(min(x_vals), max(x_vals), 100) #sec x vals extend across x range
    secant_y = m*(secant_x-x1) + y1 #declare sec y vals

    secant_line.set_data(secant_x, secant_y) #update sec line
    scatter_f_x.set_offsets(np.column_stack([[x1, x2], [y1, y2]])) #update intersection pts
    
    h_x = np.array([x1, x2]) #h x vals
    h_y = np.array([0, 0]) #h y vals
    hLine.set_data(h_x, h_y) #update h line
    
    
    x1_label.set_x(x1)
    x2_label.set_x(x2)  
    f_x_label.set_x(x1)
    f_x_label.set_y(y1)
    
    f_xh_label.set_x(x2)
    f_xh_label.set_y(y2)
    
    h_label.set_x(x1 + h / 2)

    return secant_line, scatter_f_x, x1_label, x2_label, f_x_label, f_xh_label, hLine, h_label
ani = animation.FuncAnimation(fig, update, frames=len(h_values), interval=250, blit=True)

plt.show()
