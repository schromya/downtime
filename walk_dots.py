import math
from matplotlib import pyplot as plt
from matplotlib import animation
from pynput import keyboard
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
                 a_step: float = 0.01, 
                 b: float = 0, # X position of center of circle
                 ):

        self.x = x_init
        self.x_min = x_min
        self.x_max = x_max
        self.x_step = x_step
        self.r = r
        self.a = a
        self.a_step = a_step
        self.b = b

        self.y = 0

        self.move_right() # Calculate y correctly for x=-1


    def move_right(self):
        """
        Calculates y and then increments x by x_step and a by a_step. 
        """
        self.a += self.a_step
        self.x += self.x_step + self.a_step
        self._bound_radial_movement()

        self.y = -math.sqrt(self.r ** 2 - (self.x - self.a) ** 2) + self.b
        
    def move_left(self):
        """
        Calculates y and then increments x by x_step and decrements a by a_step. 
        """
        self.a -= self.a_step
        self.x += self.x_step - self.a_step
        self._bound_radial_movement()

        self.y = -math.sqrt(self.r ** 2 - (self.x - self.a) ** 2) + self.b
        

    def _bound_radial_movement(self):
        """
        Bounds between x_min + self.a and x_max + self.a.
        """
        if self.x > self.x_max + self.a:
            self.x = self.x_max + self.a
            self.x_step *= -1
        elif  self.x  < self.x_min + self.a:
            self.x = self.x_min + self.a
            self.x_step *= -1


class KeyboardHandler:
    a_pressed = False
    d_pressed = False

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char('a'):
            self.a_pressed = True
        elif key ==  keyboard.KeyCode.from_char('d'):
            self.d_pressed = True


    def on_release(self, key):
        if key == keyboard.KeyCode.from_char('a'):
            self.a_pressed = False
        elif key == keyboard.KeyCode.from_char('d'):
            self.d_pressed = False

    def __init__(self):
        self.a_pressed = False
        self.d_pressed = False
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()



pos = math.cos(math.radians(65))  # To make 180-65-65 = 50 deg total stride
appendages = [
    # Connected to lower torso (0,0)
    {'plot': None, 'data': semicircle(-2*pos, -2*pos, 2*pos, 0.04, 2, 0, 0.04, 0)},  # Leg 1 
    {'plot': None, 'data': semicircle(2*pos, -2*pos, 2*pos, 0.04, 2, 0, 0.04, 0)},  # Leg 2
    
    # Connected to upper torso (0, 2) 
    {'plot': None, 'data': semicircle(-1*pos, -1*pos, 1*pos, 0.02, 1, 0, 0.04, 2)},  # Arm 1
    {'plot': None, 'data': semicircle(1*pos, -1*pos, 1*pos, 0.02, 1, 0, 0.04, 2)},  # Arm 2
]

fig = plt.figure(figsize=(15, 4))
ax = plt.axes(xlim=(-20, 20), ylim=(-5, 5))

# Set dot appendages
for appendage in appendages:
    appendage['plot'], = ax.plot([appendage['data'].x],[appendage['data'].y], 'r-')

# Connect torso and head
torso, = ax.plot([appendages[0]['data'].a,appendages[0]['data'].a],[0,3], 'r-')
head, = ax.plot([appendages[0]['data'].a],[3], 'ro', markersize=20)

key_handler = KeyboardHandler()

# animation function.  This is called sequentially
def animate(i, key_handler):

    for appendage in appendages:
        # Move appendages
        if key_handler.a_pressed:
            appendage['data'].move_left()
        elif key_handler.d_pressed:
            appendage['data'].move_right()

        # Plot appendages and attach them to torso
        appendage['plot'].set_data([appendage['data'].x, appendage['data'].a],[appendage['data'].y, appendage['data'].b]) 

    # Plot head and torso
    torso.set_data([appendages[0]['data'].a,appendages[0]['data'].a],[0,3])
    head.set_data([appendages[0]['data'].a],[3])


    return appendage['plot'],

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=200, interval=10, fargs=(key_handler,))

plt.show()