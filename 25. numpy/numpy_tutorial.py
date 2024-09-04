"""
    NumPy is a Python library.
    NumPy is used for working with arrays.
    NumPy is short for "Numerical Python".
    It has has functions for working in domain of linear algebra, fourier transform, and matrices.
    It is up to 50x faster than traditional Python lists. It stored in memory.

    # NumPy DataType
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
"""

import numpy as np

print(f"numpy version: {np.__version__}")

# array object is called ndarray and created by using array() function.
# 0-D arrays
zero_d_array = np.array(42)
print(f"0-D array: {zero_d_array}")

# 1-D arrays
# We can pass a list, tuple or any array-like object.
one_d_array = np.array([1, 2, 3, 4, 5])
print(f"1-D arrays: {one_d_array}")

# 2-D arrays
# An array that has 1-D arrays as its elements.
# NumPy has a whole sub module dedicated towards
# matrix operations called numpy.mat
two_d_arrays = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2-D arrays: {two_d_arrays}")

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements.
three_d_arrays = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"3-D arrays: {three_d_arrays}")

# ndim attribute returns an integer that tells us how many dimensions the array have.
print(f"zero_d_array has {zero_d_array.ndim} dimensions")
print(f"one_d_array has {one_d_array.ndim} dimensions")
print(f"two_d_arrays has {two_d_arrays.ndim} dimensions")
print(f"three_d_arrays has {three_d_arrays.ndim} dimensions")

# Create an array with 5 dimensions and verify that it has 5 dimensions
five_d_arrays = np.array([1, 2, 3, 4, 5], ndmin=5)
print(f"five_d_arrays: {five_d_arrays} has {five_d_arrays.ndim} dimensions")

# negative indexing
neg_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"Print the last element from the 2nd dimension: {neg_array[1,-1]}")

############################################################
# Data Types
############################################################
# dytpe() function return Data type of the array
print(f"zero_d_arrays datatype: {zero_d_array.dtype}")

# <U6 datatype represents a Unicode string of fixed size.
# The U stands for Unicode, and the number 6 indicates the
# maximum length of the string in characters. So, <U6 can
# store any Unicode string that is up to 6 characters long
string_array = np.array(["apple", "banana", "cherry", "watermelon"])
print(f"string_array datatype: {string_array.dtype}")

# Creating arrays with a defined data type
string_data_type_array = np.array([1, 2, 3, 4], dtype="S")
print(f"defined array type to String: {string_data_type_array.dtype}")

# Create an array with data type 4 bytes integer:
int_data_type_array = np.array([1, 2, 3, 4], dtype="i4")
print(f"defined array type to String: {int_data_type_array.dtype}")

# astype() function creates a copy of the array,
# and allows you to specify the data type as a parameter.
float_array = np.array([1.1, 2.1, 3.1])
to_int_array = float_array.astype("i")
print(f"float_array: {float_array} converted to int_array {to_int_array}")
print(f"int_array datatype: {to_int_array.dtype}")

# convert integer array to boolean
int_array = np.array([1, 0, 3])
to_bool_array = int_array.astype(bool)
print(f"int_array: {int_array} converted to int_array {to_bool_array}")
print(f"to_bool_array datatype: {to_bool_array.dtype}")

############################################################
# Copy vs View
############################################################
# copy owns the data and any changes made to the copy will not affect original array
orig_arr = np.array([1, 2, 3, 4, 5])
copy_arr = orig_arr.copy()
orig_arr[0] = 42
print(f"Updated original array: {orig_arr}")
print(f"copied array: {copy_arr}")

# view does not own the data and any changes made to the view will affect the original array
view_arr = orig_arr.view()
print(f"view array: {view_arr}")
view_arr[0] = 32
print(f"Updated view array: {view_arr}")
print(f"original array: {orig_arr}")

# Check if Array Owns its Data
# attribute base that returns None if the array owns the data.
print(f"Is copy_arr owns its data? {copy_arr.base}")
print(f"Is view_arr owns its data? {view_arr.base}")

############################################################
# Array Shape
############################################################
# attribute shape returns a tuple with each index having
# the number of corresponding element
shape_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(
    f"shape of the array {shape_arr}: {shape_arr.shape} has 2 dimensions where the first dimension has 2 elements and the second dimension has 4 elements"
)

############################################################
# Reshaping arrays
############################################################
# Reshaping means changing the shape of an array.
# we can add or remove dimensions or change number of
# elements in each dimension.
current_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshape_arr = current_arr.reshape(4, 3)
print(f"current_arr is reshaped to {reshape_arr}")
# reshape from 1-D array to 3-D array
reshape_to_3D_arr = current_arr.reshape(2, 3, 2)
print(f"current_arr is reshaped to {reshape_to_3D_arr}")

# Check if the returned array is a copy or view
# if it returns the original way, it is a view
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f"is an array copy or view? {arr.reshape(2,4).base}")

# "unknown" dimension
# do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# Covert 1D array with 8 elements to 3D array with 2x2 elements
newarr = arr.reshape(2, 2, -1)
print(f"Covert 1D array with 8 elements to 3D array with 2x2 elements: {newarr}")

# Flattening the arrays
# converting a multidimensional array into a 1D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(f"converting a multidimensional array into a 1D array: {newarr}")

############################################################
# Array Iterating
############################################################
# function nditer() can be used from very basic to very advanced iterations.
iteration_arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("iteration using nditer()")
for x in np.nditer(iteration_arr):
    print(x)

print("iteration using for regular loop")
for first_dim in iteration_arr:
    for second_dim in first_dim:
        for third_dim in second_dim:
            print(third_dim)

print("iteration Array With Different Data Types")
# Iterating Array With Different Data Types
# use op_dtypes argument and pass it the expected
# datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place
# (where the element is in array) so it needs some other space
# to perform this action, that extra space is called buffer,
# and in order to enable it in nditer() we pass flags=['buffered'].
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x)


print("Iterating With Different Step Size")
# Iterating With Different Step Size
# Iterate through every scalar element of the 2D array skipping 1 element.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)

print("Enumerated Iteration Using ndenumerate()")
# corresponding index of the element while iterating
print("Enumerate on 1D array's elements")
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

print("Enumerate on 2D array's elements")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


############################################################
# Joining Array
############################################################
# We pass a sequence of arrays that we want to join to the concatenate()
# function, along with the axis. If axis is not explicitly passed, it is taken as 0.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_concat = np.concatenate((arr1, arr2))
print(f"concatentate arr1 and arr2 with default axis (0): {arr_concat}")

# Join two 2-D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr_concat = np.concatenate((arr1, arr2), axis=1)
print(f"concatentate arr1 and arr2 with axis = 1: {arr_concat}")
