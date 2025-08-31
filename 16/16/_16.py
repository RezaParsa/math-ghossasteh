# تابع برای دریافت و ساخت یک ماتریس مربعی
def create_matrix(matrix_name, size, require_binary=False):
    """
    این تابع از کاربر یک ماتریس مربعی می‌گیرد و آن را اعتبارسنجی می‌کند.
    """
    matrix = []
    print(f"Please enter {size} rows with {size} numbers in each row. Separate the numbers with spaces(secondmatrix is weightmatrix pls have attention on it):")

    for i in range(size):
        while True:
            try:
                row_str = input(f"Row {i+1}: ")
                row = [int(x) for x in row_str.split()]
                
                # بررسی مقادیر فقط برای ماتریس مجاورت
                if require_binary:
                    is_binary = all(num in [0, 1] for num in row)
                    if not is_binary:
                        print("error: pls enter num 1 or 0 just with space.")
                        continue
                
                if len(row) == size:
                    matrix.append(row)
                    break
                else:
                    print(f"error: count of this row  ({len(row)}) with matrix size ({size}) is not suit pls enter it again.")
            except ValueError:
                print("error: pls enter num just with space.")
    return matrix
   
while True:
        try:
            num_nodes  = int(input(f"pls enter node count :"))
            if num_nodes  > 0:
                break
            else:
                print("error : matrix size must be a postive number.")
        except ValueError:
            print("erroe: matrix size must be in poSetive nums.")


   
points = {}
for i in range(num_nodes):
    node_name = input(f"Pls enter edgename {i+1} (for example A, B, ...): ").upper()
    points[node_name] = i
# ---
# حالا با استفاده از تابع، ماتریس‌ها را می‌سازیم
adj_matrix = create_matrix("Mojaverat", num_nodes, require_binary=True)
weight_matrix = create_matrix("weight" ,num_nodes)


# ---
# مسیر مورد نظر
path_str = input("pls enter path that you need  with edgename and use space for sprate them (for example  A C D): ")
path = path_str.upper().split()

total_length = 0
found_path = True


for i in range(len(path) - 1):
    start_node_name = path[i]
    end_node_name = path[i+1]
    
    # بررسی کنید که آیا کلیدها در دیکشنری موجود هستند
    if start_node_name not in points or end_node_name not in points:
        print("Error : one of edge in not defined.")
        found_path = False
        break
        
    start_index = points[start_node_name]
    end_index = points[end_node_name]

    # بررسی کنید که آیا ایندکس‌ها در محدوده ماتریس‌ها هستند
    if start_index >= len(adj_matrix) or end_index >= len(adj_matrix):
        print("error: index of edge in out of range.")
        found_path = False
        break
    
   # بررسی می‌کنیم که آیا بین این دو نقطه راهی وجود دارد؟
    if adj_matrix[start_index][end_index] == 1:
        # اگر راهی وجود داشت، طول آن را به طول کل مسیر اضافه می‌کنیم
        edge_weight = weight_matrix[start_index][end_index]
        total_length += edge_weight
    else:
        # اگر راهی وجود نداشت، پیامی نمایش می‌دهیم و از حلقه خارج می‌شویم
        print(f"[Path  {start_node_name} to {end_node_name} is not valid.")
        found_path = False
        break

if found_path:
    print(f"\total path lenth {path}: {total_length}")