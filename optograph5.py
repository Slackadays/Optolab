import matplotlib.pyplot as plt
import numpy as np

backgroundi = 0.08 # mA

current432 = 2.01
transmittance432 = 26.7
current640 = 2.18
transmittance640 = .376
current532 = 2.06
transmittance532 = .22
current775 = .13
transmittance775 = .028

power1 = .038 # mW
power2 = .527
power3 = 1.01
power4 = 3.84
power45 = 7.75
power5 = 10.44
power6 = 12.86
voltage1 = 4.89
voltage2 = 4.6
voltage3 = 4.41
voltage4 = 3.62
voltage45 = 3.31
voltage5 = 3.11
voltage6 = 2.94
current1 = .11 # mA
current2 = .42
current3 = .61
current4 = 1.37
current45 = 1.69
current5 = 1.9
current6 = 2.08

timeconstant2 = .0082 # s
timeconstant3 = .0079
timeconstant4 = .0079
timeconstant45 = .006
timeconstant5 = .0058
timeconstant6 = .0061 

bandwidth2 = 1 / (2 * np.pi * timeconstant2)
bandwidth3 = 1 / (2 * np.pi * timeconstant3)
bandwidth4 = 1 / (2 * np.pi * timeconstant4)
bandwidth45 = 1 / (2 * np.pi * timeconstant45)
bandwidth5 = 1 / (2 * np.pi * timeconstant5)
bandwidth6 = 1 / (2 * np.pi * timeconstant6)

power = [power1, power2, power3, power4, power45, power5, power6]
voltage = [voltage1, voltage2, voltage3, voltage4, voltage45, voltage5, voltage6]
current = [current1, current2, current3, current4, current45, current5, current6]

# Convert to ms
timeconstant = [timeconstant2 * 1000, timeconstant3 * 1000, timeconstant4 * 1000, timeconstant45 * 1000, timeconstant5 * 1000, timeconstant6 * 1000]

bandwidth = [bandwidth2, bandwidth3, bandwidth4, bandwidth45, bandwidth5, bandwidth6]


v_label = "Voltage (V)"
i_label = "Amps (mA)"
p_label = "Power (mW)"

title1 = "Voltage versus Power"
title2 = "Current versus Power"

# Voltage versus Power

def plot1():
    plt.plot(power, voltage, 'ro')
    plt.xlabel(p_label)
    plt.ylabel(v_label)
    plt.title(title1)

# Current versus Power

def plot2():
    plt.plot(power, current, 'ro')
    plt.xlabel(p_label)
    plt.ylabel(i_label)
    plt.title(title2)

# Bandwidth versus time constant

def plot3():
    plt.plot(timeconstant, bandwidth, 'ro')
    plt.xlabel("Time Constant (ms)")
    plt.ylabel("Bandwidth (Hz)")
    plt.title("Bandwidth versus Time Constant")

# Bandwidth versus Power

def plot4():
    # Discard the first power value
    global power
    power = power[1:]
    # set min y to 0
    plt.ylim(0, max(bandwidth) + 1)
    plt.plot(power, bandwidth, 'ro')
    plt.xlabel(p_label)
    plt.ylabel("Bandwidth (Hz)")
    plt.title("Bandwidth versus Power")

plot4()

plt.show()