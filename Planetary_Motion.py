from turtle import Turtle  # Used to draw planet trajectories
import math

G = 1

class planet:
    def __init__(self, name, rad, mass, dist, color, vx, vy):

        """ Initialising Varibales """
        self.name = name # Name of planet
        self.rad = rad # Radius of planet
        self.mass = mass # Mass of planet
        self.dist = dist # Distance from the star        
        self.x = dist # Initial position (x,y)
        self.y = 0. 
        self.vx = vx # Initial velocity in x
        self.vy = vy # Initial velocity in y
        self.color = color # Color to draw trajectory (used by turtle)
        """ Setting up Turtle """
        self.p = Turtle() # Planet 'p' is drawn using Turtle
        self.p.color(self.color)
        self.p.shape("circle")

        self.p.up() # Pen up i.e. path is not traced when the planets moves to initial position
        self.p.goto(self.x, self.y)
        self.p.down() # Pen down, trajectory will now be traced
        """  """
    def getName(self):
        return self.name

    def getRad(self):
        return self.rad

    def getMass(self):
        return self.mass

    def getDist(self):
        return self.dist

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def movePos(self, nX, nY):
        self.x = nX
        self.y = nY
        self.p.goto(nX, nY)

    def getVX(self):
        return self.vX

    def getVY(self):
        return self.vY

    def setXV(self, newVX):
        self.vX = newVX

    def setYV(self, newVY):
        self.vY = newVY


class star:

    """ Initialise the Star class """
    def __init__(self, name, radius, mass, color, x, y):
        self.name = name
        self.rad = radius
        self.m = mass
        self.c = color
        self.x = x
        self.y = y

        """Set the given position of each planet """
        self.mw = Turtle()
        self.mw.up()
        self.mw.goto(self.x, self.y)
        self.mw.down()
        self.mw.dot(self.rad, self.c)

    def getMass(self):
        return self.m

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return self.name

class solar_system(planet):
    """ Initialise solar system class """
    def __init__(self, star):
        self.star = None
        self.planets = []
        self.mw = Turtle()
        self.mw.ht()

    def add_planet(self, planet):
        self.planets.append(planet)
    
    def add_star(self, star):
        self.star = star

    def rotate_planet(self):
        """ Here we define how each planet will orbit the star  """
        for p in self.planets:

            rx = self.star.getX() - p.getX() # Finding the components of the vector from the star to the planet
            ry = self.star.getY() - p.getY()   

            r = math.sqrt(rx ** 2 + ry ** 2) # the magnitude of the above vector       

            accX = G * self.star.getMass() * rx / r ** 3 # Acceleration of the planet found using Newton's Law of Gravitation
            accY = G * self.star.getMass() * ry / r ** 3            


Sun = star("Sun",150.0,15000.0,"yellow",0,0)
p1 = planet("P1", 19, 20,220,"green", 0.0,10) # Check if planet is drawn
p2 = planet("P1", 19, 20,300,"blue", 0.0, 15.0)

mw = solar_system(Sun)
mw.add_star(Sun)
mw.add_planet(p1)
mw.add_planet(p2)
time = 10

for t in range(time):
    mw.rotate_planet()
        
input("Press 'Enter' to exit...")
