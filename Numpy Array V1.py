#Creating array examples
from imaplib import Commands

import numpy as np
# x=[1,2,3,4]
# y = np.array(x)
# print(y)
#  #Output:
# #  [1 2 3 4]

#aCREATING AN empty list and appending values to it
# l = []

# for i in range(1,5):
#     int_1 = int(input("enter:"))
#     l.append(int_1)

# print(np.array(l))

#Output
# enter:1
# enter:2
# enter:3
# enter:4
# ['1' '2' '3' '4'] Without typecasting the code is interpreted as strings
# enter:1
# enter:2
# enter:3
# enter:4
# [1 2 3 4]With typecasting

#Types of array:
#1d []
#2D[]
#3D[[[]]]
#for higher dimensional arrays...use the following process

# ar2 = np.array([[1,2,3,4],[1,2,3,4]])
# print(ar2)
# print(ar2.ndim)

# #The .ndim gives the dimension of the array, also the no of values in the ist must match, one can't be 3 another 4 values long
# Output:
#  [[1 2 3 4]
#  [1 2 3 4]]
# 2

#How to create multidimensional array from the given data
# arn = np.array([1,2,3,4], ndmin = 10)
# print(arn)
# print(arn.ndim)

# #Output:
# [[[[[[[[[[1 2 3 4]]]]]]]]]]
# 10

#Special Numpy Array
#Array filled with 0's
# ar_zero = np.zeros(4)
# ar_zero1 = np.zeros((3,4))
# print(ar_zero)
# print()
# print(ar_zero1)

# #Output:
# [0. 0. 0. 0.]

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

## similarly for 1's
# an empty array

# ar_em = np.empty(4)
# print(ar_em)

#prints the vreiosuly recorded data

##For printing a range of valuesL
# ar_rn = np.arange(4) #arange from 0 1 2 3
# print(ar_rn) 

#diagonal
# ar_dia = np.eye(3)
# print(ar_dia)
# #Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# ar_dia = np.eye(3,5)
# print(ar_dia)

# #Output:
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]

# Linspace:
# ar_lin = np.linspace(0,20,num=5)
# print(ar_lin)
#Output
# [ 0.  5. 10. 15. 20.]

#Random values between 0-1
# Rand() #Generates alues between 0 and 1 randomly
# var = np.random.rand(4)
# print(var)

# #Output:
# [0.05445057 0.57502515 0.25617439 0.34944643]

# var = np.random.rand(2, 5)
# print(var)
# #Output:
# [[0.03490295 0.51844013 0.52709037 0.86004245 0.9401254 ]
#  [0.54378456 0.58313265 0.45400154 0.23017164 0.94020337]]

# randn(): values close to zero
# var2 = np.random.randn(5)
# print(var2)

# #Output:
# [ 1.20832746  1.03272677 -0.2840104  -0.22478022 -0.79750366]

#ranf() #Functions for doign random sampling in numpy, [0.0, 1.0]
# var3 = np.random.ranf(5)
# print(var3)

# #Output
# [0.5338181  0.79683996 0.43212791 0.37521724 0.68591416]

# randint(): functions used to generatea random number between a given range
# randint(min, max, totalvalue)
# var3 = np.random.randint(5, 20, 5)
# print(var3)


#Data types:
# var = np.array([1,2,4,5,6,6,7,8,9])
# print("Data type:", var.dtype)

# var = np.array([1.0, 1.2, 1.3])
# print("Data type:", var.dtype)

# var = np.array(["A", "S", 1.2, 1.3])
# print("Data type:", var.dtype)

# #Output:
# Data type: int64
# Data type: float64
# Data type: <U32

#Type conversion

# x1 = np.array([1,2,3,4],dtype= np.int8)#1 way of changing tdata type
# print("data type:",x1.dtype)
# print(x1)

# x1 = np.array([1,2,3,4],dtype= "f")#another way of changing data type
# print("data type:",x1.dtype)
# print(x1)

# #Output:
# data type: int8
# [1 2 3 4]
# data type: float32
# [1. 2. 3. 4.]

