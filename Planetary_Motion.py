from turtle import Turtle  # Used to draw planet trajectories
import math
import numpy as np
import integrators as ig  


class planet:
    def __init__(self, name, rad, mass, dist, color, vx, vy):

        """ Initialising Varibales """
        self.name = name # Name of planet
        self.rad = rad # Radius of planet
        self.mass = mass # Mass of planet
        self.dist = dist # Distance from the star   
        self.r = np.array([dist,0.]) # Initial position    
        self.v = np.array([vx,vy]) # Initial velocity
        self.color = color # Color to draw trajectory (used by turtle)
        """ Setting up Turtle """
        self.p = Turtle() # Planet 'p' is drawn using Turtle
        self.p.color(self.color)
        self.p.shape("circle")

        self.p.up() # Pen up i.e. path is not traced when the planets moves to initial position
        self.p.goto(self.r)
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

    def getR(self):
        return self.r
    
    def movePos(self, r):
        self.r = r
        self.p.goto(self.r)

    def getV(self):
        return self.v

    def setV(self, newV):
        self.v = newV

class star:

    """ Initialise the Star class """
    def __init__(self, name, radius, mass, color, x, y):
        self.name = name
        self.rad = radius
        self.m = mass
        self.c = color
        self.r = np.array([x,y])
        

        """Set the given position of each planet """
        self.mw = Turtle()
        self.mw.up()
        self.mw.goto(self.r)
        self.mw.down()
        self.mw.dot(self.rad, self.c)

    def getMass(self):
        return self.m

    def getR(self):
        return self.r 

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
            d = self.star.getR() - p.getR() # Vector from planet to star                        
            mag_d = np.sqrt(r.dot(r)) # Magnitude of d        
            a = G * self.star.getMass() * d / mag_d ** 3 # Acceleration due to the Star acting on planet
            
            """ Move planet according to the acceleration due to gravity """
            r = ig.pos_Verlet(p.getR(),p.getV(),a,dt) # Calculates the new position r    
            p.movePos(r) # Moving the planet to the new position
            d = self.star.getR() - p.getR()
            mag_d = np.sqrt(r.dot(r))
            new_a = G * self.star.getMass() * d / mag_d**3 # Acceleration at the new position
            v = ig.vel_Verlet(p.getV(),a,new_a,dt) # Velocity of planet
            p.setV(v) 
         



Sun = star("Sun",150.0,15000.0,"purple",0,0,)
p1 = planet("P1", 19, 20,220,"green", 0.0,10) 
p2 = planet("Planet 2", 30, 80, 340, "blue", 0.0, 7.7)
p3 = planet("Planet 3", 40, 110, 380, "red", 0.0, 7.3)
mw = solar_system(Sun)
mw.add_star(Sun)
mw.add_planet(p1)
mw.add_planet(p2)
mw.add_planet(p3)

""" Variables that affect the simulation """
dt = 0.01
G = 2.5
time = 100000

for t in range(time):
    mw.rotate_planet()
        
input("Press 'Enter' to exit...")
