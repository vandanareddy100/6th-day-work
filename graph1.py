import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
student= ('jones')


marks = (25, 32, 30, 35, 29)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, student, bar_width,
alpha=opacity,
color='g',
label='student')

rects2 = plt.bar(index + bar_width, marks, bar_width,
alpha=opacity,
color='r',
label='marks')

plt.xlabel('marks')
plt.ylabel('Student')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()

