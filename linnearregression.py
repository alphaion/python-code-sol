#matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figSize']=(20.0, 10.0)

data = pd.read_csv('headbrain.csv')
print(data.shape)
data.head()

X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)
n = len(X)
numer = 0
denom = 0
for i in range(n):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
    b1 = numer/denom
    b0 = mean_y -(b1*mean_x)
    print(b1,b0)

max_x = np.max(X)+100
min_x = np.min(X)-100
x = np.linspace(min_x,max_x,1000)
y = b0+b1*n

plt.plot(x,y,color="#586970", label="Re")
plt.scatter(X,Y,c ="#ef5423", label = "scatter")

plt.xlabel("head")
plt.ylabel("body")
plt.legend()
plt.show()




