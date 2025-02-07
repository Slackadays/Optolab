import matplotlib.pyplot as plt
import numpy as np

v25 = [3.77, 4, 4.16, 4.28, 4.39, 4.35, 4.41, 4.46, 4.77, 5]
i25 = [4, 8, 12, 16, 20, 22, 24, 26, 40, 60]
nm25 = [410, 407.5, 405, 405, 405, 405, 405, 405, 405, 406]
fwhm25 = [15, 14, 18, 16, 9, 7, 6, 4, 4, 4]

v30 = [3.73, 3.95, 4.1, 4.21, 4.31, 4.35, 4.37, 4.4, 4.66, 4.96]
i30 = [4, 8, 12, 16, 20, 22, 24, 26, 40, 60]
nm30 = [410, 408, 406, 405, 405, 405, 405, 405, 406, 407]
fwhm30 = [15, 15, 16, 14, 10, 8.5, 7, 5, 4, 4]

v35 = [3.62, 3.86, 4.03, 4.15, 4.25, 4.29, 4.33, 4.36, 4.58, 4.9]
i35 = [4, 8, 12, 16, 20, 22, 24, 26, 40, 60]
nm35 = [411, 409, 407, 406, 405, 405, 405, 405, 406, 407]
fwhm35 = [17, 19, 20, 16, 12, 10, 9, 7, 4, 4]

v_label = "Voltage (V)"
i_label = "Amps (mA)"
logi_label = "ln(I)"
nm_label = "Wavelength (nm)"
fwhm_label = "FWHM (nm)"

title11 = "Wavelength versus Current at 25 degrees C"
title12 = "Wavelength versus Current at 30 degrees C"
title13 = "Wavelength versus Current at 35 degrees C"

title21 = "ln(I) versus Voltage at 25 degrees C"
title22 = "ln(I) versus Voltage at 30 degrees C"
title23 = "ln(I) versus Voltage at 35 degrees C"

title31 = "FWHM versus Current at 25 degrees C"
title32 = "FWHM versus Current at 30 degrees C"
title33 = "FWHM versus Current at 35 degrees C"

plt.subplots_adjust(hspace=0.5)

# nm-I

def plot1():
    plt.subplot(3, 1, 1)
    plt.scatter(i25, nm25)
    plt.xlabel(i_label)
    plt.ylabel(nm_label)
    plt.title(title11)

    plt.subplot(3, 1, 2)
    plt.scatter(i30, nm30)
    plt.xlabel(i_label)
    plt.ylabel(nm_label)
    plt.title(title12)

    plt.subplot(3, 1, 3)
    plt.scatter(i35, nm35)
    plt.xlabel(i_label)
    plt.ylabel(nm_label)
    plt.title(title13)
    

# ln(I)-V

def plot2():
    plt.subplot(3, 1, 1)
    plt.scatter(v25, np.log(i25))
    plt.xlabel(v_label)
    plt.ylabel(logi_label)
    plt.title(title21)

    # Add a trendline
    m, b = np.polyfit(v25, np.log(i25), 1)
    plt.plot(v25, m * np.array(v25) + b)
    plt.text(4.5, 3, "y = " + str(m) + "x + " + str(b))

    plt.subplot(3, 1, 2)
    plt.scatter(v30, np.log(i30))
    plt.xlabel(v_label)
    plt.ylabel(logi_label)
    plt.title(title22)

    # Add a trendline
    m, b = np.polyfit(v30, np.log(i30), 1)
    plt.plot(v30, m * np.array(v30) + b)
    plt.text(4.5, 3, "y = " + str(m) + "x + " + str(b))

    plt.subplot(3, 1, 3)
    plt.scatter(v35, np.log(i35))
    plt.xlabel(v_label)
    plt.ylabel(logi_label)
    plt.title(title23)

    # Add a trendline
    m, b = np.polyfit(v35, np.log(i35), 1)
    plt.plot(v35, m * np.array(v35) + b)
    plt.text(4.5, 3, "y = " + str(m) + "x + " + str(b))

# fwhm-I

def plot3():
    plt.subplot(3, 1, 1)
    plt.scatter(i25, fwhm25)
    plt.xlabel(i_label)
    plt.ylabel(fwhm_label)
    plt.title(title31)

    plt.subplot(3, 1, 2)
    plt.scatter(i30, fwhm30)
    plt.xlabel(i_label)
    plt.ylabel(fwhm_label)
    plt.title(title32)

    plt.subplot(3, 1, 3)
    plt.scatter(i35, fwhm35)
    plt.xlabel(i_label)
    plt.ylabel(fwhm_label)
    plt.title(title33)

# ln(I0)-1/T

def plot4():
    intercept25 = -6.56
    intercept30 = -6.61
    intercept35 = -6.19
    plt.scatter([1/298, 1/303, 1/308], [intercept25, intercept30, intercept35])
    plt.xlabel("1/T")
    plt.ylabel("ln(I0)")
    plt.title("ln(I0) versus 1/T")

def bandgap():
    # From qVth
    vth = 4.2
    q = 1.6 * 10 ** -19
    print("Bandgap energy from qVth is " + str(q * vth) + " Joules")

    # from hc/lambda
    h = 6.626 * 10 ** -34
    c = 3 * 10 ** 8
    lambda1 = 405 * 10 ** -9
    print("Bandgap energy from hc/lambda is " + str(h * c / lambda1) + " Joules")

    # from ln(I0) versus 1/T
    k = 1.38 * 10 ** -23

    slope25 = 2.17
    vt25 = k * (273 + 25) / q
    n25 = 1 / (vt25 * slope25)
    print("n 25C = " + str(n25))

    slope30 = 2.21
    vt30 = k * (273 + 30) / q
    n30 = 1 / (vt30 * slope30)
    print("n 30C = " + str(n30))

    slope35 = 2.15
    vt35 = k * (273 + 35) / q
    n35 = 1 / (vt35 * slope35)
    print("n 35C = " + str(n35))

    intercept25 = -6.56
    intercept30 = -6.61
    intercept35 = -6.19
    
    lnIslope = np.polyfit([1/298, 1/303, 1/308], [intercept25, intercept30, intercept35], 1)[0]

    print("ln(I0) slope is " + str(lnIslope))

    # -slope = Eg/(n k)
    Eg25 = -lnIslope * n25 * k
    Eg30 = -lnIslope * n30 * k
    Eg35 = -lnIslope * n35 * k

    print("Eg 25 C = " + str(Eg25) + " Joules")
    print("Eg 30 C = " + str(Eg30) + " Joules")
    print("Eg 35 C = " + str(Eg35) + " Joules")

    averageEg = (Eg25 + Eg30 + Eg35) / 3
    print("Average bandgap energy from ln(I0) versus 1/T is " + str(averageEg) + " Joules")

bandgap()

plt.show()