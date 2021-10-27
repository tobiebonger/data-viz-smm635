# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# set seed
np.random.seed(666)

# periods
p = 11

# sub-population size
s = 500

# simulate data
e = []

for i in range(s):
    for j in np.arange(1, p, 1):
        r = np.exp(j) * np.random.uniform(0.1, 1)
        e.append([i, j, r, 'e'])
        
        
df = pd.concat([e], axis=0, )

e = pd.DataFrame(e, columns=['i', 'j', 'r', 'g'])

c = pd.DataFrame(df.groupby('j', as_index=False)['r'].agg(np.mean))

# create figure
fig = plt.figure(figsize=(9, 6))

# add chart
ax = fig.add_subplot(1, 1, 1)

# plot data
x, y = c.j, c.r
ax.plot(x, y, marker='o' , markersize=10)

# title
ax.set_title('Average sales by start-up age')

# axes
ax.set_xlabel('Time elapsed (years)')
ax.set_ylabel('Sales (K)')

# show plot
plt.show()