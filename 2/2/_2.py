from xml.dom import ValidationErr
from xmlrpc.client import TRANSPORT_ERROR
import networkx as nx
import matplotlib.pyplot as plt


# اگر عدد 1 رو ببینی، یعنی یک فلش از اونجا به اونجا داریم.
# مثلاً در سطر 0، ستون 1 عدد 1 هست، یعنی یک فلش از نقطه 0 به نقطه 1 داریم.
try:
    n = int(input("please enter youtr matrix size in number:"))
except ValueError:
    print("Error : size of matrix must be posetive number")
    exit()
    
#اینجا یه لیست خالی درست میکنیم
my_grid = []

print(f" \n please enter {n} row of number from 0-1 with space")

# قدم سوم: گرفتن ورودی برای هر سطر و ساخت ماتریس

for i in range (n):
    while True:
        try:
            row_str = input (f"row {i+1}:")
            row = [int(x) for x in row_str.split()]
            
            if len(row) == n:
                my_grid.append(row)
                break
            else:
                print(f"error num of onsor of this row is not suit for ({len(row)}) with matrix size of {n}")
        except ValueError:
            print("error: pls enter 0 or 1 with space")
            
    


# یک جعبه خالی می‌سازیم.
my_graph = nx.DiGraph()

# حالا به هر نقطه یک اسم می‌دهیم.
# ما اینجا 4 تا نقطه داریم: 0، 1، 2، و 3
number_of_points = len(my_grid)
for i in range(number_of_points):
    my_graph.add_node(i)

# حالا در جدول می‌گردیم و فلش‌ها را پیدا می‌کنیم.
for x in range(number_of_points):
    for y in range(number_of_points):
        # اگر در خانه‌ای عدد 1 بود...
        if my_grid[x][y] == 1:
            # یک فلش از نقطه x به نقطه y می‌کشیم.
            my_graph.add_edge(x, y)

# حالا وقتشه که نقاشی رو بکشیم.
nx.draw(my_graph, with_labels=True, node_color='skyblue', node_size=1000, font_size=16)

# به نقاشی‌مون یک اسم می‌دیم.
plt.title("نمایش گراف بر اساس ماتریس")

plt.show()
