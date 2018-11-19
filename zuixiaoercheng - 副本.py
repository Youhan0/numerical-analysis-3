"""
2018/10/1
23116207 Youhan0
"""

import numpy as np;
import sympy as sy;
import matplotlib.pyplot as plt;

'''基函数内积'''
def get_fai(W,X,i,j,M):
    t=0;
    for k in range(M):
        t=t+W[k]*(X[k]**i)*(X[k]**j);
    return t;

'''f(x)和基函数内积'''
def get_f_fai(W,X,Y,j,M):
    t=0;
    for k in range(M):
        t=t+W[k]*(Y[k])*(X[k]**j);
    return t;

'''法方程的矩阵G'''
def get_G(W,X,M,N):
    G=np.mat(np.zeros((N+1,N+1)));
    for k in range(N+1):
        for l in range(N+1):
            G[k,l]=get_fai(W,X,k,l,M);
    return G;

'''法方程的矩阵D'''
def get_D(W,X,M,N):
    D=np.mat(np.zeros((N+1,1)));
    for k in range(N+1):
        D[k]=get_f_fai(W,X,Y,k,M);
    return D;


'''main'''

'''使用如下数据进行最小二乘拟合'''
X=[1,2,3,4,5];
Y=[4,4.5,6,8,8.5];
W=[2,1,3,1,1]; #权值

M=len(X); #离散点个数
N=int(input("输入拟合多项式次数："));

G=get_G(W,X,M,N)
D=get_D(W,X,M,N); #生成矩阵G和D

A=(G.I)*D;        #生成矩阵A

x=sy.Symbol("x");
def L(x):
    t=0;
    for i in range(N+1):
        t=t+A[i]*(x**i);
    return t;     #生成拟合曲线

xx=[];
yy=[];
     
i=0.0;
while i<=M+1:
    xx.append(i);
    yy.append(float(L(i)));
    i=i+0.1;

plt.plot(X,Y,linestyle='',marker='*', color='b');
plt.plot(xx,yy,linestyle='--',color='r');
