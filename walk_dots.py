import math
from matplotlib import pyplot as plt
from matplotlib import animation

class semicircle:
    """
    Dot moves in lower half of semicircle (-y)
    """
    def __init__(self,
                 x_init: float = -1,
                 x_min: float = -1, 
                 x_max: float = 1, 
                 x_step: float = 0.01,
                 r: float = 1, # Radius of semicircle
                 a: float = 0, # X position of center of circle
                 b: float = 0, # X position of center of circle
                 ):

        self.x = x_init
        self.x_min = x_min
        self.x_max = x_max
        self.x_step = x_step
        self.r = r
        self.a = a
        self.b = b

        self.y = 0

        self.move() # Calculate y correctly for x=-1

    def move(self):
        """
        Calculates y and then increments x by x_step. Bound between x_min and x_max.
        """

        self.y = -math.sqrt(self.r ** 2 - (self.x - self.a) ** 2) + self.b

        self.x += self.x_step
        if self.x > self.x_max or self.x < self.x_min:
            self.x_step *= -1
            self.x += self.x_step


pos = math.cos(math.radians(65))  # To make 180-65-65 = 50 deg total stride
appendages = [
    # Connected to lower torso (0,0)
    {'plot': None, 'data': semicircle(-2*pos, -2*pos, 2*pos, 0.04, 2, 0, 0), 'connection': (0,0)},  # Leg 1 
    {'plot': None, 'data': semicircle(2*pos, -2*pos, 2*pos, 0.04, 2, 0, 0), 'connection': (0,0)},  # Leg 2

    # Connected to upper torso (0, 2) 
    {'plot': None, 'data': semicircle(-1*pos, -1*pos, 1*pos, 0.02, 1, 0, 2), 'connection': (0,2)},  # Arm 1
    {'plot': None, 'data': semicircle(1*pos, -1*pos, 1*pos, 0.02, 1, 0, 2), 'connection': (0,2)},  # Arm 2
]

fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))

# Set dot appendages
for appendage in appendages:
    appendage['plot'], = ax.plot([appendage['data'].x],[appendage['data'].y], 'r-')

# Connect torso and head
torso, = ax.plot([0,0],[0,3], 'r-')
head, = ax.plot([0],[3], 'ro', markersize=20)

# animation function.  This is called sequentially
def animate(i):

    for appendage in appendages:
        appendage['data'].move() # Move appendages
        # Plot appendages and attach them to torso
        appendage['plot'].set_data([appendage['data'].x, appendage['connection'][0]],[appendage['data'].y, appendage['connection'][1]]) 

    return appendage['plot'],

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=200, interval=10)

plt.show()