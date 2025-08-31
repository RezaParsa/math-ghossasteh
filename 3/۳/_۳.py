# تابع برای دریافت و ساخت یک ماتریس مربعی
def create_matrix(matrix_name, size, is_adjacency=False):
    """
    این تابع از کاربر یک ماتریس مربعی می‌گیرد و آن را اعتبارسنجی می‌کند.
    """
    matrix = []
    print(f"لطفا {size} سطر با {size} عدد در هر سطر وارد کنید. اعداد را با فاصله از هم جدا کنید:")

    for i in range(size):
        while True:
            try:
                row_str = input(f"سطر {i+1}: ")
                row = [int(x) for x in row_str.split()]
                
                if is_adjacency:
                    is_valid_binary = all(num in [0, 1] for num in row)
                    if not is_valid_binary:
                        print("خطا: مقادیر ماتریس مجاورت باید فقط 0 یا 1 باشند.")
                        continue
                
                if len(row) == size:
                    matrix.append(row)
                    break
                else:
                    print(f"خطا: تعداد اعداد در این سطر ({len(row)}) با اندازه ماتریس ({size}) مطابقت ندارد. لطفا مجددا وارد کنید.")
            except ValueError:
                print("خطا: لطفا فقط عدد وارد کنید و آنها را با فاصله از هم جدا کنید.")
    return matrix

# ---
# گام اول: دریافت تعداد نقاط و نام آن‌ها
while True:
    try:
        num_nodes = int(input("لطفا تعداد نقاط (راس‌ها) را وارد کنید: "))
        if num_nodes > 0:
            break
        else:
            print("خطا: تعداد نقاط باید یک عدد مثبت باشد.")
    except ValueError:
        print("خطا: لطفا یک عدد وارد کنید.")

points = {}
for i in range(num_nodes):
    node_name = input(f"لطفا نام نقطه {i+1} را وارد کنید (مثلا A, B, ...): ").upper()
    points[node_name] = i

# ---
# گام دوم: ساخت ماتریس‌ها با استفاده از تعداد نقاط
adj_matrix = create_matrix("مجاورت", num_nodes, is_adjacency=True)
weight_matrix = create_matrix("وزن", num_nodes)

# ---
# گام سوم: دریافت مسیر و محاسبه طول آن
path_str = input("لطفا مسیر مورد نظر خود را با نام نقاط و با فاصله از هم وارد کنید (مثلا A B C): ")
path = path_str.upper().split()

total_length = 0
found_path = True

for i in range(len(path) - 1):
    start_node_name = path[i]
    end_node_name = path[i+1]
    
    if start_node_name not in points or end_node_name not in points:
        print("خطا: یکی از نقاط مسیر در تعریف اولیه وجود ندارد.")
        found_path = False
        break
        
    start_index = points[start_node_name]
    end_index = points[end_node_name]

    if start_index >= len(adj_matrix) or end_index >= len(adj_matrix) or start_index < 0 or end_index < 0:
        print("خطا: ایندکس نقاط مسیر خارج از محدوده ماتریس است.")
        found_path = False
        break

    if adj_matrix[start_index][end_index] == 1:
        edge_weight = weight_matrix[start_index][end_index]
        total_length += edge_weight
    else:
        print(f"راهی از {start_node_name} به {end_node_name} وجود ندارد.")
        found_path = False
        break

if found_path:
    print(f"\nطول کل مسیر {path}: {total_length}")