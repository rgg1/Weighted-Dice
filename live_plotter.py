import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []

index = count()
def animate(i):
    # x_vals.append(next(index))
    # y_vals.append(random.randint(0, 5))
    data = pd.read_csv('data.csv')
    x = data['num_rolls']
    y1 = data['total_normal']
    y2 = data['total_weighted']
    
    plt.cla()
    
    plt.plot(x, y1, label="Normal Die")
    plt.plot(x, y2, label="Weighted Die")
    
    plt.legend(loc='upper left')
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