# x2 = np.array([1,2,3,4])
# new = np.float32 (x2) #Changing data types as a function
# new_one = np.int_(new)
# print("Data type:", x2.dtype)
# print("Data type:", new.dtype)
# print(x2)
# print(new)
# print(new_one)

# # #Output:
# # Data type: int64
# # Data type: float32
# # [1 2 3 4]
# # [1. 2. 3. 4.]
# # [1 2 3 4]

#Numpy Arithmetic operations:

# var = np.array([1,2,3,4])
# var1 = np.array([1,2,3,4])
# varadd = var + 3
# varsub = var - 3
# varadd1 = var + var1
# print(varadd)
# print(varsub)
# print(varadd1)

# #Output:
# # [4 5 6 7]
# [-2 -1  0  1]
# [2 4 6 8]

#Adding with the use of inbuilt functions
# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# varadd = np.add(var1,var2)
# print(varadd)

#FOR 2D arrays
# var21 = np.array([[1,2,3,4],[1,2,3,4]])
# var22 = np.array([[1,2,3,4],[1,2,3,4]])
# print(var21)
# print()
# print(var22)
# print()
# varadd2 = var21 + var22
# print(varadd2)

# #OUTPUT:
# [1 2 3 4]
#  [1 2 3 4]]

# [[1 2 3 4]
#  [1 2 3 4]]

# [[2 4 6 8]
#  [2 4 6 8]]

# Arithmetic FunctionsL
# var = np.array([1,2,3,4,5,2])
# print("min:", np.min(var), np.argmin(var))
# print("max:", np.max(var), np.argmax(var))
# print("sqrt:",np.sqrt(var)) #gives the square root


# #Output:
# min: 1 0(gives the minimum value and the index position of it)
# max: 5 4
# sqrt: [1.         1.41421356 1.73205081 2.         2.23606798 1.41421356]

# var1 = np.array([[2,1,3],[9,5,6]])
# print(np.min(var1,axis=1)) #axis=1 (Row)
# print(np.min(var1,axis=0)) #axis=0 (column)

# #Output:
# [1 5]
# [2 1 3]

# var2 = np.array([1,2,3])
# print(np.sin(var2))
# print(np.cos(var2))
# print(np.cumsum(var2))

# #cumsum gives 1+2=3 and 1+2+3=6
# [0.84147098 0.90929743 0.14112001]
# [ 0.54030231 -0.41614684 -0.9899925 ]
# [1 3 6]

#Shape and reshaping

# var = np.array([[1,2,3,4],[1,2,3,4]])
# print(var)
# print()
# print(var.shape)

#OUTPUT:
# #[[1 2 3 4]
#  [1 2 3 4]]

# (2, 4) No of rows = 1, no of columns = 4

#SHAPING
# var1 = np.array([1,2,3,4], ndmin=4)
# print(var1)
# print(var1.ndim)
# print()
# print(var1.shape)

# #output:
# [[[[1 2 3 4]]]]
# 4

# (1, 1, 1, 4)

#Couldn'T VISUALISE THE ABOVE CONCEPT

#RESHAPING
# var2 = np.array([1,2,3,4,5,6])
# x = var2.reshape(3,2) (if there was var2.reshape(3,3) instead of (3,2) then the no of columns can't be established since the no of data is not enough and there should at least be 9 of the datum)
# print(x)

# #Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# var2 = np.array([1,2,3,4,5,6,7,8,9])
# x = var2.reshape(3,3) 
# print(x)

# #Output
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


# var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(var3)
# print(var3.ndim)

# print()

# x1 = var3.reshape(2,3,2)
# print(x1)
# print(x1.ndim)

#Output: converts the 1D array into 3D by passing it as 2 different amtrixes of size 3*2
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]
# 3



#Broadcasting:
# when does it come?
#the dimensions are equal and if not
# (1,3) and (1,1) watch the sizes from right side, and the operation will only occur if either the value is common or 1
# how are they added?
# (3,3) and (3,1) so the the max number is (3,3)

# var1 = np.array([1,2,3])
# print(var1.shape)
# print()
# print(var1)
# print()

# var2 = np.array([[1],[2],[3]])
# print(var2.shape)
# print()
# print(var2)
# print()

