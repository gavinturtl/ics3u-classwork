# 1.
def add_three(a: float, b: float, c: float) -> float:
    return a + b + c

result = add_three(1, 2, 3)
print(result)

# 2. 
def name_age(name: str, age: int) -> str:
    return f"Your name is {name} and you are {age} years old."

result = name_age("Ashley", 16)
print(result)

# 3.
def average_of_two(a: float, b: float) -> float:
    return (a + b) / 2

result = average_of_two(10, 20)
print(result)

# 4. 
def largest_of_three(a: float, b: float, c: float) -> float:
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

result = largest_of_three(10, 20, 12)
print(result)

# 5.
def first_two(string: str) -> str:
    return str[0:2]

result = first_two("hamburger")
print(result)
