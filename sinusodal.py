import math
from matplotlib import pyplot as plt
from matplotlib import animation

class dot:

    t = 0  # Time (s)
    y = 0

    def __init__(self,
                 a: float = 1,  # Amplitude (m)
                 w: float = 1,  # Angular frequency (rad/s)
                 p: float = 1 # Phase (rad)
                 ):

        self.a = a
        self.w = w
        self.p = p

    def move_sin_position(self):
        """
        Bound t between 0 and 100
        """
        self.t += 1
        if self.t > 100:
            self.t = 0
        self.y = self.a * math.sin(self.w * self.t + self.p)


dot = dot(1,1,1)
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(-10, 10))
d, = ax.plot([dot.t],[dot.y], 'ro')

# animation function.  This is called sequentially
def animate(i):
    dot.move_sin_position()
    d.set_data([dot.t],[dot.y])
    #d, = ax.plot([dot.t],[dot.y], 'ro')
    return d,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()