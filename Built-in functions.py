from functools import reduce

numbers = [10, 2, 8, 4, 6]
names = ["Анна", "Борис", "Виктор"]
scores = [85, 92, 78]

print(f"Длина списка: {len(numbers)}")        # 5
print(f"Сумма всех чисел: {sum(numbers)}")     # 30
print(f"Минимум: {min(numbers)}")              # 2
print(f"Максимум: {max(numbers)}")             # 10
print(f"Новый отсортированный список: {sorted(numbers)}") # [2, 4, 6, 8, 10]

print(f"Строка в число: {int('123') + 7}")     # 130
print(f"Число в строку: {str(10) + ' руб.'}")  # "10 руб."
print(f"В список: {list('ABC')}")              # ['A', 'B', 'C']
print(f"Логическое значение: {bool(1)}")       # True (0 - это False)

squares = list(map(lambda x: x**2, numbers)) 
print(f"Квадраты: {squares}") # [100, 4, 64, 16, 36]

big_nums = list(filter(lambda x: x > 5, numbers))
print(f"Числа > 5: {big_nums}") # [10, 8, 6]

product = reduce(lambda x, y: x * y, numbers)
print(f"Произведение всех чисел: {product}") # 3840

print("\nСписок студентов:")

for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{i}. {name} получил {score}")

# Результат цикла:
# 1. Анна получил 85
# 2. Борис получил 92
# 3. Виктор получил 78
