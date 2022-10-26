import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

index = count()
def animate(i):
    data = pd.read_csv('data.csv')
    x = data['num_rolls']
    y1 = data['total_normal']
    y2 = data['total_weighted']
    
    plt.cla()
    
    plt.plot(x, y1, label="Normal Die")
    plt.plot(x, y2, label="Weighted Die")
    plt.title("Weighted vs. Normal Die")
    plt.xlabel("Rolls Thrown")
    plt.ylabel("Total Sum")
    plt.legend(loc='upper left')
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
