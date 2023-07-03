import serial
import time
import re

import matplotlib.pyplot as plt 
from time import sleep
from drawnow import *

arduino = serial.Serial('COM3')
with arduino:
	arduino.setDTR(False)
	sleep(1)
	arduino.flushInput()
	arduino.setDTR(True)

arduino = serial.Serial('COM3', baudrate=115200)
plt.ion ()

count = 0 
AccYarray  = []
AccZarray  = []
tempoarray = []


def fig ():
 # heights of bars
    try:
        left = [1,2,3,4,5,6,7,8,9,10]
        
        height     = [a,b,c,d,e,f,g,h,i,j]
        # labels for bars
        tick_label = [415,445,480,515,555,590,630,680,910,980]
        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.8, color = ['r', 'g', 'r', 'c', 'm', 'y', 'k', 'g', 'b'])

        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('spectrum!')
   
    except :
        print("xx")

with arduino:
   
    while True:
         try:
            dadosstring = arduino.readline ()
            xxx = str(dadosstring)
            xxx = xxx.strip()
           # print(xxx);
            
            x=re.split(" : ",xxx)
            a1=x[1]
            a2=x[2]
            a3=x[3]
            a4=x[4]
            a5=x[5]
            a6=x[6]
            a7=x[7]
            a8=x[8]
            a9=x[9]
            a10=x[10]

            b1 = re.split(",",a1)
            b2 = re.split(",",a2)
            b3 = re.split(",",a3)
            b4 = re.split(",",a4)
            b5 = re.split(",",a5)
            b6 = re.split(",",a6)
            b7 = re.split(",",a7)
            b8 = re.split(",",a8)
            b9 = re.split(",",a9)
            b10 = re.split(",",a10)

            a=int(b1[0])
            b=int(b2[0])
            c=int(b3[0])
            d=int(b4[0])
            e=int(b5[0])
            f=int(b6[0])
            g=int(b7[0])
            h=int(b8[0])
            i=int(b9[0])
            j=(b10[0])
            j=j[:-5]
            j=int(j)
            
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            print(g)
            print(h)
            print(i)
            print(j)
            print("================")

            drawnow(fig)
    
            
         except :
            print("ee")

    drawnow(fig)
          
