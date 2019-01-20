from turtle import Turtle  # Used to draw planet trajectories

class Planet(object):
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

class Star(object):

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

Sun = Star("Sun",150.0,15000.0,"yellow",0,250)
Star2 = Star("Star2", 200.0,20000.0,"purple",0,0)
p1 = Planet("P1", 19, 20,220,"green", 0.0,10) # Check if planet is drawn


        
input("Press 'Enter' to exit...")
