import cv2
import numpy as np

# 读取图像
img = cv2.imread('300.bmp')

# 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用阈值进行二值化
_, binary = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

# 获取图像尺寸
height, width = binary.shape

# 创建一个数组来存储每列的上边界点
top_boundary = []

# 跳过左侧部分列的数量
skip_columns = 100

# 对每一列进行处理
for x in range(skip_columns, width):

    column = binary[:, x]

    # 从上往下找到第一个白色像素点的位置
    white_pixels = np.where(column == 255)[0]
    
    if len(white_pixels) > 0:
        # 如果存在白色像素，取最上面的一个
        top_y = white_pixels[0]
        top_boundary.append((x, top_y))


# 平滑处理
window_size = 5
smoothed_boundary = []
for i in range(len(top_boundary)):
    if i < window_size // 2 or i >= len(top_boundary) - window_size // 2:
        smoothed_boundary.append(top_boundary[i])
    else:
        avg_y = np.mean([top_boundary[j][1] for j in range(i - window_size // 2, i + window_size // 2 + 1)])
        smoothed_boundary.append((top_boundary[i][0], int(avg_y)))

# 找到拐点
def calculate_slope(points):
    slopes = []
    for i in range(1, len(points)):
        dx = points[i][0] - points[i-1][0]
        dy = points[i][1] - points[i-1][1]
        if dx != 0:
            slopes.append(dy / dx)
        else:
            slopes.append(0)
    return slopes

k = 10  
max_slope_diff = 0
turning_point = None

for i in range(k, len(smoothed_boundary) - k):
    left_slopes = calculate_slope(smoothed_boundary[i - k:i])
    right_slopes = calculate_slope(smoothed_boundary[i:i + k])
    left_avg_slope = np.mean(left_slopes)
    right_avg_slope = np.mean(right_slopes)
    slope_diff = abs(left_avg_slope - right_avg_slope)
    if slope_diff > max_slope_diff:
        max_slope_diff = slope_diff
        turning_point = smoothed_boundary[i]

# 在原图上绘制边界和拐点
img_with_boundary = img.copy()
for point in smoothed_boundary:
    x, y = point
    cv2.circle(img_with_boundary, (x, y), 1, (0, 0, 255), -1)

if turning_point:
    cv2.circle(img_with_boundary, turning_point, 5, (0, 255, 0), -1)

# 找出灰度图中白色区域的中心点
white_pixels = np.where(gray == 255)
if len(white_pixels[0]) > 0:
    center_y = int(np.mean(white_pixels[0]))
    center_x = int(np.mean(white_pixels[1]))
    closest_point = (center_x, center_y)
else:
    closest_point = None

if closest_point:
    # 在原图上绘制白色区域的中心点
    cv2.circle(img_with_boundary, closest_point, 5, (255, 0, 0), -1)

    if turning_point:
        # 计算拐点相对于原点坐标
        relative_x = turning_point[0] - closest_point[0]
        relative_y = turning_point[1] - closest_point[1]
        print(f"拐点相对于原点坐标: ({relative_x}, {relative_y})")

# 显示结果
cv2.imshow('result', img_with_boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存
cv2.imwrite('result.bmp', img_with_boundary)