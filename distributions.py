import numpy as np
import matplotlib.pyplot as plt

values = np.random.uniform(-10.0,10.0,100000)
plt.hist(values,50)
plt.show()


# Normal/Gaussian distribution

from scipy.stats import norm
import matplotlib.pyplot as plt

x= np.arange(-3,3,0.001)
plt.plot(x,norm.pdf(x))
plt.show()


#Poisson Probability mass function

from scipy.stats import poisson
import matplotlib.pyplot as plt

mu = 500
x = np.arange(400,600,0.5)
plt.plot(x,poisson.pmf(x,mu))
plt.show()