import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0,0.5,10000)

plt.hist(vals,50)
plt.show()

print('Percentile !!!',np.percentile(vals,50)) # 50th percentile. another name for median

print('Percentile !!!',np.percentile(vals,90)) # 90th percentile

print('Percentile !!!',np.percentile(vals,20)) # 20the percentile
