# ماتریس اصلی ما
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
for row in matrix_a:
    print(row)

print("\n---")

# بستار بازتابی
rc = reflexive_closure(matrix_a)
print("bastar Baztaby:")
for row in rc:
    print(row)

print("\n---")

# بستار تقارنی
sc = symmetric_closure(matrix_a)
print("Bastar Tagharony:")
for row in sc:
    print(row)

print("\n---")

# بستار ترایایی
tc = transitive_closure(matrix_a)
print("Bastar Tarayai:")
for row in tc:
    print(row)
