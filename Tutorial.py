#Python Tutorial
# Jared Rivera 2018

# '#' means this line is a comment, so Python ignores it when running

#This script can serve as a reference for learning some Python elements, 
#as well as a place to take models for common programming atructures.

###############################################################################

#First, let's start with libraries. Programming languages know how to do some
#basic things from the start, but we need to import functions made by other 
#users to make our lives easier and not re-code everything.
#Some common ones are seen below:

import numpy as np
import math as math 
import matplotlib.pyplot as plt 

#Notice we have to import the library with some name for our local environment.

#NumPy is the fundamental package for scientific computing with Python. 
#It contains among other things:
#-a powerful N-dimensional array object
#-sophisticated (broadcasting) functions
#-tools for integrating C/C++ and Fortran code
#-useful linear algebra, Fourier transform, and random number capabilities
#-Besides its obvious scientific uses, NumPy can also be used as an efficient 
#multi-dimensional container of generic data. 
#Arbitrary data-types can be defined. This allows NumPy to seamlessly and 
#speedily integrate with a wide variety of databases.

#See https://docs.python.org/3/library/math.html for the math library info.

#See https://matplotlib.org/api/pyplot_api.html for plots, which we'll cover.

###############################################################################

#Next is variable declaration. This is simply done with an "equals" sign:

c = 299792458 #speed of light in m/s

#That's a simple scalar integer. We can also have vectors:

x_hat = [1,0,0]

#This is the x unit vector. We can call for certain components of it,
#but we must note the index starts at zero.

x_hat_x = x_hat[0]

#This calls for the first (x) component of the vector, which is 1.

#Vectors are a subset of arrays or maatrices, where we can have any size we
#want as in the 3-D identity matrix,

I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#It's basically a vector of vectors, and indexing is simple. If I want the
#middle entry of the matrix, remembering to index from zero,

middle = I[1][1]

#How can I index for the bottiom right entry of the matrix?

#Those are the basic data structures.

###############################################################################

#Let's move on to actual operations. They're pretty easy.

#Say I want to convert from Celcius to Kelvin. I know I need to add 273.15 to
#my value, but how do I tell the computer? Like this:

degC = 25
degK = degC + 273.15

#Now say I want to tell an American what the temperature is, we are going to
#need more operations (namely multiplication and multiplication) to 
#get to Fahrenheit.

degF = (9/5)*degC + 32

#How can I convert directly from K to F? 
#Note that for subtraction we just use '-'.

#For exponentiation, we just use '**'. So if I want to know how to convert from
#pH to [H+], we just take

pH = 7
concentration_H_plus = 10**(-pH)

###############################################################################

#IF statements are what we'll use for logic or piecewise functions. Refer to
#https://www.w3schools.com/python/python_conditions.asp for more logic.

#Say I want to square any input smaller than 3 and add 5 to any input greater
#than or equal to 3, this may be some interpolated function. We can write

input = 2
input1 = 6

if input < 3:
    input = input**2
elif input >=3:
    input = input + 5
else:
    print('How did you break the script!')


#So try each input option above, remove the 1 or the 2 qnd check the variable 
#using the console after. Notice the if, else if, and else conditions. Note
#that we've only discussed numerical structures. Strings of characters exist!


###############################################################################

#FOR loops are the loop structure we'll see the most. Other types exist but
#in the learning phase we'll ignore them for now as you may damage your device.

#Say I wanted to sum the first 100 integers. We'll implement the sum as

sum_integers = 0 #initialize
for i in range(1,101):
    sum_integers = sum_integers +i
    
#Check the console to find the correct answer. Notice our summation limits 
#look a little wweird due to that indexing from zero quirk.

###############################################################################

#Plotting is essential for communicating analysis, so let's try it!
    
#Say I want to plot what my sum from 1 to 100 looks like with each integer
#step. We need to use a different structure to save that information.
    
sum_plot = [0]*102
sum_plot[0] = 0
index_plot = [0]*102

for i in range(1,101):
    index_plot[i+1] = i
    sum_plot[i+1] = sum_plot[i] + i
    
#Now we'll make the 2D plot
    
plt.plot(index_plot,sum_plot)
plt.xlabel('Index')
plt.ylabel('Sum')
plt.title('Gauss Trick')


#That's all for now. Never be afraid to google what you don't know!

























