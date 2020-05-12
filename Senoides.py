# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:25:31 2020

@author: edels
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero

t = np.linspace(0, 2 * np.pi, 15)
V = np.sin(t)

fig = plt.figure(figsize = (1, 1))
ax = SubplotZero(fig, 1, 1, 1)
fig.add_subplot(ax)
ax.axis["xzero"].set_visible(True)

for n in ["bottom", "top", "right"]:
    ax.axis[n].set_visible(False)
    
# Step graph   
ax.step(t, V, color = "black", linewidth = 2)

# Stem graph
#(markerline, stemlines, baselines) = ax.stem(t, V, linefmt = "black", basefmt = " ", use_line_collection = True)
#plt.setp(markerline, color = "black", markersize = 3) # Allow to edit stem markerline color

# Continuous line graph
#ax.plot(t, V, color = "black", linewidth = 2)

ax.set_yticks([]) # Remove the vertical ticks
ax.set_xticks([]) # Remove the horizontal ticks
fig.text(0.9, 0.37, "t", fontsize = 10) # Horizontal legend
fig.text(0.01, 0.77, "V", fontsize = 10) # Vertical legend
#plt.show()
plt.savefig("../Imagens/Conversores_de_Dados/Grafico_Senoide_Step.svg", dpi = 300)