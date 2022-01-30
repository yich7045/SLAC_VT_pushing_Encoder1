import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import collections


object = pd.read_pickle(r'evaluation_rewards.pkl')
steps = pd.read_pickle(r'evaluation_steps.pkl')
object = savgol_filter(object, 51, 3) # window size 51, polynomial order 3
plt.plot(steps, object)
plt.show()

