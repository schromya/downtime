import math
from matplotlib import pyplot as plt
from matplotlib import animation

class dot:

    t = -1  # Time (s)
    y = 0
    prev_t = 0
    prev_y = 0

    def __init__(self,
                 a: float = 1,  # Amplitude (m)
                 w: float = 1,  # Angular frequency (rad/s)
                 p: float = 1 # Phase (rad)
                 ):

        self.a = a
        self.w = w
        self.p = p

        self.move_sin_position() # Calculate y correctly for t=0

    def move_sin_position(self):
        """
        Increments t by 1/10 of a sec and calculates y. Bound t between 0 and 100
        """

        RESET_TIME = 100
        INCREMENT_AMOUNT = 1/10

        self.prev_t = self.t
        self.prev_y = self.y

        self.t += INCREMENT_AMOUNT
        if self.t > RESET_TIME:
            self.t = 0

        self.y = self.a * math.sin(self.w * self.t + self.p)

        if self.t == 0:  # Reset previous values if dot reset
            self.prev_t = self.t
            self.prev_y = self.y



dot = dot(1,1,1)
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(-10, 10))
d, = ax.plot([dot.t],[dot.y], 'ro')

# animation function.  This is called sequentially
def animate(i):
    dot.move_sin_position()
    d.set_data([dot.t],[dot.y]) # Move dot 
    ax.plot([dot.prev_t, dot.t], [dot.prev_y, dot.y], 'b-') # Graph line between points

    return d,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=200, interval=10)

plt.show()