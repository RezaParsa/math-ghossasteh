
def find_degrees(adj_matrix):
    """
    درجه هر گره را در یک ماتریس مجاورت محاسبه می‌کند.
    """
    num_vertices = len(adj_matrix)
    degrees = [0] * num_vertices
    for i in range(num_vertices):
        for j in range(num_vertices):
            # برای گراف‌های غیرجهت‌دار، مجموع وزن‌های یال‌ها به هر گره را حساب می‌کنیم.
            # یال‌های دوطرفه (i, j) و (j, i) هر کدام یک درجه به i و j اضافه می‌کنند.
            # یال‌های حلقه‌ای (self-loop) به اندازه دو درجه اضافه می‌کنند.
            degrees[i] += adj_matrix[i][j]
            # در صورتی که گراف حلقه‌ای داشت، فقط یک بار حساب می‌کنیم.
            if i == j:
                degrees[i] += adj_matrix[i][j]
    return degrees

def is_connected(adj_matrix):
    """
    همبندی (Connectedness) گراف را بررسی می‌کند.
    """
    num_vertices = len(adj_matrix)
    if num_vertices == 0:
        return True
    
    # پیدا کردن اولین گره غیرمنفرد برای شروع پیمایش
    start_node = -1
    for i in range(num_vertices):
        if sum(adj_matrix[i]) > 0:
            start_node = i
            break
            
    # اگر گره غیرمنفردی وجود نداشت، گراف خالی است و همبند محسوب می‌شود.
    if start_node == -1:
        return True

    visited = [False] * num_vertices
    stack = [start_node]
    visited[start_node] = True
    
    # پیمایش عمق اول (DFS) برای بررسی همبندی
    while stack:
        u = stack.pop()
        for v in range(num_vertices):
            if adj_matrix[u][v] > 0 and not visited[v]:
                visited[v] = True
                stack.append(v)
    
    # بررسی اینکه آیا تمام گره‌های غیرمنفرد بازدید شده‌اند یا خیر
    for i in range(num_vertices):
        if sum(adj_matrix[i]) > 0 and not visited[i]:
            return False
            
    return True

def find_eulerian_path(adj_matrix):
    """
    مسیر یا مدار اویلری را در گراف پیدا می‌کند.
    اگر مسیر یا مداری وجود نداشت، None برمی‌گرداند.
    """
    num_vertices = len(adj_matrix)
    degrees = find_degrees(adj_matrix)
    odd_degree_nodes = [i for i, degree in enumerate(degrees) if degree % 2 != 0]

    # تعیین نوع مسیر اویلری بر اساس تعداد گره‌های با درجه فرد
    if len(odd_degree_nodes) > 2 or (len(odd_degree_nodes) == 1):
        print("graph doesnt have oerlry path")
        return None
        
    if not is_connected(adj_matrix):
        print("graph not hamband there is no oelrry path.")
        return None

    # انتخاب گره شروع
    start_node = odd_degree_nodes[0] if len(odd_degree_nodes) == 2 else 0
    
    # کپی کردن ماتریس مجاورت تا بتوانیم یال‌ها را در حین پیمایش حذف کنیم
    temp_adj_matrix = [row[:] for row in adj_matrix]
    
    path = []
    stack = [start_node]
    
    while stack:
        u = stack[-1]
        
        # پیدا کردن یک گره همسایه برای پیمایش
        next_node = -1
        for v in range(num_vertices):
            if temp_adj_matrix[u][v] > 0:
                next_node = v
                break
        
        # اگر گره همسایه‌ای پیدا شد، به مسیر ادامه می‌دهیم.
        if next_node != -1:
            stack.append(next_node)
            # حذف یال پیمایش شده
            temp_adj_matrix[u][next_node] -= 1
            temp_adj_matrix[next_node][u] -= 1
        else:
            # اگر گره فعلی هیچ یال پیمایش نشده‌ای نداشت، آن را به مسیر اضافه می‌کنیم
            # و از پشته خارج می‌کنیم.
            path.append(stack.pop())
            
    return path[::-1] # برگرداندن مسیر به ترتیب صحیح (معکوس)

def print_degrees(adj_matrix, title):
    """
    درجه گره‌ها را چاپ می‌کند.
    """
    degrees = find_degrees(adj_matrix)
    print(title)
    for i, degree in enumerate(degrees):
        print(f"node deg {i}: {degree}")
    print("\n" + "-"*30 + "\n")

# --- مثال استفاده ---

# مثال 1: مدار اویلری (تمام گره‌ها با درجه زوج)
adj_matrix1 =[
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
print_degrees(adj_matrix1, "--- node degree in example 1 ---")

eulerian_path1 = find_eulerian_path(adj_matrix1)
if eulerian_path1:
    print("oel path found:", " -> ".join(map(str, eulerian_path1)))
print("\n" + "-"*30 + "\n")

# مثال 2: مسیر اویلری (دو گره با درجه فرد)
adj_matrix2 = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
print_degrees(adj_matrix2, "--- node degree in example 2 ---")

eulerian_path2 = find_eulerian_path(adj_matrix2)
if eulerian_path2:
    print("oel path found:", " -> ".join(map(str, eulerian_path2)))
print("\n" + "-"*30 + "\n")

# مثال 3: بدون مسیر اویلری (سه گره با درجه فرد)
adj_matrix3 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
print_degrees(adj_matrix3, "--- node degree in example 3 ---")

find_eulerian_path(adj_matrix3)