# print(var1+var2)

# #Output:
# (3,)

# [1 2 3]

# (3, 1)

# [[1]
#  [2]
#  [3]]

# [[2 3 4] [1+1 2+1 3+1]
#  [3 4 5] [1+2 2+2 3+2]
#  [4 5 6]] [1+3 2+3 3+3]

# [1 2 3] (1 2 3 4)
# (1*3)     (1*4) (1 and 1 compatible, 3 and 4 not compatible so they can't be added)

#INDEXING NUMPY ARRAYS
# FOR 1D ARRAY[1 2 3 4] ARE (0 1 2 3)
# FOR 2D ARRAY [[1 2]  rows are 0
#               [1 2]]          1
#   columns are 
#                0 1

# var = np.array([9,8,7,6]) [0 1 2 3] and [-4 -3 -2 -1]
# print(var[1])
# print(var[-3])

# #Output:
# 8
# 8

# var1 = np.array([[9,8,7],[4,5,6]])
# print(var1)
# print(var1.ndim)
# print()
# print(var1[0,2])

# # output:
# [[9 8 7]
#  [4 5 6]]
# 2 #2D ARRAY

# 7 #0 Row, and 2nd column gives 7


# var2 = np.array([[[1,2],[6,7]]])

# print(var2)
# print(var2.ndim)
# print()
# print(var2[0,1,1])

#Output:
# [[[1 2]
#   [6 7]]] 
# 3

# 7

#Array slicing:
#Finding a data set from array using indexing
# [1,2,3,4,5]
# (0,1,2,3,4)

# x[start:stop:step]

# var = np.array([1,2,3,4,5,6,7])
#             #   0,1,2,3,,4,5,6
# print(var)
# print()
# print("2 to 5", var[1:4])
# print("2 to end", var[1:])
# print("start to 5:", var[:5])
# print("stop:", var[1:6:2])

# # Output:
# [1 2 3 4 5 6 7]

# 2 to 5 [2 3 4]
# 2 to end [2 3 4 5 6 7]
# start to 5: [1 2 3 4 5]
# stop: [2 4 6]

# var1 = np.array([[1,2,3,4,5],[9,8,7,6,5],[11,12,13,14,15]])
# print(var1)
# print()
# print("8 to 5:", var1[2,1:])

# # Output:
# [[ 1  2  3  4  5]
#  [ 9  8  7  6  5]
#  [11 12 13 14 15]]

# 8 to 5: [12 13 14 15]






#ITERATION:
#using for loop
# 1D ARRAY
# var = np.array([9,8,7,6,5,4])
# print(var)
# print()
# for i in var:
#     print(i)

# # OUTPUT:
# [9 8 7 6 5 4]

# 9
# 8
# 7
# 6
# 5
# 4

# # 2D ARRAY
# var1 = np.array([[1,2,3,4],[1,2,3,4]])
# print(var1)
# print()
# for j in var1: #prints 1 row at a time then moves n to the next row
#     print(j)

# print()

# for k in var1:
#     for l in k:
#         print(l)

#Output:
# [[1 2 3 4]
#  [1 2 3 4]]

# [1 2 3 4]
# [1 2 3 4]

# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4

# FOR 3D ARRAY:
# var3 = np.array([[[9,8,7,6],[1,2,3,4]]])
# print(var3)
# print(var3.ndim)
# print()

# for i in var3:
#     for j in i:
#         for k in j:
#             print(k)


# #Output:
# [[[9 8 7 6]
#   [1 2 3 4]]]
# 3

# 9
# 8
# 7
# 6
# 1
# 2
# 3
# 4

#USING FUNCTIONS:
#np.nditer
# var3 = np.array([[[9,8,7,6],[1,2,3,4]]])
# print(var3)
# print(var3.ndim)
# print()

# for i in np.nditer(var3):
#     print(i)

# #output:
# [[[9 8 7 6]
#   [1 2 3 4]]]
# 3

# 9
# 8
# 7
# 6
# 1
# 2
# 3
# 4


# #Data with indexes:
# #np.ndenumerate
# var3 = np.array([[[9,8,7,6],[1,2,3,4]]])
# print(var3)
# print(var3.ndim)
# print()

