import matplotlib.pyplot as plt
country = ['united states','Brazil','India','Russia','France','Spain','Argentia','Colombia']
cases = [9937271,5614258,8439389,1733440,1601367,1365895,1217028,1117977]
plt.pie(cases, labels=country, autopct='%1.1f%%', startangle=90,
wedgeprops={"edgecolor":"1",'linewidth':1,
'linestyle': 'solid'})
# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
# Display the graph onto the screen
plt.show()
