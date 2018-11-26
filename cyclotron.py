import numpy as np
import math as math
import matplotlib.pyplot as plt  # Tools and libraries
from mpl_toolkits.mplot3d import Axes3D
from decimal import Decimal

c = 3.0E08  # Speed of Light (scalar)
e = [5000000.0, 0.0, 0.0]  # Electric Field (vector)
b = [0.0, 0.0, -1.5]  # Magnetic Field (vector)
bmag = np.linalg.norm(b)  # Magnitude of Magnetic Field (vector)


class Particle:  # Set up the structure and properties of a particle
    def __init__(self, pos, vel, mass, charge):
        self.pos = pos
        self.vel = vel  # Properties of the particle
        self.mass = mass
        self.charge = charge

    def radius(self, b):
        b = np.linalg.norm(b)
        speed = np.linalg.norm(self.vel)
        radius = speed * self.mass / (self.charge * b)
        return radius
        # Properties of the particle's motion

    def period(self):
        field = np.linalg.norm(b)
        period = 2.0 * math.pi * self.mass / (field * self.charge)
        return period


# choose a proton as the particle, describe in 3 Dimension 
proton = Particle([0.00, 0.0, 0.0], [0.05 * c, 0.0, 0.0], 1.67E-27, +1.60E-19)

# We accelerate the particle with the electric field when it crosses the gap
gap_size = 0.5 * proton.radius(b)

###################################################################################
# Given position and velocity, the function returns acceleration as an array in 3D
# The magnetic field is applied where x > 0 or  x < - gap_size
# The electric field is applied where x < 0 and x > - gap_size
###################################################################################

jumps = 0
jumps_max = 46
count = 0

<<<<<<< HEAD

def a(q_over_m, r, v):
    global count, jumps  # if you use the global statement, the variable will become available
    if jumps >= jumps_max:  # "outside" the scope of the function, effectively becoming a global variable
        # No acceleration
        a = 0.0
    elif r[0] >= 0 or r[0] <= -gap_size:
        a = np.cross(v, b)
        a = a * q_over_m
        if count:
            jumps += 1
            velo[jumps] = np.linalg.norm(v)
            count = 0
    else:
        a = np.array(e)
        a = a * q_over_m
        if r[1] > 0:
            a = -a
        count += 1
    return a
=======
def a( q_over_m, r, v ):
	global count, jumps                # if you use the global statement, the variable will become available 
	if jumps >= jumps_max:			# "outside" the scope of the function, effectively becoming a global variable
		# No acceleration
		a = 0.0						#Finishes the cyclotron motion
	elif r[0] >= 0 or r[0] <= -gap_size:		#Outside gap, subject to magnetic field
		a = np.cross(v, b) 
		a = a * q_over_m
		if count!=0:						
			jumps += 1							#Effectively gives us a way to add to the jump variable only when the particle crosses the E field to B field threshold
			velo[jumps] = np.linalg.norm(v)		#Unnecessary to the plot, but so far allows us to get the final velocity using the print function at the bottom of the code
			count = 0							# Set to 0 so that we only add to the jump variable once
	else: 										#Inside gap, subject to electric field
		a = np.array(e)	
		a = a * q_over_m
		if r[1] > 0:							#Reverses acceleration direction so that the particle does not decelerate 'round the circle
			a = -a
		count = 1
	return a
>>>>>>> 5bacee0b38cd0ee6c6e87dbbe141f04bc08d3d37


###############################################################################
#  
#    Solving Equations of Motions Using RK4
#
###############################################################################


# initializes array that will hold the velocity of particle
# each time it gains velocity (crosses gap)
velo = np.zeros((jumps_max + 1,))
velo[0] = np.linalg.norm(proton.vel)


def rk4(particle, iterations, desired_value):
<<<<<<< HEAD
    RK4_pos = []
    RK4_vel = []

    n = 400
    h = particle.period() / n
    q_over_m = particle.charge / particle.mass

    p_0 = np.array(particle.pos)
    v_0 = np.array(particle.vel)

    for i in range(iterations + 10):
        i += 1
        p_i = p_0
        v_i = v_0

        k1 = h * a(q_over_m, p_i, v_i)
        l1 = h * v_i

        k2 = h * a(q_over_m, p_0 + (l1 * 0.5), v_0 + (k1 * 0.5))
        l2 = h * (v_0 + (k1 * 0.5))

        k3 = h * a(q_over_m, p_0 + (l2 * 0.5), v_0 + (k2 * 0.5))
        l3 = h * (v_0 + (k2 * 0.5))

        k4 = h * a(q_over_m, p_0 + l3, v_0 + k3)
        l4 = h * (v_0 + k3)

        v_0 = v_0 + (k1 + 2.0 * (k2 + k3) + k4) / 6.0
        p_0 = p_0 + (l1 + 2.0 * (l2 + l3) + l4) / 6.0

        if desired_value == 'velocity':
            vel_mag = np.linalg.norm(v_0)
            RK4_vel.append(vel_mag)
            value = RK4_vel
        elif desired_value == 'position':
            RK4_pos.append(p_0)
            value = RK4_pos

    return value

