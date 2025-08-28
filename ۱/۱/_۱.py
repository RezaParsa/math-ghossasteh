
import itertools

# اینجا گزاره مرکب خود را به عنوان یک رشته وارد کنید.
# از حروف کوچک برای گزاره‌ها (مثل p و q) استفاده کنید.
# از کلمات 'and'، 'or' و 'not' برای عملگرها استفاده کنید.
proposition = input("pls enter ur gozare (example: p and (not q)): ").lower()

# پیدا کردن تمام متغیرهای موجود در گزاره
variables = sorted(list(set(char for char in proposition if 'a' <= char <= 'z')))

# تعداد متغیرها
num_variables = len(variables)

# ساختن تمام ترکیبات ممکن از True و False برای متغیرها
truth_values = list(itertools.product([False, True], repeat=num_variables))

# چاپ سربرگ جدول
header = variables + [proposition]
print("\t".join(header))

# چاپ یک خط جداکننده برای زیبایی جدول
print("-" * (8 * (len(variables) + 1)))

# محاسبه و چاپ هر سطر از جدول
for combination in truth_values:
    # ساختن دیکشنری برای نگهداری مقادیر فعلی متغیرها
    # مثلاً {'p': True, 'q': False}
    context = dict(zip(variables, combination))
    
    # جایگزین کردن عملگرهای منطقی برای استفاده در پایتون
    py_proposition = proposition.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ')
    
    # محاسبه نتیجه نهایی گزاره با استفاده از eval()
    try:
        result = eval(py_proposition, {}, context)
    except NameError:
        print("error: unknowe name.")
        exit()
    
    # چاپ مقادیر متغیرها و نتیجه نهایی
    row_values = [str(val) for val in combination]
    row_values.append(str(result))
    print("\t".join(row_values))