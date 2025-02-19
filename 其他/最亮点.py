import cv2
import numpy as np


image = cv2.imread('300.bmp', 0)


all_pixel_values = image.flatten()

# 找到最亮点的像素值和坐标
max_value = np.max(image)
max_index = np.unravel_index(np.argmax(image), image.shape)

print("所有像素值:", all_pixel_values)
print("最亮点的像素值:", max_value)
print("最亮点的坐标:", max_index)

# 在图像上标记出最亮点（可选）
result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.circle(result_image, max_index[::-1], 5, (0, 0, 255), -1)
cv2.imshow('Image with brightest point', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()