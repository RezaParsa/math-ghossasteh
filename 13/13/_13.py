# ماتریس مجاورت یک گراف را تعریف می‌کنیم.
# این ماتریس باید مربعی باشد.
# 1 یعنی راه دارد، 0 یعنی راه ندارد.
adj_matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

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
