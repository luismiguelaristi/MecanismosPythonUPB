# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import cv2 
import sys 
import numpy as np

import tkinter as tk
from tkinter import filedialog

import os
import shutil

root = tk.Tk()
root.wm_attributes('-topmost', 1)
root.withdraw()

file_path = filedialog.askopenfilename()


if file_path != "":
    print(file_path)
else:
    print("Archivo no válido")


infile = file_path
outfile = r"result.mp4"
fps = 30
size = (1920,1080)

cap = cv2.VideoCapture(infile)
fourcc = cv2.VideoWriter_fourcc(*'H264')
vw = cv2.VideoWriter(outfile, fourcc, fps, size)
tmp = 0
while cap.isOpened():
    ret,frame = cap.read()
    
    try:
        tmp = np.maximum(tmp, frame)
    except:
        break
    vw.write(tmp)
    
cap.release()
vw.release()