import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# ماتریس مجاورت گراف
# 1 یعنی بین دو نقطه راه (یال) وجود دارد، 0 یعنی راهی نیست.
# در این مثال، یک گراف 4 نقطه‌ای داریم.
adj_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
])

# تبدیل ماتریس مجاورت به یک شیء گراف
# networkx می‌تواند از یک آرایه numpy گراف بسازد.
G = nx.from_numpy_array(adj_matrix)

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
