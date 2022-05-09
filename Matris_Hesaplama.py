
from calendar import c
import numpy as np


print("Matrislerin satir sayisini giriniz (m)=")
m = int(input())
print("Matrislerin sutun sayisini giriniz (n)=")
n = int(input())

A = [[0 for i in range(n)] for i in range(m)]

print("A matrisini giriniz:")
for i in range(m):
    for j in range(n):
        print('A[{}][{}]'.format(i+1, j+1))
        A[i][j] = int(input())

B = [[0 for i in range(n)] for i in range(m)]

print("B matrisini giriniz:")
for i in range(m):
    for j in range(n):
        print('B[{}][{}]'.format(i+1, j+1))
        B[i][j] = int(input())
print("A matrisi :", A)
print("B matrisi :", B)
C = [[0 for i in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]

print("A+B Matrislerinin Toplamı:", C)

deta1=np.array(C)
np.linalg.det(deta1) 
print ("Determinantı: ", np.linalg.det(deta1))