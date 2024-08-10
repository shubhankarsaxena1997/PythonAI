# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

# FUNCTIONAL METHOD OF PLOTING

# plt.plot(x,y, 'r-') #r used to fill the color of plot

plt.title('Growth chart')
plt.xlabel('X')
plt.ylabel('Y')

# below used to plot subplots in a single frame
plt.subplot(1,2,1)
plt.plot(x, y , 'r')

plt.subplot(1,2,2)
plt.plot(y, x , 'b')


# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

# OBJECT ORIENTED METHOD OF PLOTING

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y, label='Sine Wave')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sine Wave')

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
ax1.plot(x,y, 'r')
ax1.set_title('LARGER PLOT')

ax2.plot(y,x, 'b')
ax2.set_title('SMALLER PLOT')
# %%

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

# below used to plot subplots in a single frame
fig, ax = plt.subplots(nrows=1, ncols=2)
# set layout if graph's value are overlapping 
# plt.tight_layout()

ax[0].plot(x,y)
ax[0].set_title("Initial Graph")

ax[1].plot(y,x)
ax[1].set_title("Resultant Graph")

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig,axes = plt.subplots(nrows=2, ncols=1,figsize=(8,2)) #figsize sets teh size of figure, currently its 8 inches in width and 2 inches in height
# fig = axes.add_axes([0,0,1,1])
axes.set_xlable("X")

axes[0].plot(x,y)
axes[1].plot(y,x)
fig.savefig('plt.jpg')

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

fig = plt.figure()
axes = fig.add_axes(([0,0,1,1]))
axes.plot(x,y, 'g', lw=2, marker='o')

# %%
