import matplotlib.pyplot as plt
import numpy as np

voltages = [-6, -4, -2, -1, 0]

ledpower0 = 0

current0 = [-12, -7.8, -3.7, -1.5, 0] # uA at -6, -4, -2, -1, 0V
voltage0 = [-.33, .32, -.3, -.27, 0]

ledpower1 = 0.12 # mW

current1 = [-46.1, -54.8, -51.6, -51.3, -52.6] # uA at -6, -4, -2, -1, 0V
voltage1 = [5.85, .537, 1.9, .908, .282]

ledpower2 = 1.5

current2 = [-512, -509, -508, -507, -140] 
voltage2 = [4.87, 2.93, .917, .038, .461]

ledpower3 = 2.7 

current3 = [-937, -937, -936, -680, -160]
voltage3 = [4.05, 1.978, .038, .441, .495]

v_label = "Voltage (V)"
i_label = "Amps (uA)"

# I-V

def plot1():
    title = "Voltage vs. Current for four different LED powers"
    plt.title(title)
    plt.xlabel(v_label)
    plt.ylabel(i_label)
    plt.plot(voltages, current0, label="0 mW")
    plt.plot(voltages, current1, label="0.12 mW")
    plt.plot(voltages, current2, label="1.5 mW")
    plt.plot(voltages, current3, label="2.7 mW")
    plt.legend()

# I-P with trendline for -2V

def plot2():
    title = "Current vs. Power for -2V"
    plt.title(title)
    plt.xlabel("Power (mW)")
    plt.ylabel(i_label)
    trendline = np.polyfit([ledpower0, ledpower1, ledpower2, ledpower3], [current0[2], current1[2], current2[2], current3[2]], 1)
    plt.plot([ledpower0, ledpower1, ledpower2, ledpower3], [current0[2], current1[2], current2[2], current3[2]], label="-2V")
    plt.plot([ledpower0, ledpower1, ledpower2, ledpower3], np.polyval(trendline, [ledpower0, ledpower1, ledpower2, ledpower3]), label="Trendline")
    plt.text(1.5, -510, "y = " + str(trendline[0]) + "x + " + str(trendline[1]))
    plt.legend()

r1 = 5000
t1 = 1.8 # us

r2 = 20000
t2 = 8.8

r3 = 10000
t3 = 4

# tau vs r

def plot3():
    title = "Tau vs. Resistance"
    plt.title(title)
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel("Tau (us)")
    plt.plot([r1, r3, r2], [t1, t3, t2])


plot3()

plt.show()