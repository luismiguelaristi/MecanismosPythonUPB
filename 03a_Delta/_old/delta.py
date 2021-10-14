# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:00:10 2020

@author: Luis
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#para realizar animaciones
from matplotlib.animation import FuncAnimation
#para gráficas 3D
from mpl_toolkits.mplot3d import Axes3D

#Importar comandos de IPython para limpiar variables y terminal
from IPython import get_ipython

# para exportar e importar variables a archivos
import pickle

#Equivalente a clear all
get_ipython().magic('reset -sf')
#Equivalente a clc
get_ipython().magic('clear')
#Cerrar todas las ventanas de gráficos (close all)
plt.close("all")


def fn_delta(x0):
    global a,b,h,r,phi
    global px,py,pz
    Qx = x0[0]
    Qy = x0[1]
    Qz = x0[2]
    Dx = r*np.cos(phi);
    Dy = r*np.sin(phi);
    Dz = 0;
    Cx = px + h*np.cos(phi);
    Cy = py + h*np.sin(phi);
    Cz = pz;
    return ((Qx-Dx)**2 + (Qy-Dy)**2 + (Qz-Dz)**2 - a**2,
            (Qx-Cx)**2 + (Qy-Cy)**2 + (Qz-Cz)**2 - b**2,
            Qx*np.cos(phi + (np.pi/2)) + Qy*np.sin(phi + (np.pi/2)))


global a,b,h,r,phi
global px,py,pz

#base fija a eje motores [mm]
r=144.34 
#eje motores a eje paralelogramo superior (esf?ricos)
a=200.87
#longitud paralelogramo
b=526.695
#distancia eje paralelogramo inferior (esf?ricos) a centro de la base m?vil
h= 52.528

phi=(30)*np.pi/180

px = 0;
py = 0;
pz = -528.6718

Qx_ini_1 = 284.5325
Qy_ini_1 = 164.2749
Qz_ini_1 = -80.0967
Qx_ini_2 = -Qx_ini_1
Qy_ini_2 = Qy_ini_1
Qz_ini_2 = Qz_ini_1
Qx_ini_3 = 0
Qy_ini_3 = -np.sqrt(Qx_ini_1**2 + Qy_ini_1**2)
Qz_ini_3 = Qz_ini_1

x0_1 = [Qx_ini_1,Qy_ini_1,Qz_ini_1]
x0_2 = [Qx_ini_2,Qy_ini_2,Qz_ini_2]
x0_3 = [Qx_ini_3,Qy_ini_3,Qz_ini_3]

PHI = [phi,phi+np.deg2rad(120),phi+np.deg2rad(240)]
X0 = np.array([x0_1,x0_2,x0_3])

numpos = 50
numtray = 3
numbrazos = 3

# Trayectorias
# Linea recta
PX1 = np.linspace(0,100,numpos)
PY1 = np.linspace(0,0,numpos)
PZ1 = np.linspace(pz,pz-100,numpos)
# Circunferencia
r_c = 100
theta = np.linspace(0,2*np.pi,numpos)
PX2 = r_c*np.cos(theta)
PY2 = r_c*np.sin(theta)
PZ2 = np.ones(numpos)*pz-100
# Linea recta de regreso
PX3 = np.flip(PX1)
PY3 = np.flip(PY1)
PZ3 = np.flip(PZ1)

# Para unir arrays se usa el comando np.append
# Este solo recibe dos argumentos, si se tienen mas de dos arrays a unir
# hacer un array en el segundo argumento con los arrays que se requiera
PX = np.append(PX1,[PX2,PX3])
PY = np.append(PY1,[PY2,PY3])
PZ = np.append(PZ1,[PZ2,PZ3])

#numpos = np.size(PX)

#Definicion de puntos
Dx_1 = r*np.cos(phi)
Dy_1 = r*np.sin(phi)
Dz_1 = 0
CX_1 = PX + h*np.cos(phi)
CY_1 = PY + h*np.sin(phi)
CZ_1 = PZ
# definir puntos C y D para cada brazo
Dx_2 = r*np.cos(phi + np.deg2rad(120));
Dy_2 = r*np.sin(phi + np.deg2rad(120));
Dz_2 = 0;
CX_2 = PX + h*np.cos(phi + np.deg2rad(120));
CY_2 = PY + h*np.sin(phi + np.deg2rad(120));
CZ_2 = PZ;

Dx_3 = r*np.cos(phi + np.deg2rad(240));
Dy_3 = r*np.sin(phi + np.deg2rad(240));
Dz_3 = 0;
CX_3 = PX + h*np.cos(phi + np.deg2rad(240));
CY_3 = PY + h*np.sin(phi + np.deg2rad(240));
CZ_3 = PZ;

#EXITFLAG = np.zeros([numpos,3])
QX = np.zeros([numpos*numtray,3])
QY = np.zeros([numpos*numtray,3])
QZ = np.zeros([numpos*numtray,3])

for j in range(0,numbrazos):
    x0 = X0[j,:]
    phi = PHI[j]
    for i in range(0,numpos*numtray):
        px = PX[i];
        py = PY[i];
        pz = PZ[i];
        Y,info,msg,EXITFLAG = fsolve(fn_delta,x0,full_output = True)
        x0 = Y
        QX[i,j] = Y[0];
        QY[i,j] = Y[1];
        QZ[i,j] = Y[2];
    
