from functools import reduce

data = ["10", "25", "30", "45", "50"]
names = ["Товар А", "Товар Б", "Товар В"]
prices = [1000, 2500, 3000]

numbers = list(map(int, data))
print(f"Числа: {numbers}")

filtered = list(filter(lambda x: x > 25, numbers))
print(f"Числа > 25: {filtered}")

total_sum = reduce(lambda x, y: x + y, numbers)
print(f"Сумма через reduce: {total_sum}")

print("\nОтчет по товарам:")
for i, (name, price) in enumerate(zip(names, prices), 1):
    type_status = "OK" if isinstance(price, int) else "Error"
    print(f"{i}. {name} — {price} руб. [Статус типа: {type_status}]")

print(f"\nСортировка цен: {sorted(prices, reverse=True)}")
