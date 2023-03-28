import numpy as np

# 第一組數據
arr1 = [["2000-01-04","30.6020"],["2000-01-05","30.8000"]]

# 第二組數據
arr2 = [["2000-01-04","30.6020"],["2000-01-05","30.8000"]]

arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

# Get unique dates from both arrays
dates1 = set(arr1_np[:, 0])
dates2 = set(arr2_np[:, 0])

# Find intersection of dates
common_dates = list(dates1.intersection(dates2))

# Filter arrays to only include common dates
filtered_arr1 = np.array([row for row in arr1_np if row[0] in common_dates])
filtered_arr2 = np.array([row for row in arr2_np if row[0] in common_dates])

# 將數值部分轉換為 float
values1 = filtered_arr1[:, 1].astype(float)
values2 = filtered_arr2[:, 1].astype(float)


# values1 = arr1_np[:, 1].astype(np.float64)
# values2 = arr2_np[:, 1].astype(np.float64)

# 打印 values1 和 values2 的形状
print(values1.shape)
print(values2.shape)

# 計算相關係數
corr = np.corrcoef(values1, values2)[0, 1]

print("相關係數：", corr)