# for i,d in np.ndenumerate(var3):
#     print(i,d)

#Output:
# [[[9 8 7 6]
#   [1 2 3 4]]]
# 3

# (0, 0, 0) 9
# (0, 0, 1) 8
# (0, 0, 2) 7
# (0, 0, 3) 6
# (0, 1, 0) 1
# (0, 1, 1) 2
# (0, 1, 2) 3
# (0, 1, 3) 4



#COPY VS VIEWS FUNCTIONS
# var = np.array([1,2,3,4])
# co = var.copy() #the copy command doesn't reflect the change of value within the array to the copied form of the array
# var[1] = 40
# print("var:", var)
# print("copy", co)

# x = np.array([9,8,7,6,5])
# vi = x.view()#the view command reflects the change of value of within the array to the copied array
# x[1]=40
# print("x:", x)
# print("view:", vi)

# #Output:
# var: [ 1 40  3  4]  
# copy [1 2 3 4]
# x: [ 9 40  7  6  5]
# view: [ 9 40  7  6  5]




#Joining and splitting arrays:

#CONCATENATE FUNCTION
#1D Array
# var = np.array([1,2,3,4])
# var1 = np.array([9,8,7,6])
# ar = np.concatenate((var, var1))
# print(ar)

# #Otput:
# [1 2 3 4 9 8 7 6]

#2D Array:
# vr = np.array([[1,2],[3,4]])
# vr1 = np.array([[9,8],[7,6]])
# ar_new = np.concatenate((vr, vr1),axis=1) #axis=1 rows axis=0 columns
# print(vr)
# print()
# print(vr1)
# print()
# print(ar_new)

#Output: t
# [[1 2]
#  [3 4]]

# [[9 8]
#  [7 6]]

# [[1 2 9 8]  
#  [3 4 7 6]]

# var_1 = np.array([1,2,3,4])
# var_2 = np.array([9,8,7,6])
# a_new = np.stack((var_1, var_2),axis = 1)
# print(a_new)

#STACK FUNCTION:
# stack creates a new function and axis=1 creates rows and axis=0 creates columns
# var_1 = np.array([1,2,3,4])
# var_2 = np.array([9,8,7,6])
# a_new = np.stack((var_1,var_2),axis=1) #both the axis=1 and dstack work the same way
# a_new1 = np.dstack((var_1,var_2)) //height
# a_new2 = np.stack((var_1,var_2),axis=0)
# a_new3 = np.vstack((var_1,var_2)) //column#both the axis=0 and and vstack works the same way
# a_new4 = np.hstack((var_1,var_2)) #row
# print(a_new)
# print(a_new1)
# print(a_new2)
# print(a_new3)
# print(a_new4)

# #Output:
# [[1 9]
#  [2 8]
#  [3 7]
#  [4 6]]
# [[[1 9]
#   [2 8]
#   [3 7]
#   [4 6]]]
# [[1 2 3 4]
#  [9 8 7 6]]
# [[1 2 3 4]
#  [9 8 7 6]]
# [1 2 3 4 9 8 7 6]


#Splitting the array

# var = np.array([1,2,3,4,5,6,7,8])
# print(var)
# ar = np.array_split(var,3) #splits the above array into 3 different stacks of list
# print()
# print(ar)
# print(type(ar))
# print(ar[0])

# #Output:
# # [1 2 3 4 5 6 7 8]

# [array([1, 2, 3]), array([4, 5, 6]), array([7, 8])]
# <class 'list'>
# [1 2 3]

#Splits the 2D array into a list containing 2D arrays and also the vertical axis

# var1 = np.array([[1,2],[3,4],[5,6]])
# print(var1)
# ar1 = np.array_split(var1,3) 
# ar2 = np.array_split(var1,3, axis=1)
# print()
# print(ar1)
# print(ar2)

#Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# [array([[1, 2]]), array([[3, 4]]), array([[5, 6]])]
# [array([[1],
#        [3],
#        [5]]), array([[2],
#        [4],
#        [6]]), array([], shape=(3, 0), dtype=int64)]


#Numpy Functions:
#search, sort, search sorted, filter

