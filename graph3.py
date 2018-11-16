import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14) })
 
# All the possibility of style:
possibilities = [u'seaborn-darkgrid', u'seaborn-notebook', u'classic', u'seaborn-ticks', u'grayscale', u'bmh', u'seaborn-talk', u'dark_background', u'ggplot', u'fivethirtyeight', u'_classic_test', u'seaborn-colorblind', u'seaborn-deep', u'seaborn-whitegrid', u'seaborn-bright', u'seaborn-poster', u'seaborn-muted', u'seaborn-paper', u'seaborn-white', u'seaborn-pastel', u'seaborn-dark', u'seaborn', u'seaborn-dark-palette']
 
# Initialise figure
my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
 
# Let's do a chart per possibility:
for n, v in enumerate(possibilities):
print n,v
 
# I set the new style
plt.style.use(v)
 
# Start new place in the figure
plt.subplot(5 ,5, n + 1)
 
# multiple line plot
for column in df.drop('x', axis=1):
plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.4)
 
# And highlith one
plt.plot(df['x'], df['y5'], marker='', color='orange', linewidth=4)
 
# Add a title to say which style it is
plt.title(v, fontsize=10, fontweight=0, color='grey', loc='left')
 
# remove labels
plt.tick_params(labelbottom='off')
plt.tick_params(labelleft='off')
 
# save
plt.savefig('PNG/#199_Matplotlib_style_sheet.png', dpi=96, bbox_inches='tight')
