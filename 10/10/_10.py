
# ماتریس متناظر با رابطه R
# این ماتریس باید مربعی باشد.
r_matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

# ماتریس متناظر با رابطه S
# تعداد ستون‌های این ماتریس باید با تعداد سطرهای ماتریس R برابر باشد.
s_matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

# پیدا کردن ابعاد ماتریس‌ها
rows_r = len(r_matrix)
cols_r = len(r_matrix[0])
rows_s = len(s_matrix)
cols_s = len(s_matrix[0])

# بررسی امکان ترکیب (ضرب بولی)
# تعداد ستون‌های S باید با تعداد سطرهای R برابر باشد.
if cols_s != rows_r:
    print("there is no RoS  ,size of ur matrix in not suit.")
    exit()

# یک ماتریس خالی برای نتیجه (RoS) می‌سازیم
ros_matrix = []

# حالا ترکیب را انجام می‌دهیم (مانند ضرب بولی)
for x in range(rows_r):
    new_row = []
    for y in range(cols_s):
        cell_value = 0
        for z in range(cols_r):
            # اگر در S از z به y و در R از x به z راهی بود
            # پس در RoS از x به y راهی هست.
            if s_matrix[z][y] == 1 and r_matrix[x][z] == 1:
                cell_value = 1
                break # اگر 1 پیدا شد، نیاز به ادامه نیست
        new_row.append(cell_value)
    ros_matrix.append(new_row)

# چاپ ماتریس RoS
print("Matrix RoS:")
for row in ros_matrix:
    print(row)