#search: search and array for a certain value and reutnr the indexes that get a match
# where Commands
# var = np.array([1,2,3,4,2,5,2,5,6,7])
# #  index       0,1,2,3,4,5,6,7,8,9
# x = np.where( var  == 2)
# print(x)

# var1 = np.array([1,2,3,4,2,5,2,5,6,7])
# #  index       0,1,2,3,4,5,6,7,8,9
# x1 = np.where( (var1/2)  == 0)
# print(x1)

# #Output:
# (array([1, 4, 6]),)
# (array([], dtype=int64),)

# search sorted array:
# Binary search in the array, and returns the index where the specified value would be inserted to maintain the search order
# var2 = np.array([1,2,3,4,6,7,8,9])
# #  index         0,1,2,3,4,5,6,7,8,9
# x2 = np.searchsorted(var2, 5)
# print(x2)

# Output:
# 4

#Note: for it work the array must obe sorted in ascending order and value being searched must be comparable with the arrays elements
#also it can work for diff numerical types suc as intergers and float values but not if the data are mixed such as strings and numbers
#Moves from left to right  by defaults

# var2 = np.array([1,2,3,4,9,10])
# # #  index       0,1,2,3,4,5,6,7,8,9
# x2 = np.searchsorted(var2, [5,6,7], side="right")
# print(x2)
#fins values from right to left

# ouptu
# [4 4 4]


#Sort array: Ordered seq that has been sorted in ordere coressponding to elements ike numeric or alhabetical or ascending or descending
# var2 = np.array([4,2,3,1,12,5,22,52,6,7])
# # # index       0,1,2,3,4,5,6,7,8,9
# print(np.sort(var2))

# # #Output:
# # [ 1  2  3  4  5  6  7 12 22 52]
# #for string values
# var2 = np.array(["a","s","e","d"])
# # # index       0,1,2,3,4,5,6,7,8,9
# print(np.sort(var2))

# # Output:
# ['a' 'd' 'e' 's']

# FILTER ARRAY:
# Getiing elements out of an existing array and creating a new array out of them
# var2 = np.array(["a","s","e","d"])
# # # # index       0,1,2,3,4,
# f =[True,False, False,True]#Only the parts which are indicated as true will be printed)
# new_a = var2[f]
# print(new_a)

# # Output:
# ['a' 'd']



#NUMPY ARRAY FUNCTIONS:
#SHUFFLE: shuffles the data randomly
# var = np.array([1,2,3,4,5])
# np.random.shuffle(var)
# print(var)

# Output:
# [5 2 1 3 4]

#UNIQUE:
# var = np.array([1,2,3,2,4,2,6,2,7])
# x = np.unique(var)
# print(x)

# #Output:
# [1 2 3 4 6 7]

# var = np.array([1,2,3,2,4,2,6,2,7])
# x = np.unique(var,return_index=True,return_counts=True) #Returns the first instance of the use of the characters, there indexes and the no of instances they were used
# print(x)

#Output:
# [1 2 3 4 6 7]

##resize
# var2 = np.array([1,2,3,4,5,6])
# y = np.resize(var2,(3,2))
# print(y)

#Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# var2 = np.array([1,2,3,4,5,6])
# y = np.resize(var2,(3,2))
# print(y)
# print()
# print("Flatten", y.flatten(order="F"))
# print("Ravel:", np.ravel(y,order="A"))#F AND A are file formats by default it would make a list similar to C

# #Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# Flatten [1 3 5 2 4 6]
# Ravel: [1 2 3 4 5 6]



#INSERT FUNCTION
# var = np.array([1,2,3,4])
# print(var)
# v = np.insert(var, (2,4), 6.5) #INSERTS ONLY the interger component
# print(v)

# #Output:
# [1 2 3 4]
# [1 2 6 3 4 6]

# var1 = np.array([[1,2,3],[1,2,3]])
# print(var1)
# print()
# v1 = np.insert(var1, 2, 6, axis=0)#row 2, 6 elements axis 0 cast)
# print(v1)

# Output:
# [[1 2 3]
#  [1 2 3]]

# [[1 2 3]
#  [1 2 3]
#  [6 6 6]]

