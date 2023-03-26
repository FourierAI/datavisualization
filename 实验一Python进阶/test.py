import matplotlib.pyplot as plt
import numpy as np

plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3, rowspan=1)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2, rowspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), colspan=1, rowspan=2)
plt.tight_layout()
plt.show()