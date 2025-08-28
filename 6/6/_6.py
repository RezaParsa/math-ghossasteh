# یک جدول جادویی (ماتریس) آماده می‌کنیم.
# این ماتریس باید مربعی باشد.
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# پیدا کردن ابعاد ماتریس
n = len(matrix)

# بررسی خاصیت تقارن
is_symmetric = True
for x in range(n):
    for y in range(n):
        if matrix[x][y] != matrix[y][x]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("this matrix is Taghrony")
else:
    print("this matrix is not Taghrony.")

# ---

# بررسی خاصیت پادتقارن
is_antisymmetric = True
for x in range(n):
    for y in range(n):
        # خانه‌های روی قطر اصلی را نادیده می‌گیریم (جایی که x == y)
        if x != y and matrix[x][y] == 1 and matrix[y][x] == 1:
            is_antisymmetric = False
            break
    if not is_antisymmetric:
        break

if is_antisymmetric:
    print(" this matrix is Padtaghrony .")
else:
    print("this matrix in not Padtaghrony .")

# ---

# بررسی خاصیت تراگذری (ترایایی)
# برای این کار، اول باید ضرب بولی ماتریس در خودش را انجام دهیم (R²)
def boolean_multiply(m1, m2):
    size = len(m1)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = result[i][j] or (m1[i][k] and m2[k][j])
    return result

# R² = R * R
r_squared = boolean_multiply(matrix, matrix)

# حالا بررسی می‌کنیم که آیا R² زیرمجموعه‌ای از R است؟
# یعنی هرجایی که در R² عدد 1 هست، در R هم باید عدد 1 باشد.
is_transitive = True
for x in range(n):
    for y in range(n):
        if r_squared[x][y] == 1 and matrix[x][y] == 0:
            is_transitive = False
            break
    if not is_transitive:
        break

if is_transitive:
    print("‌this matrix has Trayae.")
else:
    print("this matrix doesnt has Trayae.")
