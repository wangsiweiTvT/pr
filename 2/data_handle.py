import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('origin.xlsx', sheet_name='Sheet1', header=0)

df = df.set_axis(['no', 'create_time', 'gender', 'height', 'weight', 'age', 'lenth'], axis='columns')

df = df[df['age'] < 100]
df = df[df['lenth'] > 20]
for index, row in df.iterrows():
    height =str(row['height']).replace(" ", "")
    weight = str(row['weight']).replace(" ", "")
    if ( row['lenth'] > 100):
        df.loc[index,'lenth']=row['lenth']/10
    elif(row['lenth']>35):
        df.loc[index, 'lenth']=(row['lenth']*5+50)/10

    if(height[-1]=='m' or height[-1] == '米'):
        df.loc[index, 'height']=np.float64(height[:-1])
    elif(np.float64(height)>100):
        df.loc[index, 'height']=np.float64(height)/100
    else:
        df.loc[index, 'height'] = np.float64(height)

    if(weight[-1]=='g' or weight[-1]=='G'or weight[-1]=='克'):
        df.loc[index, 'weight']=np.float64(weight[:-2])
    elif(np.float64(weight)>140):
        df.loc[index, 'weight']=np.float64(weight)/2
    else:
        df.loc[index, 'weight'] = np.float64(weight)



df = df.astype({'height':'float','weight':'float'})



df_male = df[df['gender'] == 1]
df_female = df[df['gender'] == 2]

from numpy import *

df_male['height'] = df_male['height'] - df_male.describe().loc['mean', 'height']
df_male['weight'] = df_male['weight'] - df_male.describe().loc['mean', 'weight']
df_male['age'] = df_male['age'] - df_male.describe().loc['mean', 'age']
df_male['lenth'] = df_male['lenth'] - df_male.describe().loc['mean', 'lenth']

male_metric_df = df_male.iloc[:, 3:7]

male_metric_mat = mat(male_metric_df)

m = male_metric_mat.shape[0]

# 将矩阵转置
transposed_matrix = np.transpose(male_metric_mat)
# transposed_matrix.shape
# cov = np.cov(transposed_matrix)
# print(cov)

# 计算协方差矩阵
cov = transposed_matrix.dot(male_metric_mat) / m
print(cov)

# 计算特征值
eig_vals, eig_vecs = np.linalg.eig(cov)

print("特征值:", cov)
print("特征向量:", cov)




# plt.scatter(list(df_male['height']),list(df_male['weight']),c='b')
# plt.scatter(list(df_female['height']),list(df_female['weight']),c='r')
# plt.show()

# plt.scatter(list(df_male['lenth']),list(df_male['weight']),c='b')
# plt.scatter(list(df_female['lenth']),list(df_female['weight']),c='r')
# plt.show()


# plt.scatter(list(df_male['lenth']),list(df_male['height']),c='b')
# plt.scatter(list(df_female['lenth']),list(df_female['height']),c='r')
# plt.show()


print(df_male.describe())
print(df_male.describe().loc['25%','height'])
print(df_male.describe().loc['25%','weight'])
print(df_male.describe().loc['25%','lenth'])

print(df_male.describe().loc['75%','height'])
print(df_male.describe().loc['75%','weight'])
print(df_male.describe().loc['75%','lenth'])

df_male = df_male[(df_male['height'] >=df_male.describe().loc['25%','height']) & (df_male['height']<=df_male.describe().loc['75%','height'])
                  & (df_male['weight'] >=df_male.describe().loc['25%','weight']) & (df_male['weight']<=df_male.describe().loc['75%','weight'])
                  & (df_male['lenth'] >=df_male.describe().loc['25%','lenth']) & (df_male['lenth']<=df_male.describe().loc['75%','lenth'])]



df_female = df_female[(df_female['height'] >=df_female.describe().loc['25%','height']) & (df_female['height']<=df_female.describe().loc['75%','height'])
                  & (df_female['weight'] >=df_female.describe().loc['25%','weight']) & (df_female['weight']<=df_female.describe().loc['75%','weight'])
                  & (df_female['lenth'] >=df_female.describe().loc['25%','lenth']) & (df_female['lenth']<=df_female.describe().loc['75%','lenth'])]





# print(list(df_male["height"]))

# plt.scatter(list(df_male['height']),list(df_male['weight']),c='b')
# plt.scatter(list(df_female['height']),list(df_female['weight']),c='r')
# plt.show()


# plt.scatter(list(df_male['lenth']),list(df_male['weight']),c='b')
# plt.scatter(list(df_female['lenth']),list(df_female['weight']),c='r')
# plt.show()


# plt.scatter(list(df_male['lenth']),list(df_male['height']),c='b')
# plt.scatter(list(df_female['lenth']),list(df_female['height']),c='r')
# plt.show()