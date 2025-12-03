# Inductance as a function of core permeability
import numpy as np
import matplotlib.pyplot as plt

# permeability of free space
mu0 = np.pi * 4.e-7

# Dimensions of the core in meters
Ac = 9e-4 # core area
Ag = 9e-4 # air-gap area
g = 5e-4 # air-gap length
lc = 0.3 # core mean length
N = 500 # turns wounded

# Permeability range
mu_r = np.linspace(100, 100000, 101)

# Reluctance (ampere turns per weber)
Rg = g / (mu0 * Ag) # air-gap reluctance

Rc = lc / (mu_r * mu0 * Ac)

# Total reluctance
R_total = Rg + Rc

# Inductance
L = N ** 2 / R_total

# Plot
plt.plot(mu_r, L,
         label= "Inductance vs relative permeability")

plt.xlabel("Core relative permeability $\\times 10^4$")
plt.ylabel("Inductance (H)")

plt.title("Inductance as a function of core relative permeability")


x_ticks = np.arange(0, 100001, 10000)
x_tick_labels = x_ticks / 10000
plt.xticks(x_ticks, labels=[f'{int(x)}' for x in x_tick_labels])

plt.grid(True)
plt.ylim(0, 0.7)
plt.show()