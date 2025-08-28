# نقشه ما (گراف)
# هر کلید یک نقطه است، و هر مقدار یک دیکشنری دیگر است
# که نقاط مجاور و فاصله آن‌ها را نشان می‌دهد.
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# تابع جادویی ما برای پیدا کردن کوتاه‌ترین مسیر
def dijkstra(graph, start, end):
    # اینجا یک جعبه برای نگهداری کوتاه‌ترین مسافت‌ها می‌سازیم
    # اول به همه جا می‌گیم که مسافتشون بی‌نهایت (خیلی زیاد) است
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # مسافت از نقطه شروع به خودش صفره
    
    # یک لیست خالی برای نقاطی که از آن‌ها بازدید کردیم
    visited = []
    
    # یک دیکشنری برای نگهداری مسیر
    path = {}

    while len(visited) < len(graph):
        # پیدا کردن نزدیک‌ترین نقطه از میان نقاطی که هنوز نرفتیم
        min_distance = float('infinity')
        closest_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                closest_node = node
        
        # اگر نزدیک‌ترین نقطه پیدا نشد، از حلقه خارج می‌شیم
        if closest_node is None:
            break
            
        # این نقطه رو به لیست نقاطی که دیدیم اضافه می‌کنیم
        visited.append(closest_node)
        
        # حالا به همسایه‌های این نقطه نگاه می‌کنیم
        for neighbor, weight in graph[closest_node].items():
            if distances[closest_node] + weight < distances[neighbor]:
                # اگر مسیر جدید کوتاه‌تر بود، اون رو جایگزین می‌کنیم
                distances[neighbor] = distances[closest_node] + weight
                path[neighbor] = closest_node # و مسیر رو هم یادداشت می‌کنیم

    return distances, path

# حالا می‌خواهیم مسیر رو از "A" به "D" پیدا کنیم
distances, path = dijkstra(graph, 'A', 'D')

# چاپ کردن نتیجه
print("shortest path from A to D:", distances['D'])

# حالا مسیر رو از آخر به اول پیدا می‌کنیم
route = []
current_node = 'D'
while current_node is not None:
    route.insert(0, current_node)
    current_node = path.get(current_node, None)

print("path:", ' -> '.join(route))
