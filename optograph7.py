import matplotlib.pyplot as plt
import numpy as np

darki1ohm = 0
darki10kohm = 0
darki400kohm = 0
darkv1ohm = 0
darkv10kohm = 0
darkv400kohm = 0

lightpower2 = 30 # mW
lightpower1 = 2.7
lightpower0 = 0

rl = [1, 10000, 400000]

p0id = [0, 0, 0]
p0vd = [0, 0, 0]

p1im = [50.4, 45.3, 7.3] # uA at 1, 10k, and 400k ohms
p1vm = [0, .45, 2.79]

p2im = [323, 210, 12.3] 
p2vm = [0, 2.08, 4.72]

vocp0 = 0
iscp0 = 0
pimp0 = 0

vocp1 = 2.79
iscp1 = 50.4
pimp1 = vocp1 * iscp1

vocp2 = 4.72
iscp2 = 323
pimp2 = vocp2 * iscp2 

# fill factors for power 2 (uW)

power1 = p2im[0] * p2vm[0]
power2 = p2im[1] * p2vm[1]
power3 = p2im[2] * p2vm[2]

# Calculate the highest power and get the voltage for that power

maxpower = max(power1, power2, power3)

maxvoltage = 0

if maxpower == power1:
    maxvoltage = p2vm[0]
elif maxpower == power2:
    maxvoltage = p2vm[1]
else:
    maxvoltage = p2vm[2]

print("Max voltage: " + str(maxvoltage))

fillfactor = maxpower / pimp2

print("Fill factor: " + str(fillfactor))

# Conversion efficiency

efficiency = maxpower / (lightpower2 * 1000)

print("Conversion efficiency: " + str(efficiency))  

v_label = "Voltage (V)"
i_label = "Amps (uA)"

# I-V curve for each power

def plot1():
    title = "Current vs. Voltage for three different powers"
    plt.title(title)
    plt.xlabel(v_label)
    plt.ylabel(i_label)
    plt.plot(p0vd, p0id, label="0 mW")
    plt.plot(p1vm, p1im, label="0.027 mW")
    plt.plot(p2vm, p2im, label="0.3 mW")
    plt.legend()

# Measured powers

def plot2():
    title = "Power vs. Voltage for power 2"
    plt.title(title)
    plt.xlabel(v_label)
    plt.ylabel("Power (uW)")
    plt.plot(p2vm, [power1, power2, power3])




plot2()

plt.show()