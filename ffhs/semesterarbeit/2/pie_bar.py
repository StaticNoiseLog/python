import matplotlib.pyplot as plt
import numpy as npy

texts, percentages = npy.loadtxt('programming_language_popularity.csv',
                                 delimiter=',',
                                 comments='‡',  # C# is a popular language, can't use hashtag as comment
                                 dtype={'names': ('text', 'percentage'),
                                        'formats': (npy.dtype('U255'), npy.float)},
                                 unpack=True,  # return two unpacked values
                                 skiprows=0)

percentages_provided_total = npy.sum(percentages)
if percentages_provided_total < 100:
    percentages = npy.append(percentages, 100 - percentages_provided_total)
    texts = npy.append(texts, 'übrige')

fig = plt.figure(figsize=(10, 5))
fig.suptitle('Populäre Programmiersprachen (Google Trends)')

# pie chart
plt.subplot(1, 2, 1)
plt.pie(percentages,
        labels=texts,
        startangle=90,
        autopct='%1.1f%%')  # show percentages

# bar chart
plt.subplot(1, 2, 2)
plt.bar(texts, percentages, width=0.5, align="center")
plt.xlabel('Programmiersprache')
plt.ylabel('Prozent')
plt.grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
