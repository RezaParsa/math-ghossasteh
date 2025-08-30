
# ماتریس بولی اول ما
# در جبر بولی، 1 به معنی "درست" و 0 به معنی "نادرست" است.

# --- دریافت ماتریس اول (A) ---

while True:
    try:
        n_a = int(input("pls enter matrix A size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

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
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")

print("first matrix done")

# --- دریافت ماتریس دوم (B) ---
print("\n--------------------------")

while True:
    try:
        n_b = int(input("pls enter matrix B size: "))
        break
    except ValueError:
        print("erroe matrix size must be in podetive nums.")

matrix_b = []
print(f"pls {n_b} row of nub must enter with space:")

for i in range(n_b):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_b:
                matrix_b.append(row)
                break
            else:
                print(f"error: count of this row  ({len(row)}) with matrix size ({n_b}) is not suit pls enter it again.")
        except ValueError:
            print("error: pls enter num just with space.")

print("secndry matrix done.")



rows_a = len(matrix_a)
cols_a = len(matrix_a[0])
rows_b = len(matrix_b)
cols_b = len(matrix_b[0])


# حالا بررسی می‌کنیم که آیا وست (join) قابل محاسبه است؟
# وست فقط وقتی ممکن است که تعداد سطرها و ستون‌های هر دو ماتریس با هم برابر باشد.
if rows_a == rows_b and cols_a == cols_b:
    print(" (join) is calcualtable.")
    # حالا وست را حساب می‌کنیم
    join_result = []
    for x in range(rows_a):
        new_row = []
        for y in range(cols_a):
            # وست با استفاده از 'یا' منطقی (or) انجام می‌شود
            result = matrix_a[x][y] or matrix_b[x][y]
            new_row.append(result)
        join_result.append(new_row)
    
    print("vest result (join):")
    for row in join_result:
        print(row)
else:
    print("(join) cannot calculat join cause matrix sizes are not in suit size.")

print("-------------------")

# حالا بررسی می‌کنیم که آیا رسند (meet) قابل محاسبه است؟
# رسند فقط وقتی ممکن است که تعداد ستون‌های ماتریس اول با تعداد سطرهای ماتریس دوم برابر باشد.
if cols_a == rows_b:
    print("(meet)rsand is calculateable.")
    # حالا رسند را حساب می‌کنیم
    meet_result = []
    for x in range(rows_a):
        new_row = []
        for y in range(cols_b):
            # اینجا هر سطر از ماتریس اول را با هر ستون از ماتریس دوم ترکیب می‌کنیم
            result = 0
            for z in range(cols_a):
                # از 'و' منطقی (and) و 'یا' منطقی (or) استفاده می‌کنیم
                # این کار مثل ضرب و جمع در جبر معمولی است
                result = result or (matrix_a[x][z] and matrix_b[z][y])
            new_row.append(result)
        meet_result.append(new_row)
    
    print("result of (meet):")
    for row in meet_result:
        print(row)
else:
    print(" (meet) Rasand is not calculatable cause numbers colums of firstmatrix is not same as secondmatrix row.")