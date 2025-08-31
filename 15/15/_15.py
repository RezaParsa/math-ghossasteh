# ماتریس مجاورت یک گراف را تعریف می‌کنیم.
# این ماتریس باید یک مربع (n*n) باشد.
# 1 یعنی راه دارد، 0 یعنی راه ندارد.
while True:
    try:
        n_a = int(input("pls enter matrix A size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

adjacency_matrix = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                adjacency_matrix.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")


# تعداد نقاط در گراف (تعداد سطرها یا ستون‌ها)
num_nodes = len(adjacency_matrix)

# یک لیست برای نگهداری نقاطی که به آن‌ها رسیده‌ایم
# در ابتدا، فقط به نقطه اول (نقطه 0) رسیده‌ایم.
reached_nodes = {0} # با یک مجموعه (set) کار می‌کنیم که راحت‌تر است

# یک صف برای نگهداری نقاطی که باید بررسی شوند
# ابتدا فقط نقطه شروع را در صف قرار می‌دهیم.
queue = [0]

# تا زمانی که صف خالی نشده، ادامه می‌دهیم
while queue:
    # یک نقطه را از صف برمی‌داریم
    current_node = queue.pop(0)

    # همسایه‌های این نقطه را بررسی می‌کنیم
    for neighbor in range(num_nodes):
        # اگر راهی از نقطه فعلی به همسایه وجود داشت (یعنی 1 بود)
        # و هنوز به این همسایه نرسیده‌ایم...
        if adjacency_matrix[current_node][neighbor] == 1 and neighbor not in reached_nodes:
            # همسایه را به لیست نقاطی که به آن‌ها رسیده‌ایم اضافه می‌کنیم
            reached_nodes.add(neighbor)
            # و آن را به صف اضافه می‌کنیم تا بعداً همسایه‌های آن را بررسی کنیم
            queue.append(neighbor)

# در نهایت، بررسی می‌کنیم که آیا تعداد نقاطی که به آن‌ها رسیده‌ایم،
# با تعداد کل نقاط گراف برابر است؟
if len(reached_nodes) == num_nodes:
    print("Graph in Hamband.")
else:
    print("Graph is not Hamband.")
