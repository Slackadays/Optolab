import matplotlib.pyplot as plt
import numpy as np

v = [0, .4, .8, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.025, 2.05, 2.1]
i = [0, 0, .0001, .0001, .0001, .22, 3.55, 15.15, 37.35, 54.6, 65, 76.8]
p = [0, 0, 0, 0, 0, .012, .158, .692, 1.655, 2.34, 2.72, 3.12]

v_label = "Voltage (V)"
i_label = "Amps (mA)"
p_label = "Power (mW)"

ititle = "I-V (Voltage versus Current) Curve"
ptitle = "P-I (Power versus Current) Curve"
ilntitle = "ln(I) versus V"

itrendline = np.polyfit(v[7:], i[7:], 1)
itrenddata = np.poly1d(itrendline)

ptrendline = np.polyfit(i, p, 1)
ptrenddata = np.poly1d(ptrendline)

iln = np.log(i[6:])
ilntrendline = np.polyfit(v[6:], iln, 1)
ilntrenddata = np.poly1d(ilntrendline)

# First do I-V

#plt.scatter(v, i)
#plt.xlabel(v_label)
#plt.ylabel(i_label)
#plt.title(ititle + "\n" + "y = " + str(itrendline[0]) + "x + " + str(itrendline[1]))
#plt.plot(v[7:], itrenddata(v[7:]), "r-")

# Now do P-I

#plt.scatter(i, p)
#plt.xlabel(i_label)
#plt.ylabel(p_label)
#plt.plot(i[7:], ptrenddata(i[7:]), "r-")
#plt.title(ptitle + "\n" + "y = " + str(ptrendline[0]) + "x + " + str(ptrendline[1]))

# Also include dP/dI 

dpdi = np.diff(p[5:]) / np.diff(i[5:])
print(dpdi)
#plt.scatter(i[6:], dpdi)
#plt.xlabel(i_label)
#plt.ylabel("dP/d" + i_label)
#plt.ylim(0, .1)
#plt.title("dP/d" + i_label)

# Now do ln(i)

#plt.scatter(v[6:], iln)
#plt.xlabel(v_label)
#plt.ylabel("ln(" + i_label + ")")
#plt.plot(v[6:], ilntrenddata(v[6:]), "r-")
#plt.title(ilntitle + "\n" + "y = " + str(ilntrendline[0]) + "x + " + str(ilntrendline[1]))

#plt.show()