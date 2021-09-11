#!/usr/bin/env python
# coding: utf-8

# # Solución del sistema de ecuaciones para mecanismo manivela balancín por método analítico
# 
# Norton, R. L., & Hernández, A. E. G. (2000). Diseño de maquinaria. McGraw-Hill Interamericana. https://books.google.com.co/books?id=9LhYAAAACAAJ

# ![SolucionManivelaBalancinNorton.png](attachment:SolucionManivelaBalancinNorton.png)

# ## Ecuación de cierre vectorial
# 
# $\overrightarrow{r_{2}}+\overrightarrow{r_{3}}-\overrightarrow{r_{4}}-\overrightarrow{r_{1}}=0$
# 
# cuyas ecuaciones escalares correspondientes son
# 
# $r2\cdot cos(\theta_{2})+r3\cdot cos(\theta_{3})-r4\cdot cos(\theta_{4})-r1\cdot cos(\theta_{1})=0$,
# 
# $r2\cdot sin(\theta_{2})+r3\cdot sin(\theta_{3})-r4\cdot sin(\theta_{4})-r1\cdot sin(\theta_{1})=0$

# ## Solución analítica
# 
# Ver Norton, 2000

# ### 1. Importar módulos necesarios
# 
# Numpy para herramientas matemáticas
# 
# matplotlib.pyplot para gráficos

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ### 2. definir parámetros

# In[2]:


r2 = 60.0
r3 = 150.0
r4 = 100.0
r1 = 160.0 
th1 = 0.0


# ### 3. definir valor para variable de entrada

# In[3]:


th2 = np.deg2rad(0)


# ### 4. implementar ecuaciones

# In[4]:


k1 = r1/r2
k2 = r1/r4
k3 = ((r2**2)-(r3**2)+(r4**2)+(r1**2))/(2*r2*r4)

A = k3 - k2*np.cos(th2) - k1 + np.cos(th2)
B = -2*np.sin(th2)
C = k3 - k2*np.cos(th2) + k1 - np.cos(th2)

print(B,A,C)


# ### 5. evaluar

# In[5]:


Bsquared = (B**2)
ACfour = (4*A*C)
print(Bsquared,ACfour)


# In[6]:


root = np.sqrt(Bsquared - ACfour)
print(root)
th4a = 2*np.arctan((-B+root)/(2*A))
th4b = 2*np.arctan((-B-root)/(2*A))
print(np.rad2deg(th4a),np.rad2deg(th4b))


# Nos quedamos con la solución $\theta_{4b}$
# 
# Ahora calculamos $\theta_{3}$

# In[7]:


th3a = np.arccos((r1+r4*np.cos(th4a)-r2*np.cos(th2))/r3)
th3b = -np.arccos((r1+r4*np.cos(th4a)-r2*np.cos(th2))/r3)
print(np.rad2deg(th3a),np.rad2deg(th3b))


# ### 6. resolver para un rango de posiciones de la barra de entrada
# 
# Ahora hagámoslo iterativo. Para hacer esto conviene hacer una función:
# - La función recibe el ángulo $\theta_2$
# - La función entrega ambos valores de $\theta_3$ y $\theta_4$

# In[8]:


def manivelaBalancinAnalitico(th2):
    k1 = r1/r2
    k2 = r1/r4
    k3 = ((r2**2)-(r3**2)+(r4**2)+(r1**2))/(2*r2*r4)

    A = k3 - k2*np.cos(th2) - k1 + np.cos(th2)
    B = -2*np.sin(th2)
    C = k3 - k2*np.cos(th2) + k1 - np.cos(th2)
    
    Bsquared = (B**2)
    ACfour = (4*A*C)
    root = np.sqrt(Bsquared - ACfour)
    th4a = 2*np.arctan((-B+root)/(2*A))
    th4b = 2*np.arctan((-B-root)/(2*A))
    th3a = np.arccos((r1+r4*np.cos(th4a)-r2*np.cos(th2))/r3)
    th3b = np.arccos((r1+r4*np.cos(th4b)-r2*np.cos(th2))/r3)
    return [th4a,th4b,th3a,th3b]
    


# Ahora probemos la función. Deberíamos obtener lo mismo que con la evaluación de arriba

# In[9]:


varSecundarias = manivelaBalancinAnalitico(th2)
print(np.rad2deg(varSecundarias))


# Perfecto, ahora que la función trabaja bien, llamemos a esta función en un ciclo para resolver para muchas posiciones de la manivela.

# In[10]:


#Numero de iteraciones
numpos = 50

#theta 2 vector
th2_v = np.linspace(0,2*np.pi,numpos)
th4_v = np.zeros(numpos)
th3_v = np.zeros(numpos)

for i in range(0,numpos):
    varSecundarias = manivelaBalancinAnalitico(th2_v[i])
    th4_v[i] = varSecundarias[1]
    th3_v[i] = varSecundarias[3]
    
print(np.rad2deg(th3_v),np.rad2deg(th4_v))


# Ahora grafiquemos las variables secundarias Vs la principal.
# Para esto necesitamos importar el módulo Matplotlib:

# In[11]:


import matplotlib.pyplot as plt


# Ahora podemos graficar usando los comandos asociados a "plt", ejemplo: "plt.plot"

# In[12]:


plt.figure()
plt.plot(np.rad2deg(th2_v),np.rad2deg(th3_v))
plt.legend(["Theta3"])
plt.xlabel("Theta2")
plt.ylabel("Theta3")
plt.grid()
plt.figure()
plt.plot(np.rad2deg(th2_v),np.rad2deg(th4_v))
plt.legend(["Theta4"])
plt.xlabel("Theta2")
plt.ylabel("Theta4")
plt.grid()

