"""
This is a modified matrix multiplication code
"""
############################################# 


import numpy as np
import numpy.linalg as la
import math

def driver():

     n = 2
     y = np.array([[1,2],[3,4]])
     w = np.array([[5,6],[7,8]])

# evaluate the matrix multiplication of y and w     
     mp = matmul(y,w,n)

# print the output
     print('the matrix product is : ', mp)

     return
     
def matmul(y,w,n):
#   Computes the matrix multiplication of matrices y, w
 
     
     rowsY, columnsY = y.shape
     rowsW, columnsW = w.shape
     
     mp = np.zeros((rowsY, columnsW))
     
     for i in range(rowsY):
          for j in range(columnsW):
               for k in range(columnsY):
                    mp[i, j] = mp[i, j] + y[i, k] * w[k, j]
        

     return mp  
     
driver()               
