# ماتریس اصلی ما
matrix = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

# تابع بستار بازتابی
def reflexive_closure(m):
    n = len(m)
    result = [row[:] for row in m]
    for i in range(n):
        result[i][i] = 1
    return result

# تابع بستار تقارنی
def symmetric_closure(m):
    n = len(m)
    result = [row[:] for row in m]
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                result[j][i] = 1
    return result

# تابع بستار ترایایی
def transitive_closure(m):
    n = len(m)
    result = [row[:] for row in m]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1
    return result

# --- نمایش نتایج ---
print("main matrix:")
for row in matrix:
    print(row)

print("\n---")

# بستار بازتابی
rc = reflexive_closure(matrix)
print("bastar Baztaby:")
for row in rc:
    print(row)

print("\n---")

# بستار تقارنی
sc = symmetric_closure(matrix)
print("Bastar Tagharony:")
for row in sc:
    print(row)

print("\n---")

# بستار ترایایی
tc = transitive_closure(matrix)
print("Bastar Tarayai:")
for row in tc:
    print(row)
