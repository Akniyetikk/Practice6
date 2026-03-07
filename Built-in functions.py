from functools import reduce

numbers = [10, 2, 8, 4, 6]
names = ["Akniyet", "Aigul", "Azamat"]
scores = [85, 92, 78]

print(f"Length: {len(numbers)}")  
print(f"Sum: {sum(numbers)}")    
print(f"Min: {min(numbers)}")    
print(f"Max: {max(numbers)}")     
print(f"Sorted list: {sorted(numbers)}") 

print(f"Str to int: {int('123') + 7}")    
print(f"Int to str: {str(10) + ' tg.'}")  
print(f"List: {list('ABC')}")    
print(f"Logical meaning: {bool(1)}")      

squares = list(map(lambda x: x**2, numbers)) 
print(f"Squares: {squares}") 

big_nums = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {big_nums}") 

product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}") 

print("\nlist of students")

for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{i}. {name} got {score}")


