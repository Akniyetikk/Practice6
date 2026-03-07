from functools import reduce

data = ["10", "25", "30", "45", "50"]
names = ["product A", "product B", "product C"]
prices = [1000, 2500, 3000]

numbers = list(map(int, data))
print(numbers)

filtered = list(filter(lambda x: x > 25, numbers))
print(filtered)

total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

print("\nОтчет:")
for i, (name, price) in enumerate(zip(names, prices), 1):
    type_status = "OK" if isinstance(price, int) else "Error"
    print(f"{i}. {name} — {price} tg. [Type status: {type_status}]")

print(f"\n {sorted(prices, reverse=True)}")
