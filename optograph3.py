import matplotlib.pyplot as plt
import numpy as np

v = [3, 3.5, 4, 4.14, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1]
i = [1.1, 5.9, 14.9, 20, 22.5, 25, 29.7, 32.4, 37, 42.3, 49.2, 57, 65.7, 81.1]
p = [.01185, .0154, .0236, .0317, .0436, .353, 1.307, 2.477, 3.73, 5.23, 7.14, 9.1, 11.51, 15.83]

v_label = "Voltage (V)"
i_label = "Amps (mA)"
p_label = "Power (mW)"

ititle = "I-V (Voltage versus Current) Curve"
ptitle = "P-I (Power versus Current) Curve"

# First do I-V

plt.scatter(v, i)
plt.xlabel(v_label)
plt.ylabel(i_label)
plt.title(ititle)

# Now do P-I

#plt.scatter(i, p)
#plt.xlabel(i_label)
#plt.ylabel(p_label)
#plt.title(ptitle)

plt.show()

# Now do dP/dI

#dpdi = np.diff(p) / np.diff(i)
#plt.scatter(i[1:], dpdi)
#plt.xlabel(i_label)
#plt.ylabel("dP/dI")
#plt.title("dP/dI versus I")

#plt.show()

# Now do IdV/dI


dvdi = np.diff(v) / np.diff(i)
dvdi = dvdi * i[1:]

print(dvdi)

# Retain only the 1st, 2nd, 5th, and 7th elements

dvdi = dvdi[[0, 1, 4, 6]]

i = i[1:]

i = [i[0] , i[1], i[4], i[6]]

# Make a trendline

m, b = np.polyfit(i, dvdi, 1)

plt.scatter(i, dvdi)
plt.xlabel(i_label)
plt.ylabel("IdV/dI")
plt.title("IdV/dI versus I" + "\n" + "y = " + str(m) + "x + " + str(b))
plt.plot(i, m*np.array(i) + b)

plt.show()

# Threshold current = 22.5mA
# Threshold voltage = 4.2V
# IdV/dI = .02143x + .4916
# Rs = .0214 * 1000 = 21.4 ohms
# n = .4916 / Vt = .4916 / .0257 = 19.14