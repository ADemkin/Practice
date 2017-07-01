#!/usr/bin/env python3
# coding: utf-8
#

doubled = [i * 2 for i in range(12)]

# print(doubled) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

tri = [i for i in range(50) if i % 3 == 0]

# print(tri) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

odds = [i for i in range(30) if i % 2 == 1]

# print(odds) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

multiple = [[i, i**2, i**3] for i in range(5)]

# print(multiple) # [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64]]

'''
[[0, 0, 0],
 [1, 1, 1],
 [2, 4, 8],
 [3, 9, 27],
 [4, 16, 64]]

'''

# flattened = []
# for row in multiple:
#     for i in row:
#         flattened.append(i)
#
# print(flattened)

flattened = [i for row in multiple for i in row]

# print(flattened) # [0, 0, 0, 1, 1, 1, 2, 4, 8, 3, 9, 27, 4, 16, 64]

no_doubles = [i for i in range(len(flattened)) if flattened[i] != flattened[i - 1]]

# print(no_doubles)

codes = {i: chr(i) for i in range(65,91)}

print(codes)

# flipped = {}
# for key, value in codes:
#     flipped[value] = key
#
# print(flipped)