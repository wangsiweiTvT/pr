import matplotlib.pyplot as plt

x1=[0,1,3,5,6]
x2=[1,3,4,5,7]

y1=[0,100,200,100,0]
y2=[0,150,300,150,0]


# 假设x1是正类.x2负类 x<= a 那么归为 正类. a={0,1,3,4,5,6,7}

TPR=[0.2,0.4,0.6,0.6,0.8,1,1]
FPR=[0,0.2,0.4,0.6,0.8,0.8,1]

plt.plot(TPR,FPR,c = 'r')
plt.show()