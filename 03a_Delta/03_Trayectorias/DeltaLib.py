#!/usr/bin/env python
# coding: utf-8

# In[40]:


# get_ipython().run_line_magic('reset', '-sf')
# import numpy as np


# In[41]:
import os
from pathlib import Path
import numpy as np

def genMintCode(pathStr,splinetime,reps,nomArchivo = None):
    p = Path(pathStr) 
    csv = str(p)
    csv_folder = str(p.parent)
    try:
        TH = np.genfromtxt(csv, delimiter=',')
    except OSError as err:
        return "OS error: {0}".format(err)
    numpos = int(np.size(TH)/3)
    TH = np.reshape(TH,[numpos,3])
    if nomArchivo is None: 
        filename = csv_folder + '\\solution.txt'
    else:
        filename = csv_folder + '\\' + nomArchivo
    file1 = open(filename,"w")
    TH0 = TH[:,0]
    TH1 = TH[:,1]
    TH2 = TH[:,2]
    m,n = TH.shape
    #print(m,n)
#     print("hola",end='\n',file = file1)
    print('VECTORA(0,1,2)=%5.2f,%5.2f,%5.2f : GO(0)\n' % (TH0[0],TH1[0],TH2[0]),end = '',file = file1)
    print('Pause(IDLE(0))\n',end = '',file = file1)

    print('Print "Ir al punto inicial completado con exito"\n',end = '',file = file1)

    # se incializa y se declara el primer valor de los vectores movx y movy
    
    print('Dim movzero(%i)\n'% (m*reps+1),end = '',file = file1);
    print('Dim movone(%i)\n'% (m*reps+1),end = '',file = file1);
    print('Dim movtwo(%i)\n'% (m*reps+1),end = '',file = file1);
    print('movzero(1)=%i\n'% (m*reps),end = '',file = file1);
    print('movone(1)=%i\n'% (m*reps),end = '',file = file1);
    print('movtwo(1)=%i\n'% (m*reps),end = '',file = file1);

    # se generan los dem?s valores de movx y movy
    
    k = 0;
    for j in range(0,reps):
        for i in range(2,m+2):
            print('movzero(%i)=%5.2f\n'% (i+(m*j),TH0[k]),end = '',file = file1);   
            print('movone(%i)=%5.2f\n'% (i+(m*j),TH1[k]),end = '',file = file1); 
            print('movtwo(%i)=%5.2f\n'% (i+(m*j),TH2[k]),end = '',file = file1);
            k = k+1;
        k = 0;
        # i=i+1;
        # print('movzero(%i)=%5.2f\n'% (i+(m*j),TH0[k]),end = '',file = file1);   
        # print('movone(%i)=%5.2f\n'% (i+(m*j),TH1[k]),end = '',file = file1); 
        # print('movtwo(%i)=%5.2f\n'% (i+(m*j),TH2[k]),end = '',file = file1);

        
    # se genera la orden de movimiento y el splinetime
    
    print('SPLINETABLE(0, movzero, Null, Null) \n',end = '',file = file1);
    print('SPLINETIME(0) = %5.0f\n'% (splinetime),end = '',file = file1);
    print('SPLINE(0) = _spABSOLUTE Or _spT_ABSOLUTE\n',end = '',file = file1);
    print('SPLINETABLE(1, movone, Null, Null) \n',end = '',file = file1);
    print('SPLINETIME(1) = %5.0f\n'% (splinetime),end = '',file = file1);
    print('SPLINE(1) = _spABSOLUTE Or _spT_ABSOLUTE\n',end = '',file = file1);
    print('SPLINETABLE(2, movtwo, Null, Null) \n',end = '',file = file1);
    print('SPLINETIME(2) = %5.0f\n'% (splinetime),end = '',file = file1);
    print('SPLINE(2) = _spABSOLUTE Or _spT_ABSOLUTE\n',end = '',file = file1);

    print('GO(0,1,2)\n',end = '',file = file1);
    print('Pause(IDLE(0) & IDLE(1) & IDLE(2))\n',end = '',file = file1);
    print('Print "?Movimiento completado!"\n',end = '',file = file1);
    file1.close()
    print(m," puntos procesados")
    return filename
    


# In[42]:


# thm = np.genfromtxt('angulos.csv', delimiter=',')
# numpos = int(np.size(thm)/3)
# thm = np.reshape(thm,[numpos,3])
# numpos,thm
    
# genMintCode(thm,25,1)

