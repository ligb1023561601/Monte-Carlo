# _*_ coding: utf-8 _*_
# @Time     : 2017/10/25 16:56
# @Author    : Ligb
# @File     : math_plot.py


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import *
import math
import random


def calc_position(theta_a, theta_b, theta_c):
    t_0_1 = matrix([[math.cos(theta_a), math.sin(theta_a) * -1, 0, 0],
                  [math.sin(theta_a), math.cos(theta_a), 0, 0],
                  [0, 0, 1, 250],
                  [0, 0, 0, 1]])
    t_1_2 = matrix([[math.cos(theta_b), math.sin(theta_b) * -1, 0, 0],
                  [0, 0, -1, 0],
                  [math.sin(theta_b), math.cos(theta_b), 0, 0],
                  [0, 0, 0, 1]])
    t_2_3 = matrix([[math.cos(theta_c), math.sin(theta_c) * -1, 0, 0],
                  [0, 0, 1, 700],
                  [math.sin(theta_c) * -1, math.cos(theta_c) * -1 , 0, 0],
                  [0, 0, 0, 1]])
    t_0_3 = t_0_1 * t_1_2 * t_2_3
    positions = t_0_3[0:, -1][0:3]
    return list(positions)


def plot_workspace(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, y, z, color='b', rstride=1, cstride=1,linewidth=0, antialiased=True)
    ax.set_zlim(0, 1500)
    plt.show()

x = []
y = []
z = []
for i in range(1000):
    theta_1 = random.uniform(-1, 1)
    theta_2 = random.uniform(-1, 1)
    theta_3 = random.uniform(-1, 1)
    theta_1 = math.pi * theta_1
    theta_2 = 0.61111111 * math.pi * theta_2
    theta_3 = 0.94444444 * math.pi * theta_3
    ordinates = calc_position(theta_1, theta_2, theta_3)
    x.append(float(ordinates[0][0]))
    y.append(float(ordinates[1][0]))
    z.append(float(ordinates[2][0]))

x = array(x)
y = array(y)
z = array(z)
k = arange(0, 1000, 1)
x, y = meshgrid(x, y)
z, k = meshgrid(z, k)
plot_workspace(x, y, z)
print(x.max(), y.max(), z.max(), k.max())
print(x.min(), y.min(), z.min(), k.min())




