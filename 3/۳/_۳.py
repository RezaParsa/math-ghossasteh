
# ماتریس بولی اول ما
# در جبر بولی، 1 به معنی "درست" و 0 به معنی "نادرست" است.
a = [[0, 1, 0],
     [1, 0, 1]]

# ماتریس بولی دوم ما
b = [[1, 1, 0],
     [0, 1, 0],
     [1, 0, 1]]

# اینجا ابعاد هر دو ماتریس را پیدا می‌کنیم
rows_a = len(a)
cols_a = len(a[0])
rows_b = len(b)
cols_b = len(b[0])

# حالا بررسی می‌کنیم که آیا وست (join) قابل محاسبه است؟
# وست فقط وقتی ممکن است که تعداد سطرها و ستون‌های هر دو ماتریس با هم برابر باشد.
if rows_a == rows_b and cols_a == cols_b:
    print("وست (join) قابل محاسبه است.")
    # حالا وست را حساب می‌کنیم
    join_result = []
    for x in range(rows_a):
        new_row = []
        for y in range(cols_a):
            # وست با استفاده از 'یا' منطقی (or) انجام می‌شود
            result = a[x][y] or b[x][y]
            new_row.append(result)
        join_result.append(new_row)
    
    print("vest result (join):")
    for row in join_result:
        print(row)
else:
    print("(join) cannot calculat join cause matrix sizes are not in same size.")

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
                result = result or (a[x][z] and b[z][y])
            new_row.append(result)
        meet_result.append(new_row)
    
    print("result of (meet):")
    for row in meet_result:
        print(row)
else:
    print(" (meet) Rasand is not calculatable cause numbers colums of firstmatrix is not same as secondmatrix row.")