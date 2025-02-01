import matplotlib.pyplot as plt
import numpy as np

v = [0, .4, .8, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.025, 2.05, 2.1]
i = [0, 0, 0, .01, .03, 2.5, 5.9, 13.9, 27.7, 32.8, 37.4, 48.1] 
nm = [631.56, 631.56, 631.56, 631.56, 631.56, 631.56, 631.96, 632.36, 633.16, 633.55, 633.95, 633.95]
fwhm = [15.9, 15.9, 15.9, 15.9, 15.9, 15.9, 15.9, 17, 18.69, 20.28, 23.06, 26.25]

v_label = "Voltage (V)"
i_label = "Amps (mA)"
nm_label = "Wavelength (nm)"

ititle = "I-V (Voltage versus Current) Curve"
nmtitle = "nm-I (Wavelength versus Voltage) Curve"

itrendline = np.polyfit(v[7:], i[7:], 1)
itrenddata = np.poly1d(itrendline)

# First do I-V

plt.scatter(v, i)
plt.xlabel(v_label)
plt.ylabel(i_label)
plt.title(ititle + "\n" + "y = " + str(itrendline[0]) + "x + " + str(itrendline[1]))
plt.plot(v[7:], itrenddata(v[7:]), "r-")

# Now do nm-V

#plt.scatter(i, nm)
#plt.xlabel(i_label)
#plt.ylabel(nm_label)
#plt.title(nmtitle)

# Now do fwhm-V

#plt.scatter(v, fwhm)
#plt.xlabel(v_label)
#plt.ylabel("FWHM (nm)")
#plt.title("FWHM versus Voltage")

plt.show()

# Vth,o = (6.626×10^−34×3×10^8)÷(1.602×10^−19×632.76×10^−9) = 1.96V
# Vth = 307.95÷168.7 = 1.82V 
# Ego = (6.626×10^−34×3×10^8)÷(632.75×10^−9) = 3.14*10^-19
# Egv = (1.602×10^−19×1.8) = 2.88*10^-19


# red led 639nm, 2.1v
# blue 465nm, 2.85v
# h = (1.602×10^−19)×(.75÷(5.855924074915442475642384×10⁵))÷(3×10^8) = 6.839×10⁻³⁴