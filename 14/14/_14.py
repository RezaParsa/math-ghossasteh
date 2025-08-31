# ماتریس مجاورت گراف کوچک‌تر (G1)
while True:
    try:
        n_a = int(input("pls enter matrix A size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

g1 = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                g1.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")


# ماتریس مجاورت گراف بزرگ‌تر (G2)
while True:
    try:
        n_a = int(input("pls enter matrix A size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

g2 = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                g2.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")


# پیدا کردن تعداد نقاط در هر دو گراف
n1 = len(g1)
n2 = len(g2)

# بررسی شرط اول: آیا تعداد نقاط G1 کمتر یا مساوی G2 است؟
if n1 > n2:
    print("G1 زیرگراف G2 نیست، زیرا تعداد نقاط G1 بیشتر است.")
    exit()

# بررسی شرط دوم: آیا تمام یال‌های G1 در G2 وجود دارند؟
is_subgraph = True
for x in range(n1):
    for y in range(n1):
        # اگر در G1 یک یال وجود داشت (مقدار 1 بود)
        if g1[x][y] == 1:
            # بررسی می‌کنیم که آیا در G2 هم در همان خانه، یال وجود دارد؟
            if g2[x][y] == 0:
                is_subgraph = False
                break
    if not is_subgraph:
        break

# چاپ نتیجه نهایی
if is_subgraph:
    print("G1  is subgraph G2 .")
else:
    print("G1 is not subgraph G2 .")
