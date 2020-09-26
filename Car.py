# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:56:57 2020

@author: shubham
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#allocate arrays for plotting
#position
xt = []
yt = []
#velocity
dxt = []
dyt = []
#position gains
Kx = []
Ky = []
#velocity gains
Kdx = []
Kdy = []

#initital state
x = np.matrix([[0.0, 0.0, 0.0, 0.0]]).T

#initial uncertainity
P = np.diag([10000.0, 10000.0, 1000.0, 1000.0])

#define state space representation
dt = 0.1
A = np.matrix([[1.0, 0, dt, 0],
               [0, 1.0, 0, dt],
               [0, 0, 1.0, 0],
               [0, 0, 0, 1.0]])

C = np.matrix([[0, 0, 1.0, 0],
              [0, 0, 0, 1.0]])

#Measurement noise covariance matrix
R = np.matrix([[100.0, 0],
               [0, 100.0]])

#Process noise covariance Q
sv = 10.0

G = np.matrix([[0.5*dt*dt], [0.5*dt*dt], [dt], [dt]])
Q = G*G.T*sv*sv

size = 200
vx = 10
vy = 0

#mx = np.array(vx + np.random.randn(size))
#my = np.array(vy + np.random.randn(size))
#measurements = np.vstack((mx, my))

omega = 10
dt = 0.01
radius = 5
mx = []
my = []
for i in range(75):
    randm = np.random.randn(2)
    #omega = np.random.randn(1)
    #print(randm)
    mx.append(-radius*omega*math.sin(omega*dt) + randm[0])
    my.append(radius*omega*math.cos(omega*dt) + randm[0])
    dt = dt + 0.01
measurements = np.vstack((mx,my))
'''fig = plt.figure(figsize = (16,5))
plt.step(range(len(measurements[0])), mx)
plt.step(range(len(measurements[0])), my)
plt.ylabel('Velocity')
plt.xlabel('measurements')'''

def saveParameters(x, K):
    """Saves the matrix values at each time step.
    
    Args: x (system state), K (Kalman gains)
    
    Returns: None
    
    """
    xt.append(float(x[0]))
    yt.append(float(x[1]))
    dxt.append(float(x[2]))
    dyt.append(float(x[3]))
    Kx.append(float(K[0,0]))
    Ky.append(float(K[1,0]))
    Kdx.append(float(K[2,0]))
    Kdy.append(float(K[3,0]))

for n in range(len(measurements[0])):
    I = np.eye(4)
    x = A*x
    P = A*P*A.T + Q
    S = C*P*C.T + R
    K = (P*C.T)*np.linalg.inv(S)
    Z = measurements[:, n].reshape(2,1)
    y = Z - (C*x)
    x = x + (K*y)
    P = (I - K*C)*P
    saveParameters(x, K)

#plot velocity   
fig1 = plt.figure(figsize = (16, 9))
plt.step(range(len(measurements[0])), dxt, label = '$Vx$')
plt.step(range(len(measurements[0])), dyt, label = '$Vy$')
#plt.step(range(len(measurements[0])), mx, label = '$origVx$')
#plt.step(range(len(measurements[0])), my, label = '$origVy$')
#plt.step(range(size), mx)
#plt.step(range(size), my)
plt.legend(loc = 'best')
    
#plot positions
fig2 = plt.figure(figsize = (16,16))
plt.scatter(xt, yt, s = 20, c = 'blue', label = '$Position$')
plt.scatter(xt[0], yt[0], s = 100, c = 'red', label = '$Start$')
plt.scatter(xt[-1], yt[-1], s = 100, c = 'green', label = '$Goal$')
plt.axis('equal')
plt.legend(loc = 'best', prop={'size':22})

#plot gains
fig3 = plt.figure(figsize = (16,16))
plt.plot(range(len(measurements[0])),Kx, label = '$Gain x$')
plt.plot(range(len(measurements[0])),Ky, label = '$Gain y$')
plt.plot(range(len(measurements[0])),Kdx, label = '$Gain xdot$')
plt.plot(range(len(measurements[0])),Kdy, label = '$Gain ydot$')
plt.legend(loc = 'best', prop={'size':22})
