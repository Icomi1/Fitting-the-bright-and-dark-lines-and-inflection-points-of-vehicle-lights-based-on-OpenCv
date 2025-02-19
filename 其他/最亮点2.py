import cv2
import numpy as np


image = cv2.imread('300.bmp')


image_float = image.astype(float)

# R: 0.299, G: 0.587, B: 0.114
brightness = 0.299 * image_float[:, :, 0] + 0.587 * image_float[:, :, 1] + 0.114 * image_float[:, :, 2]

all_brightness_values = brightness.flatten()

max_brightness = np.max(brightness)
max_index = np.unravel_index(np.argmax(brightness), brightness.shape)

print("所有像素的亮度值:", all_brightness_values)
print("最亮点的亮度值:", max_brightness)
print("最亮点的坐标:", max_index)


cv2.circle(image, max_index[::-1], 5, (0, 0, 255), -1)

cv2.imshow('Image with brightest point', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
