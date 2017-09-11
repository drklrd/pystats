import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0,0.5,10000)

plt.hist(vals,50)
plt.show()

print('First moment -> mean',np.mean(vals)) # First moment or mean

print('Second moment -> variance',np.var(vals)) # Second moment or variance

import scipy.stats as sp
print('Third -> skew',sp.skew(vals)) # Third moment or skew


print('Fourth -> kurtosis',sp.kurtosis(vals)) # Fourth moment or kurtosis
