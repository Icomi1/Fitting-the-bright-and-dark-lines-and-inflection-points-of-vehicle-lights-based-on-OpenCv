import cv2
import numpy as np

# 读取图像并转换为灰度图
img = cv2.imread('300.bmp', 0)

# 不使用 _
ret, binary_with_ret = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
print("实际使用的阈值:", ret)

# 使用 _
_, binary_with_underscore = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)

# 显示二值化后的图像
cv2.imshow('Binary Image with _', binary_with_underscore)
cv2.waitKey(0)
cv2.destroyAllWindows()