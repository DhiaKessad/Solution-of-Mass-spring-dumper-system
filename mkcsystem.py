#this simulate a mass-spring-damper system
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

#parameters
m = 1000 #mass
k =40 #spring stifness
c = 10 #dumper viscosity

A = np.array([[0, 1],[-k/m, -c/m]])
B = np.array([[0], [1/m]])
C = np.array([[1, 0]])
sys = ctrl.ss(A, B, C, 0)

t = np.arange(0,100,0.1)
[t_anl,y_anl, ] = ctrl.forced_response(sys, T=t, X0 = [10,0])

plt.figure(figsize=(7,7))
plt.plot(t_anl,y_anl,'k-')
plt.title('Simulation of a Mass-Spring-Damper System')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.show()