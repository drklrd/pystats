import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(200.0,20.0,10000)

print('Standard deviance',incomes.std())
print('Variance',incomes.var())


plt.hist(incomes,50)
plt.show()

