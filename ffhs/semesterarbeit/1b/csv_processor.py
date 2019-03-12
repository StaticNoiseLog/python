import csv
 
with open('./ffhs/semesterarbeit/1b/ElektrischeEnergieEinfuhrAusfuhr.csv',
          encoding='utf-8',  # blub
          errors='strict',  newline=None) as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    data = [item for item in filereader]
 
for row in data:
    print("{0:10} {1:10} {2:10}".format(
        row[0], row[1], row[2]))
 
user_input = input("Show with pyplot? [N]y: ")
if not user_input.lower().startswith( 'y' ):
    raise SystemExit(0)
 
# https://pythonspot.com/matplotlib-bar-chart/
import numpy as np
import matplotlib.pyplot as plt
 
data_years = [row[0].replace('"', '') for row in data[1:]]
data_ausfuhr = [int(row[1]) for row in data[1:]]
data_einfuhr = [int(row[2]) for row in data[1:]]
n_groups = len(data_ausfuhr)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.5
opacity = 0.8
 
rects1 = plt.bar(index, data_ausfuhr,
alpha=opacity,
color='b',
label='Frank')
 
rects2 = plt.bar(index + bar_width, data_einfuhr,
alpha=opacity,
color='g',
label='Guido')
 
plt.xlabel(data[0][0].replace('"', ''))
plt.ylabel(data[0][1].replace('"', '') + "/" + data[0][2].replace('"', ''))
 
# plt.xlabel('Person')
# plt.ylabel('Scores')
plt.title('Elektrische Energie Ausfuhr/Einfuhr Ggw')
plt.xticks(index + bar_width, data_years)
plt.legend()
  
plt.tight_layout()
plt.show()
 
#plt.hist([row[1] for row in data[10:]], density=1, bins=len(data[0][0])-1)
#plt.bar([row[0].replace('"', '') for row in data[10:]], [row[1] for row in data[10:]])
#plt.bar(["one", "two", "three"], [20, 50, 15])
 
# weightList = [10, 20, 40, 25, 5]
# plt.hist(weightList, density=1, bins=20)
# plt.axis([50, 110, 0, 0.06])
 
 
 
# plot.axis([50, 110, 0, 0.06])
# #axis([xmin,xmax,ymin,ymax])
# plot.xlabel('Weight')
# plot.ylabel('Probability')
# plot.show()