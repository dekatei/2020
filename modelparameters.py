import numpy as np
import pylab as py
import random
m_e = 1
#aee = 1.4991
aep = 1.1560
app = 0.8669
m_p = 1836.2  # massofproton
w_0 = 0.058 #frequency
N = 3
E_0 = 0.6
L = 100000 # количество одинаковых промежутков времени
T = 2 * np.pi * N /w_0  # Период колебаний
#print('T', T)
u = 3 * 325 #время на которое предоставляем систему самой себе

t = np.linspace(0, u, L)

# t = linspace(0,2*0.03, L)
n = 5 
nn =5#количесвто экспериментов
eps = 0.1
dist = 2 * ((2 ** (2 / 3) * aep ** 2 - app ** 2) / (4 - 2 ** (2 / 3))) ** (1 / 2) # distance between protons
sphere = np.array(np.random.normal(size =(n,3)))
ball = sphere/np.linalg.norm(sphere,axis = 1).reshape(n,1)
#print(sphere)
#print(np.linalg.norm(sphere, axis = 1))
#print (ball)
#print(np.linalg.norm(ball, axis =1))
p = (2*eps)**0.5* ball
#def momentum(n,eps):# задаем количество экспериментов n, для них вектор импульса для электрона, eps - начальная энергия
#        p = []
#        for _ in range(n):
#            # p.append(0)
#            pi = np.pi
#            theta = pi * random.uniform(0, 1)  # randit обе границы включаются в диапазон, только целые числа ,randrange не включая правую границу
#            phi = 2 * pi * random.uniform(0, 1)
#            p_x = (2 * eps) ** (0.5) * np.cos(phi) * np.sin(theta)
#            p_y = (2 * eps) ** (0.5) * np.sin(phi) * np.sin(theta)
#            p_z = (2 * eps) ** (0.5) * np.cos(theta)
#            p.append([p_x, p_y, p_z])
#
#        return p # набор векторов импульса
#p = momentum(nn,eps)

#S = []#
#n = 10000
##попытка сделать равномерное распределение на сфере
#def xyz(n):
#    xyz = []
#    for _ in range(n):
#        xyz.append([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])
#    return xyz
#A = xyz(n)
#def length2(i, xyz):
#    a = xyz[i][0] ** 2 + xyz[i][1] ** 2 + xyz[i][2] ** 2
#    return a
#for i in range(n) :
#    if not length2(i, A) > 1 :
#        S.append(A[i])
#p = np.array(S)
#for i in range (nn):
#    b = length2(i,p)
#    p[i][0]= (2 * eps) ** (0.5) * p[i][0]/b**0.5
#    p[i][1]= (2 * eps) ** (0.5) * p[i][1]/b**0.5
#    p[i][2]= (2 * eps) ** (0.5) * p[i][2]/b**0.5