### PRHW5

#### 1

立该警示牌的目的是：让更多的人穿救生衣 避免被淹死。

被淹死的前提下 穿救生。

根据样本
$$
被淹死的前提下 穿救生衣:\\
P(穿救生衣|被淹死)=\frac{1}{102}\\
P(不穿救生衣|被淹死)=\frac{101}{102}\\
那么：计算穿救生衣条件下，和不穿救生衣条件下的被淹死的概率\\
假设先验概率：P(被淹死)=P(存活)=\frac{1}{2}\\
P(被淹死|穿救生衣)=\frac{P(穿救生衣\mid被淹死)\times P(被淹死)}{P(穿救生衣)}\\
=\frac{P(穿救生衣\mid被淹死)\times P(被淹死)}{P(穿救生衣\mid被淹死)\times P(被淹死)+P(穿救生衣\mid存活)\times P(存活)}\\
=\frac{ \frac{1}{102} \times \frac{1}{2}}{\frac{1}{102}\times \frac{1}{2}+P(穿救生衣\mid存活)\times \frac{1}{2}}\\
=\frac{1}{1+P(穿救生衣\mid存活)\times 102}

$$
所以给出的数据并不足够。需要给出存活人数以及存活人数穿救生衣的概率。

#### 2

$$
P(A=i)为第i扇门后藏有汽车\\
P(i=1)=P(i=2)=P(i=3)=\frac{1}{3}\\
P(B=j)为参赛者选的第 j 扇门\\
P(j=1)=P(j=2)=P(j=3)=\frac{1}{3}\\
显然：A,B是独立事件\\
C为在事件A,B的条件下主持人打开的第k扇门(k\neq i,k\neq j)\\
D为事件ABC的条件下,是否换门(x=0 不换| x=1换)\\
P(k=1)=P(k=1,i=j)+P(k=1,i\neq j)\\
=P(k=1,i=j=3)+P(k=1,i=j=2)+P(k=1,i=2,j=3)+P(k=1,i=3,j=2)\\
=P(k=1|i=j=3)P(i=j=3)\\
+P(k=1|i=j=2)P(i=j=2)\\
+P(k=1|i=2,j=3)P(i=2,j=3)\\
+P(k=1|i=3,j=2)P(i=3,j=2)\\
=\frac{1}{2}\times \frac{1}{3}\times \frac{1}{3}\\
+\frac{1}{2}\times \frac{1}{3}\times \frac{1}{3}\\
+\frac{1}{3}\times \frac{1}{3}\\
+\frac{1}{3}\times \frac{1}{3}\\
=\frac{1}{3}\\
同理 P(k=2)=P(k=3)=\frac{1}{3}\\
不换门时：\\
中奖概率就是i=j时 \\
P(i=j)=P(i=j=1)+P(i=j=2)+P(i=j=3)=\frac{1}{3}\\
换门时
中奖概率就是i\neq j ：= 1-\frac{1}{3}=\frac{2}{3}
$$





实验结果：

不换门中奖概率是 324/1000

换门概率是 676/1000

![image-20240403214152357](/Users/wangsiwei/Library/Application Support/typora-user-images/image-20240403214152357.png)