fig1 = plt.figure()
ax1 = fig1.add_subplot(111,projection = '3d')

ax1.plot([Dx_1,0],[Dy_1,0],[Dz_1,0],'-b')
h_a1 = ax1.plot([CX_1[0],QX[0,0]],[CY_1[0],QY[0,0]],[CZ_1[0],QZ[0,0]],'-r')
h_b1 = ax1.plot([CX_1[0],PX[0]],[CY_1[0],PY[0]],[CZ_1[0],PZ[0]],'-g')
h_h1 = ax1.plot([CX_1[0],0],[CY_1[0],0],[CZ_1[0],0],'-k')
ax1.plot([Dx_2,0],[Dy_2,0],[Dz_2,0],'-b')
h_a2 = ax1.plot([CX_2[0],QX[0,1]],[CY_2[0],QY[0,1]],[CZ_2[0],QZ[0,1]],'-r')
h_b2 = ax1.plot([CX_2[0],PX[0]],[CY_2[0],PY[0]],[CZ_2[0],PZ[0]],'-g')
h_h2 = ax1.plot([CX_2[0],0],[CY_2[0],0],[CZ_2[0],0],'-k')
ax1.plot([Dx_3,0],[Dy_3,0],[Dz_3,0],'-b')
h_a3 = ax1.plot([CX_3[0],QX[0,2]],[CY_3[0],QY[0,2]],[CZ_3[0],QZ[0,2]],'-r')
h_b3 = ax1.plot([CX_3[0],PX[0]],[CY_3[0],PY[0]],[CZ_3[0],PZ[0]],'-g')
h_h3 = ax1.plot([CX_3[0],0],[CY_3[0],0],[CZ_3[0],0],'-k')
h_P = ax1.plot([PX[0]],[PY[0]],[PZ[0]],'-m')

ax1.set_xlim3d(-400,400)
ax1.set_ylim3d(-400,400)
ax1.set_zlim3d(0,-800)
ax1.invert_zaxis()
#ax1.axis("scaled")

def animar(i):
    brazo_a_X = np.array([Dx_1,QX[i,0]])
    brazo_a_Y = np.array([Dy_1,QY[i,0]])
    brazo_a_Z = np.array([Dz_1,QZ[i,0]])
    brazo_b_X = np.array([CX_1[i],QX[i,0]])
    brazo_b_Y = np.array([CY_1[i],QY[i,0]])
    brazo_b_Z = np.array([CZ_1[i],QZ[i,0]])
    brazo_h_X = np.array([CX_1[i],PX[i]])
    brazo_h_Y = np.array([CY_1[i],PY[i]])
    brazo_h_Z = np.array([CZ_1[i],PZ[i]])
    brazo2_a_X = np.array([Dx_2,QX[i,1]])
    brazo2_a_Y = np.array([Dy_2,QY[i,1]])
    brazo2_a_Z = np.array([Dz_2,QZ[i,1]])
    brazo2_b_X = np.array([CX_2[i],QX[i,1]])
    brazo2_b_Y = np.array([CY_2[i],QY[i,1]])
    brazo2_b_Z = np.array([CZ_2[i],QZ[i,1]])
    brazo2_h_X = np.array([CX_2[i],PX[i]])
    brazo2_h_Y = np.array([CY_2[i],PY[i]])
    brazo2_h_Z = np.array([CZ_2[i],PZ[i]])
    brazo3_a_X = np.array([Dx_3,QX[i,2]])
    brazo3_a_Y = np.array([Dy_3,QY[i,2]])
    brazo3_a_Z = np.array([Dz_3,QZ[i,2]])
    brazo3_b_X = np.array([CX_3[i],QX[i,2]])
    brazo3_b_Y = np.array([CY_3[i],QY[i,2]])
    brazo3_b_Z = np.array([CZ_3[i],QZ[i,2]])
    brazo3_h_X = np.array([CX_3[i],PX[i]])
    brazo3_h_Y = np.array([CY_3[i],PY[i]])
    brazo3_h_Z = np.array([CZ_3[i],PZ[i]])
    h_a1[0].set_data_3d([brazo_a_X,brazo_a_Y,brazo_a_Z])
    h_b1[0].set_data_3d([brazo_b_X,brazo_b_Y,brazo_b_Z])
    h_h1[0].set_data_3d([brazo_h_X,brazo_h_Y,brazo_h_Z])
    h_a2[0].set_data_3d([brazo2_a_X,brazo2_a_Y,brazo2_a_Z])
    h_b2[0].set_data_3d([brazo2_b_X,brazo2_b_Y,brazo2_b_Z])
    h_h2[0].set_data_3d([brazo2_h_X,brazo2_h_Y,brazo2_h_Z])
    h_a3[0].set_data_3d([brazo3_a_X,brazo3_a_Y,brazo3_a_Z])
    h_b3[0].set_data_3d([brazo3_b_X,brazo3_b_Y,brazo3_b_Z])
    h_h3[0].set_data_3d([brazo3_h_X,brazo3_h_Y,brazo3_h_Z])
    h_P[0].set_data_3d([PX[:i],PY[:i],PZ[:i]])

animacion = FuncAnimation(fig1, animar, interval=15)
plt.show()
