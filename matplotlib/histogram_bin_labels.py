import matplotlib.pyplot as plt
import numpy as np

"""This function centers the bars on the bin labels,
but this is actually not correct: You get a bar labeled "0" and it
will hold the 4 years old person. So the label should be "0 to 10".
And this is what you (sort of) get with the default.
"""
def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42,
                   4, 99, 102, 11, 55, 30, 66, 72, 12, 22, 41, 58, 81]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')

plt.xticks(bins) # bin 1 holds 0-10, bin 2 is 10-20, etc.

#ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))

#bins_labels(bins, fontsize=10)

plt.show()
