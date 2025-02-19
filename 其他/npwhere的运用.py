import numpy as np


column = np.array([0,0,255,255,0])

print(column == 255)
'''
不加[0]，返回的是这种形式
(array([2, 3], dtype=int64),)
'''
white_pixels = np.where(column == 255)[0]
print(white_pixels)