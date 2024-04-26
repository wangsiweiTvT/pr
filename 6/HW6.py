import numpy as np
import matplotlib.pyplot as plt



def uni_sample():
    return np.random.random(1)-0.005

def avg(n):
    sum = 0
    for i in range(n):
        sum=sum+uni_sample()
    return sum/n

def dataset(m,n):
    x=dict()
    y=list()
    for i in range(100):
        x[i/100]=0
    for i in range(m):
        v=avg(n)
        k=float(np.around(v,decimals=2))
        y.append(k)
        x[k]=x[k]+1
    return list(x.keys()),list(x.values()),y


def loguniform(low=0, high=1, size=None):
    return 2**(np.random.uniform(low, high, size))

def avg_logu(n):
    sum = 0
    for i in range(n):
        sum=sum+loguniform(2,25)
    return sum/n

def dataset_logu(m,n):
    y=list()
    for i in range(m):
        v=avg_logu(n)
        k=float(np.around(v,decimals=2))
        y.append(k)
    return y


if __name__ == '__main__':
    y = dataset_logu(100,1)
    print(y)

