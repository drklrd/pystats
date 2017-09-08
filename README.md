## Major types of data

- Numerical
	- Quantitative measurement
	- Discreate, Continuos

- Categorical
	- Qualitative data with no inherent mathematical meaning
	- Gender, Yes/no

- Ordinal
	- Mixture of numerical and categorical
	- Rating of a movie

## Mean, Median and Mode

```
Mean : Average

0,2,3,2,1,0,0,2,0

Mean = (0+2+3+2+1+0+0+2+0) / 9 = 1.11

```

```
Sort the values and take the value at midpoint

0,2,3,2,1,0,0,2,0

Sort it :

0,0,0,0,1,2,2,2,3
        *

```

Median is less susceptible to outliers than mean

Eg: Mean houseold income in US is $72,641 but the median is $52,939 as the mean is skewed by some billionaires

Median better represents the typical American in this example


```
Mode : The most common value in data set
Not relevant to continuous numerical data
```

## Standard deviation, Variance

Measures how "spread-out" the data is.

Variance is simply the average of the squared differences from the mean.

Standard deviation is just the square root of the variance. This is usually a way to identify outliers. Data points that lie more than one standard deviation from the mean can be considered unusual. We can talk about how extreme a data point is by talking about "how many sigmas" away from the mean it is.


## Population variance vs Sample variance

For N samples, we just divide the squared variances by N-1 instead of N.



## Probability density functions(Continuous data)

Example - A normal distribution

Gives the probability of a data point falling within some given range of a given value


## Probability mass functions(discrete data)

For discrete data.



## Examples of Data distributions

### Uniform distribution

Flat constast probability of a value occuring within a given range. Unlike normal distribution where the concentration is around the mean, the uniform distribution has equal probality across any given value within the range we define

### Normal/Gaussian

### Exponential PDF / "Power Law"

### Binomial probability mass function(discrete data)

### Poisson probability mass function(discrete data)

A website has an average 500 visits per day. Whats the odds of getting 550 ?

```
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

```







