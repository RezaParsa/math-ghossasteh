# یک جدول جادویی (ماتریس) آماده می‌کنیم.
# این ماتریس باید مربعی باشد (تعداد سطر و ستون یکسان).
m = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

# از شما می‌خواهیم بگویید چند بار این کار را تکرار کنیم
try:
    n = int(input("pls enter a number for 'n': "))
except ValueError:
    print("pls enter just numbers.")
    exit()

# اگر n صفر یا منفی بود، هیچ کاری نمی‌کنیم
if n <= 0:
    print("n must be + number.")
    exit()

# حالا یک تابع جادویی برای ضرب بولی می‌سازیم
def boolean_multiply(matrix1, matrix2):
    # اول ابعاد را پیدا می‌کنیم
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # بررسی می‌کنیم که ضرب امکان پذیر است یا نه
    if cols1 != rows2:
        print("size in not fit for multiply!")
        return None

    # یک جدول خالی برای نتیجه می‌سازیم
    result_matrix = []
    
    # حالا ضرب را انجام می‌دهیم
    for x in range(rows1):
        new_row = []
        for y in range(cols2):
            cell_value = 0
            for z in range(cols1):
                cell_value = cell_value or (matrix1[x][z] and matrix2[z][y])
            new_row.append(cell_value)
        result_matrix.append(new_row)
    
    return result_matrix

# اگر n برابر 1 بود، همان ماتریس اولی را نشان می‌دهیم
if n == 1:
    print(f"result to powers of R {n}:")
    for row in m:
        print(row)
else:
    # یک کپی از ماتریس اصلی برای شروع کار می‌سازیم
    result = m
    # حالا n-1 بار ضرب را تکرار می‌کنیم
    for i in range(n - 1):
        result = boolean_multiply(result, m)

    # و در نهایت، نتیجه نهایی را چاپ می‌کنیم
    print(f"result to powers of R {n}:")
    for row in result:
        print(row)
