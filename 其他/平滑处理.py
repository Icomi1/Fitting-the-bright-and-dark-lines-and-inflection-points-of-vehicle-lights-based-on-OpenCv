import numpy as np

# 模拟原始边界点列表
top_boundary = [(1, 10), (2, 12), (3, 15), (4, 13), (5, 16)]
window_size = 5
smoothed_boundary = []

# 假设当前处理第2个点（索引i = 2）
i = 2
avg_y = np.mean([top_boundary[j][1] for j in range(i - window_size // 2, i + window_size // 2 + 1)])
smoothed_boundary.append((top_boundary[i][0], int(avg_y)))

print("原始点:", top_boundary[i])
print("平滑后的点:", smoothed_boundary[-1])