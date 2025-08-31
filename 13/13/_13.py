# ماتریس مجاورت یک گراف را تعریف می‌کنیم.
# این ماتریس باید مربعی باشد.
# 1 یعنی راه دارد، 0 یعنی راه ندارد.
while True:
    try:
        n_a = int(input("pls enter matrix A size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

adj_matrix = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                adj_matrix.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")


# تعداد سطرها و ستون‌های ماتریس را پیدا می‌کنیم
n = len(adj_matrix)

# یک ماتریس خالی به نام "متمم" می‌سازیم
complement_matrix = []

# حالا سطر به سطر ماتریس اصلی را بررسی می‌کنیم
for x in range(n):
    # یک سطر جدید برای ماتریس متمم
    new_row = []
    for y in range(n):
        # اگر سطر و ستون برابر بود (روی قطر اصلی)...
        if x == y:
            # همان مقدار قبلی را نگه می‌داریم
            new_row.append(adj_matrix[x][y])
        else:
            # اگر 1 بود، 0 می‌شود و اگر 0 بود، 1 می‌شود
            if adj_matrix[x][y] == 1:
                new_row.append(0)
            else:
                new_row.append(1)
    # سطر جدید را به ماتریس متمم اضافه می‌کنیم
    complement_matrix.append(new_row)

# چاپ ماتریس اصلی و ماتریس متمم
print("Main matrix:")
for row in adj_matrix:
    print(row)

print("\n---")

print("Matrix motamam:")
for row in complement_matrix:
    print(row)
