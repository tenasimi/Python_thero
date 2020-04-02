from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
# all population in millions
populations = [1120, 1029, 329, 65, 215, 212, 204]
# generate random colors from pltc module
colors = sample(list(pltc.cnames.values()), len(populations))
# or set this color combination for same output
#colors = ['#00CED1', '#F4A460', '#808080', '#B8860B', '#FA8072', '#696969']

# labels for pie chart
country = ["China", "Turkey", "US","Russia", "Indonesia", "Brasil", "Pakistan"]
# cut out size for china part from slice
space_slice = [0.02,0,0,0,0,0,0]
# width and height of plot
plt.figure(figsize=(6,5)) # razmer krugovoy diagrammi
# create pie chart and feed population %, colors and label
plt.pie(populations, labels = country, autopct='%1.1f%%',
        shadow = False, explode = space_slice, colors=colors)
# show scale and location for scale
plt.legend(country, loc=(-0.25, 0.7), shadow = False)
plt.show()
