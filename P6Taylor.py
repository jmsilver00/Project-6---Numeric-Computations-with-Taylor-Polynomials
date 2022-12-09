#Jacob Silveira
#CST-305
#11/28/2022

#Differential Equations solved:
#Part 1:
#a. y" -2xy' +x^2y = 0; y(0) = 1, y'(0) = -1
#b. y" - (x-2)y' + 2y = 0; y(3) = 6, y'(3) = 1, near x = 3;
#Part 2:
#(x^2 + 4)y" + y = x; x = 0

#import all needed libraries 
import numpy as np #numpy will be used for math                 
import matplotlib.pyplot as plt #matplotlib will be used to graph mathematical results
from scipy.special import factorial #factorial function 

#Part 1) a) 
def part1A(x):
    #values for final y(x)
    y0 = 1                   #value of the first term               
    y1 = -x                  #value of the second term           
    y2 = 0                   #value of the third term             
    y3 = -1 / 3 * pow(x, 3)  #value of the fourth term     
    y4 = -1 / 12 * pow(x, 4) #value of the fifth term    
    return  y0 + y1 + y2 + y3 + y4  #return all as an added equation
    
print("The value of y(x) when x = 3.5 is: ")
print(part1A(3.5))

#Part 1) b) 
def part1B(x):
    #value for final y(x)
    y0 = 6                                  #value of the first term 
    y1 = (x-3)                              #value of the second term  
    y2 = -11/2 * pow((x-3), 2)              #value of the third term   
    y3 = -12/6 * pow((x-3), 3)              #value of the fourth term 
    y4 = -12 / factorial(4) * pow((x-3), 4) #value of the fifth term      
    return y0 + y1 + y2 + y3 + y4           #return all as an added equation 

#For Part 2 
def part2(x, a0, a1):
    #For even a0 from worked problem 
    a = a0*(1-(1/8)*pow(x,2)+(1/128)*pow(x,4)-(13/15360)*pow(x,6)+(403/3440640)*pow(x, 8)-(7657/412876800)*pow(x,10))
    #For odd a1 from worked problem 
    b = a1*(x-(1/24)*pow(x,3)+(7/1920)*pow(x,5)-(7/15360)*pow(x,7)+(301/4423680)*pow(x, 9))
    return a + b #return a0+a1
       
dt = 0.02 #dt val 
numSteps = 10000 #number of steps for graph 

#graph space
xspace = np.linspace(-100, 100, numSteps) 
results_A = np.empty(numSteps)  #y for Part 1) A)                   
results_B = np.empty(numSteps)  #y for Part 1) B)              
results_2 = np.empty(numSteps)  #y for Part 2)                 
    
#creating array to store the values 
for i in range(-10000, 10000):
    results_A[i] = part1A(i*dt)        #Part 1) A)
    results_B[i] = part1B(i * dt)      #Part 1) B)
    results_2[i] = part2(i * dt, 2, 2) #Part 2)  

#creating plots 
plt.title("Taylor Series Part 1. a)")  #title
plt.xlabel("x")                        #x axis label
plt.ylabel("y")                        #y axis label
plt.plot(xspace, results_A)            #plot
plt.show()                             #display

plt.title("Taylor Series Part 1. b)")  #title
plt.xlabel("x")                        #x axis label
plt.ylabel("y")                        #y axis label
plt.plot(xspace, results_B)            #plot
plt.show()                             #display

plt.title("Part 2")                    #title
plt.xlabel("x")                        #x axis label
plt.ylabel("y")                        #y axis label
plt.plot(xspace, results_2)            #plot
plt.show()                             #display






