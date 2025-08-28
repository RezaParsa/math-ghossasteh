import networkx as nx
import matplotlib.pyplot as plt

# این جدول  ماست!
# اگر عدد 1 رو ببینی، یعنی یک فلش از اونجا به اونجا داریم.
# مثلاً در سطر 0، ستون 1 عدد 1 هست، یعنی یک فلش از نقطه 0 به نقطه 1 داریم.
my_grid = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

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
plt.title("نقاشی فلش دار ما")

# و در آخر، نقاشی‌مان را نشان می‌دهیم!
plt.show()
