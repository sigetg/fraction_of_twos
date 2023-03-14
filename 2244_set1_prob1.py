#Author: George Sigety

import numpy as np
import matplotlib.pyplot as plt
import random

#function to create roll array
def create_roll_array():
    i = 0
    randomNums = [None] * 1000
    while i < 1000:
        randomNums[i] = random.randint(1, 6)
        i += 1
    return randomNums

#function to create array of fraction of twos
def fraction_of_twos_array(randomNums):
    fraction_of_twos = [None] * 1000
    i = 0
    twos = 0
    while i < 1000:
        if randomNums[i] == 2:
            twos += 1
        if i == 0:
            fraction_of_twos[i] = 0
        else:
            fraction_of_twos[i] = twos / i
        i += 1
    return fraction_of_twos
    
#determine running fraction of twos for 1000 random rolls
randomNums = create_roll_array()
fraction_of_twos = fraction_of_twos_array(randomNums)

#Plot Setup
plt.title("Running Fraction of Twos Over 1000 Dice Rolls")
plt.xlabel("Number of Rolls")
plt.ylabel("Running Fraction of Twos")
x = np.arange(0, 1000, 1)
y = fraction_of_twos
plt.yticks([1/6, 2/6, 3/6, 4/6, 5/6, 1],[r'$\frac{1}{6}$',r'$\frac{2}{6}$',\
    r'$\frac{3}{6}$',r'$\frac{4}{6}$', r'$\frac{5}{6}$', r'$1$'])
plt.plot(x, y)
#show plot
plt.show()



