# این ماتریس باید مربعی باشد.

while True:
    try:
        n_a = int(input("pls enter matrix_a A size: "))
        break
    except ValueError:
        print("error : matrix_a size must be posetive num.")

matrix_a = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                matrix_a.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix_a  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")


# پیدا کردن ابعاد ماتریس
n = len(matrix_a)

# بررسی خاصیت تقارن
is_symmetric = True
for x in range(n):
    for y in range(n):
        if matrix_a[x][y] != matrix_a[y][x]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("this matrix_a is Taghrony")
else:
    print("this matrix_a is not Taghrony.")

# ---

# بررسی خاصیت پادتقارن
is_antisymmetric = True
for x in range(n):
    for y in range(n):
        # خانه‌های روی قطر اصلی را نادیده می‌گیریم (جایی که x == y)
        if x != y and matrix_a[x][y] == 1 and matrix_a[y][x] == 1:
            is_antisymmetric = False
            break
    if not is_antisymmetric:
        break

if is_antisymmetric:
    print(" this matrix_a is Padtaghrony .")
else:
    print("this matrix_a in not Padtaghrony .")

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
r_squared = boolean_multiply(matrix_a, matrix_a)

# حالا بررسی می‌کنیم که آیا R² زیرمجموعه‌ای از R است؟
# یعنی هرجایی که در R² عدد 1 هست، در R هم باید عدد 1 باشد.
is_transitive = True
for x in range(n):
    for y in range(n):
        if r_squared[x][y] == 1 and matrix_a[x][y] == 0:
            is_transitive = False
            break
    if not is_transitive:
        break

if is_transitive:
    print("‌this matrix_a_a has Trayae.")
else:
    print("this matrix_a_a doesnt has Trayae.")