# var1 = np.array([[1,2,3],[1,2,3]])
# v1 = np.insert(var1, 2, 6, axis =1) #ADDS 6 6 to columns of index=2
# print(v1)

# #Output:
# [[1 2 6 3]
#  [1 2 6 3]]

# var1 = np.array([[1,2,3],[1,2,3]])
# v1 = np.insert(var1, 2,[22,23,24], axis=0) #ROW 2, [22,23,24] ADDITION
# print(v1)

# #Output:
# [[ 1  2  3]
#  [ 1  2  3]
#  [22 23 24]]


# Adding float and other decimal numbers:

# var = np.array([1,2,3,4])
# print(var)
# # v = np.insert(var, (2,4), 6.5) #INSERTS ONLY the integer component
# x=np.append(var,6.5) #USE APPEND FUNCTION
# print(x)

# #Output:
# [1 2 3 4]
# [1.  2.  3.  4.  6.5]

#DELETE 
# var1 = np.array([1,2,3,4])
# print(var1)
# d = np.delete(var1,2)
# print(d)

# # Output:
# [1 2 3 4]
# [1 2 4]

# CONCEPT OF MATRIX NUMPY ARRAY
# var = np.matrix([[1,2],[1,2]])
# var1= np.matrix([[1,2],[1,2]])
# var2= var + var1
# var3 = var*var1
# print(var)
# print(type(var))
# print(var2)
# print()
# print(var3)
# print()

# var = np.array([[1,2,3],[1,2,3]])
# var1= var + var
# var2 = var*var
# print(var)
# print(type(var))
# print(var1)
# print(var2)
# # Output:
# [[2 4]
#  [2 4]]

# [[3 6]
#  [3 6]] MATRIX MULTIPLICATION WORKS AS PER REGULAR MATRIX MULTIPLICATION

# [[1 2 3]
#  [1 2 3]]
# <class 'numpy.ndarray'>
# [[2 4 6]
#  [2 4 6]]

# [[1 4 9]
#  [1 4 9]]ARRAY MULTIPLICATION MULTIPLIES THE VALUES IN THE RESPECTIVE INDEXES EQUIVALENT


#TRANSPOSE OF A MATRIX
# var = np.matrix([[1,2,3],[4,5,6]])
# print(var)
# print()
# print(np.transpose(var))
# print()
# print(var.T)
# print()
# print(np.swapaxes(var,0,1))

# #oUTPUT:
# [[1 2 3]
#  [4 5 6]]

# [[1 4]
#  [2 5]
#  [3 6]]

# [[1 4]
#  [2 5]
#  [3 6]]

# [[1 4]
#  [2 5]
#  [3 6]]


#INVERSE OF A MATRIX
# var3 = np.matrix([[1,2],[3,4]])
# print(var3)
# print()
# print(np.linalg.inv(var3))

# #INVERSE OF A MATRIX(LOGIC)
# # FOR [1 2] INVERSE WILL BE = 1/(4-6)[4 -2
# #     [3 4]                          -3 1]

# # ANSWER:
# [[1 2]
#  [3 4]]

# [[-2.   1. ]
#  [ 1.5 -0.5]]

#POWER OF A MATRIX
#np.linalg.matrix_power(var4,2)
# var4 = np.matrix([[1,2],[3,4]])
# print(var4)
# print()
# print(np.linalg.matrix_power(var4,2))
# print()
# print(np.linalg.matrix_power(var4,-2)) #MULTIPLICATION WITH THE INVERSE OF A MATRIX

# #OUTPUT:
# [[1 2]
#  [3 4]]

# [[ 7 10]
#  [15 22]]

# [[ 5.5  -2.5 ]
#  [-3.75  1.75]]


# A=[a b c   |A|=a[ei-hf]-b[di-gf]+c[dh-eg]
 #   d e f = 
#    g h i]
# np.linalg.det(var)

# var5 = np.matrix([[1,2,3],[3,4,3],[1,2,3]])
# print(var5)
# print()
# print(np.linalg.det(var5))

# #Output:
# [[1 2 3]
#  [3 4 3]
#  [1 2 3]]

# 0.0


