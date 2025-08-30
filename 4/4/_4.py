

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



# پیدا کردن ابعاد ماتریس‌ها
rows_a = len(matrix_a)
cols_a = len(matrix_a[0])
rows_b = len(matrix_b)
cols_b = len(matrix_b[0])

# بررسی اینکه آیا ضرب بولی امکان‌پذیر است؟
if cols_a == rows_b:
  print("zarbboly is possible.")
  
  # یک جدول خالی برای نتیجه ضرب می‌سازیم
  result = []
  
  # حالا شروع می‌کنیم به ضرب
  for x in range(rows_a):
    # یک سطر جدید برای نتیجه
    new_row = []
    for y in range(cols_b):
      # مقدار هر خانه را با یک متغیر موقت شروع می‌کنیم
      cell_value = 0
      for z in range(cols_a):
        # این جا جادوی ضرب بولی اتفاق می‌افتد
        # a[x][z] AND b[z][y]
        # سپس با OR جمع می‌کنیم
        cell_value = cell_value or (matrix_a[x][z] and matrix_b[z][y])
      
      new_row.append(cell_value)
    
    result.append(new_row)
  
  # نتیجه نهایی را چاپ می‌کنیم
  print("result of zarbboly:")
  for row in result:
    print(row)

else:
  print("zarbboly is not possible . firstmatrix colums count is not equal with secendmatrix rows count")