""" Integrators for Planetary Motion """

""" Velocity-Verlet

Variables:
r ~ Initial Position
v ~ Initial Velocity
a ~ Acceleration
dt ~ Time Step

 """
def pos_Verlet(r,v,a,dt):
     r += v*dt + ((a*dt**2)/2)
     return r

def vel_Verlet(v, a, new_a, dt):
    v += (a+new_a)*dt/2
    return v