import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ماتریس مجاورت گراف
# 1 یعنی بین دو نقطه راه (یال) وجود دارد، 0 یعنی راهی نیست.
# در این مثال، یک گراف 4 نقطه‌ای داریم.
while True:
    try:
        n_a = int(input("pls enter matrix A size: "))
        break
    except ValueError:
        print("error : matrix size must be posetive num.")

matrix_a = []
print(f"pls {n_a} row of num must be enter with space:")

for i in range(n_a):
    while True:
        try:
            row_str = input(f"row {i+1}: ")
            row = [int(x) for x in row_str.split()]
            if len(row) == n_a:
                matrix_a.append(row)
                break
            else:
                print(f"error: count of this row ({len(row)}) wiht size of matrix  ({n_a}) is not suit pls renter it .")
        except ValueError:
            print("error enter nums with space .")

# تبدیل ماتریس مجاورت به یک شیء گراف
# networkx می‌تواند از یک آرایه numpy گراف بسازد.
G = nx.from_numpy_array(np.array(matrix_a))

# رسم گراف
# با استفاده از spring_layout موقعیت نقاط را برای نمایش بهتر مشخص می‌کنیم.
pos = nx.spring_layout(G) 

# حالا گراف را با رنگ‌های زیبا و واضح رسم می‌کنیم.
# nx.draw_networkx_nodes: نقاط گراف را رسم می‌کند.
# nx.draw_networkx_edges: یال‌ها (خطوط) را رسم می‌کند.
# nx.draw_networkx_labels: برچسب‌ها (شماره نقاط) را روی گراف قرار می‌دهد.
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

# نمایش گراف رسم شده
plt.title("show graph from matrixmoghvrat")
plt.axis('off') # محورهای x و y را مخفی می‌کند
plt.show()
