# ماتریس مجاورت (همسایگی)
# اگر از A به B راهی هست، خانه [0, 1] برابر با 1 است
adj_matrix = [
    [0, 1, 1, 0],  # از A به B و C راه داریم
    [1, 0, 0, 1],  # از B به A و D راه داریم
    [1, 0, 0, 1],  # از C به A و D راه داریم
    [0, 1, 1, 0]   # از D به B و C راه داریم
]

# ماتریس وزن (فاصله بین نقاط)
# فاصله از A به B برابر 5 و از A به C برابر 2 است
weight_matrix = [
    [0, 5, 2, 0],
    [5, 0, 0, 3],
    [2, 0, 0, 4],
    [0, 3, 4, 0]
]

# مسیر مورد نظر ما
# مسیر از A به C و سپس به D است
# نام نقاط را به سادگی به A, B, C, D تبدیل می‌کنیم
path = ['A', 'C', 'D']

# حالا یک جعبه برای نگهداری طول کل مسیر می‌سازیم
total_length = 0
found_path = True  # یک پرچم (چراغ) که نشان می‌دهد آیا مسیر معتبر است یا نه

# برای راحتی کار، نام نقاط را به شماره تبدیل می‌کنیم
points = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

# از اولین نقطه مسیر تا یکی مانده به آخر پیش می‌رویم
for i in range(len(path) - 1):
    start_node_name = path[i]
    end_node_name = path[i+1]
    
    # شماره نقاط را از دیکشنری پیدا می‌کنیم
    start_index = points[start_node_name]
    end_index = points[end_node_name]
    
    # بررسی می‌کنیم که آیا بین این دو نقطه راهی وجود دارد؟
    if adj_matrix[start_index][end_index] == 1:
        # اگر راهی وجود داشت، طول آن را به طول کل مسیر اضافه می‌کنیم
        edge_weight = weight_matrix[start_index][end_index]
        total_length += edge_weight
    else:
        # اگر راهی وجود نداشت، پیامی نمایش می‌دهیم و از برنامه خارج می‌شویم
        print(f"No path from {start_node_name} to {end_node_name} .")
        found_path = False
        break

# اگر تمام مسیر معتبر بود، طول کل را چاپ می‌کنیم
if found_path:
    print(f"Total length of the route {path}: {total_length}")
