# coding=UTF-8

import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)
plt.style.use('ggplot')

'''
X = np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
Yb = np.cos(X)
plt.plot(X, Ya)
plt.plot(X, Yb)
plt.show()

def pdf(X, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (X - mu) ** 2)

X = np.linspace(-6, 6, 1000)
for i in range(5):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(X, pdf(X, mu, sigma), color = '.75')
plt.plot(X, pdf(X, 0., 1.), color = 'k')
plt.show()'''

data = [5., 25., 50., 20.]
print(range(len(data)))
plt.bar(range(len(data)), data, width=0.2)
plt.show()

