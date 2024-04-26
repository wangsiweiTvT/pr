import matplotlib.pyplot as plt
import numpy as np

c1 = np.array([[1,2],[2,3],[3,3],[4,5],[5,5]])
c2 = np.array([[1,0],[2,1],[3,1],[3,2],[5,3],[6,5]])

print(c1)
print(c2)

plt.scatter(x=c1[:,0],y=c1[:,1],c='r')
plt.scatter(x=c2[:,0],y=c2[:,1],c='b')
# plt.show()

# 2、Fisher算法实现
def cal_cov_and_avg(samples):
    """
    给定一个类别的数据，计算协方差矩阵和平均向量
    :param samples:
    :return:
    """
    u1 = np.mean(samples, axis=0)
    cov_m = np.zeros((samples.shape[1], samples.shape[1]))
    for s in samples:
        t = s - u1
        cov_m += t*t.reshape(2, 1)
    return cov_m, u1
def fisher(c_1, c_2):
    """
    fisher算法实现(参考上面的推导公式进行理解)
    :param c_1:
    :param c_2:
    :return:
    """
    cov_1, u1 = cal_cov_and_avg(c_1)
    cov_2, u2 = cal_cov_and_avg(c_2)
    #计算样本类内离散度矩阵Si Sw
    s_w = cov_1 + cov_2
    # u, s, v = np.linalg.svd(s_w)
    # s_w_inv = np.dot(np.dot(v.T, np.linalg.inv(np.diag(s))), u.T)
    return np.dot(np.linalg.inv(s_w), u1 - u2)




w = fisher(c1, c2).reshape(1, -1)       # 调用函数，得到参数w
print(w)


plt.scatter(c2[:, 0], c2[:, 1], c='k', marker='o', label='c2')
plt.scatter(c1[:, 0], c1[:, 1], c='r', marker='x', label='c1')


x_tmp = np.linspace(-1, 1)
y_tmp = x_tmp * w[0, 1] / w[0, 0]
plt.plot(x_tmp, y_tmp, '#808080', linewidth=1)

wu = w / np.linalg.norm(w)


# 正负样板店
c1_project = np.dot(c1, np.dot(wu.T, wu))
plt.scatter(c1_project[:, 0], c1_project[:, 1], c='r', s=15)
for i in range(c1.shape[0]):
    plt.plot([c1[i, 0], c1_project[i, 0]], [c1[i, 1], c1_project[i, 1]], '--r', linewidth=1)

c2_project = np.dot(c2, np.dot(wu.T, wu))
plt.scatter(c2_project[:, 0], c2_project[:, 1], c='k', s=15)
for i in range(c2.shape[0]):
    plt.plot([c2[i, 0], c2_project[i, 0]], [c2[i, 1], c2_project[i, 1]], '--k', linewidth=1)

plt.axis("equal")  # 两坐标轴的单位刻度长度保存一致
plt.show()

