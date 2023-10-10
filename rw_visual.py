#Frontend portion for the data visualization CS project

import matplotlib.pyplot as plt 

from random_walk import RandomWalk

##Continues to make a random walk as long as the program is active.
while True:
#Makes a random walk and plots the points.

  rw = RandomWalk()

  rw.fill_walk()
  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

  #Emphasizes the first and last points. 
  plt.scatter(0,0, c='green', edgecolors='none', s=100)
  plt.scatter(rw.x_values[-1], c='red', edgecolors='none', s=100)
  
  plt.show()

  con_running = input("Make another walk? (y/n: ")
  if con_running == 'n':
    break
