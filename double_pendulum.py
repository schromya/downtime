import math
from matplotlib import pyplot as plt
from matplotlib import animation

class double_pendulum:
    """
    https://personal.math.ubc.ca/~israel/m215/doublpen/doublpen.html#:~:text=A%20double%20pendulum%20consists%20of%20two%20balls%20hanging,can%20use%20a%20linear%20approximation%20to%20their%20motion.
    """

    x0, y0 = 0, 0  # Where pendulum is "tied"
    x1, y1 = 0, 0  # Joint 1
    x2, y2 = 0, 0  # Joint 2

    t = 0

    def __init__(self,
                 th1: float = 0,  # Theta, Angle joint 1 (rad)
                 th2:float = 0,  # Theta, Angle joint 2 (rad)
                 m1: float = 1,  # Mass of joint 1 (kg)
                 m2: float = 1,  # Mass of joint 2 (kg)
                 l1: float = 1,  # Length of joint 1 (m)
                 l2: float = 1,  # Length of joint 1 (m)
                 ):

        self.th1 = th1
        self.th2 = th2
        self.m1 = m1
        self.m2 = m2
        self.l1 = l1
        self.l2 = l2

        self.update_positions() # Calculate initial positions

    def update_positions(self):
        g = 9.8  # Gravity (m/s)
        self.th1 = - (self.m1 + self.m2) * g * self.th1 / (self.m1 * self.l1) + self.m2 * g * self.th2 / (self.m1 * self.l1)
        self.th2 = (self.m1 + self.m2) * g * self.th1 / (self.m1 * self.l2) - (self.m1 + self.m2) * g * self.th2 / (self.m1 * self.l2)

        # Scale by time
        # self.t += 1
        # w = 20  # Angular frequency (rad/s)
        # self.th1 *= math.cos(w * self.t)
        # self.th2 *= math.cos(w * self.t)

        self.x1 = self.l1 * math.sin(self.th1)
        self.y1 = self.l1 * math.cos(self.th1)
        self.x2 = self.l2 * math.sin(self.th2) + self.x1
        self.y2 = self.l2 * math.cos(self.th2) + self.y1


pen = double_pendulum(1,2, 1,1, 1,1)
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-3, 3), ylim=(-3, 3))
d, = ax.plot([pen.x0, pen.x1, pen.x2],[pen.y0, pen.y1, pen.y2], 'ro-')

# animation function.  This is called sequentially
def animate(i):
    pen.update_positions()
    #d.set_data([dot.t],[dot.y]) # Move dot 
    d.set_data([pen.x0, pen.x1, pen.x2],[pen.y0, pen.y1, pen.y2]) # Move pendulum

    return d,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=200, interval=200)

plt.show()