# create some fake income data centered around 27,000 with normal distribution and standard deviation of 15,000 with 10,000 datapoints
# Then compte the mean average- it should be close to 27,000

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(27000,15000,10000)
print('MEAN',np.mean(incomes))
print('MEDIAN',np.median(incomes))



# Now lets add an outlier

incomes = np.append(incomes,[100000000])

# Median wont change much but mean does

print('MEAN after OUTLIER',np.mean(incomes))
print('MEDIAN after OUTLIER',np.median(incomes))


# show in plot
# plt.hist(incomes,50)
# plt.show()


# MODE

ages = np.random.randint(18,high=90,size=500)

from scipy import stats
print('MODE ', stats.mode(ages))