
# ماتریس متناظر با رابطه R
# این ماتریس باید مربعی باشد.
while True:
    try:
        n_a = int(input("pls enter matrix R size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

r_matrix = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                r_matrix.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")


#take S_Matrix 
while True:
    try:
        n_a = int(input("pls enter matrix S size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

s_matrix = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                s_matrix.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")

# ماتریس متناظر با رابطه S
# تعداد ستون‌های این ماتریس باید با تعداد سطرهای ماتریس R برابر باشد.

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