=======
	global n, h, jumps
	RK4_pos = []
	RK4_vel = []
	
	n=400
	h = particle.period() / n
	q_over_m = particle.charge / particle.mass
	
	p_0 = np.array(particle.pos) 
	v_0 = np.array(particle.vel) 
	
	for i in range(iterations):
		p_i = p_0
		v_i = v_0
	
		k1 = h * a( q_over_m, p_i, v_i )
		l1 = h * v_i
		
		
		k2 = h * a( q_over_m, p_0 + (l1 * 0.5), v_0 + (k1 * 0.5) )
		l2 = h * (v_0 + (k1 * 0.5))
		

		k3 = h * a( q_over_m, p_0 + (l2 * 0.5), v_0 + (k2 * 0.5) )
		l3 = h * (v_0 + (k2 * 0.5))
	
		k4 = h * a( q_over_m, p_0 + l3, v_0 + k3 )
		l4 = h * (v_0 + k3)
		

		v_0 = v_0 + (k1 + 2.0 * (k2 + k3) + k4) / 6.0
		p_0 = p_0 + (l1 + 2.0 * (l2 + l3) + l4) / 6.0
	
		
		
		if desired_value == 'velocity': 
			vel_mag = np.linalg.norm(v_0)
			RK4_vel.append(vel_mag)
			value = RK4_vel
		elif desired_value == 'position': 
			RK4_pos.append(p_0)
			value = RK4_pos
	jumps=0
	
		
	return value
	
>>>>>>> 5bacee0b38cd0ee6c6e87dbbe141f04bc08d3d37

#######################################################################################
#  
#    Since this program graphs many figures, it is more convenient and efficient
#		to create a plot function. 
#		This function can accomodate 2D and 3D plots, note the first argument
#		must be a 3 element list, whose entries are labels for x,y,z coordinates, respectively.
#
#########################################################################################

def plot(coord_labels, title, dimension, x, y, z=0):
    fig = plt.figure()

    if dimension == '2d':
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(x, y)
    elif dimension == '3d':
        ax = fig.add_subplot(111, projection=dimension)
        ax.plot3D(x, z, y)
        ax.set_zlabel(coord_labels[2])

    ax.set_xlabel(coord_labels[0])
    ax.set_ylabel(coord_labels[1])
    ax.set_title(title)


###############################################################################
#  
#    Plotting Trajectory of Particle
#
###############################################################################


def position_plot(particle):
    x = []
    y = []
    z = []

    x.append(particle.pos[0])
    y.append(particle.pos[1])
    z.append(particle.pos[2])

    results = rk4(proton, 10000, 'position')

    for i in results:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])

    coordlabel = ["X-axis (m)", "Y-axis (m)", "Z-axis (m)"]
    plot(coordlabel, "Particle Trajectory in Cyclotron Accelerator", '3d', x, y, z)


###############################################################################
#  
#    velocity	vs. time plot
#
###############################################################################


def velocity_plot(particle):
<<<<<<< HEAD
    n = 400
    h = particle.period() / n

    v = rk4(proton, 10000, 'velocity')
    t = np.linspace(0, len(v) * h, len(v))

    coordlabel = ["Time (s)", "Velocity (m/s)", "Z-axis (m)"]
    plot(coordlabel, "Beam Velocity as a Function of Time", '2d', t, v)

    # prints final velocity
    final_velo = velo[len(velo) - 1]
    print(final_velo)

    # prints final time
    final_t = t[len(velo) - 1]
    print(final_t)

=======
	
	v = rk4(proton , 10000 ,'velocity')	
	t = np.linspace(0, len(v) * h, len(v))
	
	
	coordlabel = ["Time (s)","Velocity (m/s)","Z-axis (m)"]
	plot(coordlabel, "Beam Velocity as a Function of Time", '2d', t,v)
	

	#prints final velocity
	final_velo = velo[len(velo) - 1]
	print (final_velo)

	#prints final time
	final_t = t[len(velo) - 1]
	print (final_t)
>>>>>>> 5bacee0b38cd0ee6c6e87dbbe141f04bc08d3d37

###############################################################################
#  
#    velocity vs radius
#
###############################################################################


def vel_rad_plot(particle):
    radius = np.zeros((len(velo),))

    for item in range(1, len(velo) + 1):
        radius[item - 1] = velo[item - 1] * particle.mass / (particle.charge * bmag)

    coordlabel = ["Radius (m)", "Velocity (m/s)", "Z-axis (m)"]
    plot(coordlabel, "Beam Velocity at Various Extraction Radius", '2d', radius, velo)


velocity_plot(proton)
<<<<<<< HEAD
jumps = 0
position_plot(proton)
vel_rad_plot(proton)
plt.show()
=======
position_plot(proton)
vel_rad_plot(proton)
plt.show()



#################################################################################################################################################
# Goals #########################################################################################################################################
#################################################################################################################################################
# 1. Replacing the count variable with a simpler method of adding to the number of jumps?
#
#
#
##################################################################################################################################################
# Changelog ######################################################################################################################################
##################################################################################################################################################
# 1. Adjusted count variable to be less obtuse, instead functioning as a simple boolean
# 2. Removed a redundant assignment to i in the RK4's for loop
# 3. Made n and h global variables, so that defining them isn't required for the other functions
# 4. Removed a redundant +10 to the iterations in the RK4 for loop
# 5. Reset the jump variable to 0 at the end of the RK4 function so that it may be called again without having to reset the variable manually as
# before, deleted the associated assignement at the bottom of the code
#
>>>>>>> 5bacee0b38cd0ee6c6e87dbbe141f04bc08d3d37
