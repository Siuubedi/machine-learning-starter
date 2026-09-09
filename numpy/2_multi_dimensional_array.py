import numpy as np

# 2D Array
array2 = np.array([[1, 2, 3, 4], ["A", "B", "C", "D"]])
print(array2)

# 3D Array
array3 = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
])
print(array3)
print(array3.ndim)
print("Shape", array3.shape)

# Multi Dimensional Array
arraym = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
    [[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]]
])
print("Multi", arraym.ndim)

# Printing the array elements
print("Printing the array elements:")
print("First", arraym[0][0][0])

# If i want to print "17"
print("This will print 17:", arraym[1][1][0])
print("This will print 32:", arraym[2][1][3])

# Let's form a word
array = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
])

#AMIGO
word = array[0,0,0]+array[1,1,0]+array[0,2,2]+array[0,2,0]+array[1,1,2]
print(word)
