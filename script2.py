import random

n = int(input("n = "))
a, b = float(input("a = ")), float(input("b = "))

# Генерация массива вещественных чисел
arr = [round(random.uniform(-10, 10), 2) for _ in range(n)]
print(f"Исходный: {arr}")

# 1. Максимальный элемент
print(f"Максимум: {max(arr)}")

# 2. Сумма до последнего положительного
# Ищем индекс последнего элемента > 0
idx = next((i for i in range(n-1, -1, -1) if arr[i] > 0), -1)
s = sum(arr[:idx]) if idx != -1 else 0
print(f"Сумма до посл. положительного: {s}")

# 3. Удаление элементов с |x| в [a,b] и заполнение нулями
# Оставляем только те, чей модуль не в интервале
filtered = [x for x in arr if not (a <= abs(x) <= b)]
# Дополняем нулями до исходной длины n
result = filtered + [0.0] * (n - len(filtered))
print(f"Результат: {result}")