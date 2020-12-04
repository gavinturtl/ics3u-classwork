# 1.
def add_three(a: float, b: float, c: float) -> float:
    return a + b + c
# 2. 
def name_age(name: str, age: int) -> str:
    return f"Your name is {name} and you are {age} years old."
# 3.
def average_of_two(a: float, b: float) -> float:
    return (a + b) / 2
# 4. 
def largest_of_three(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
# 5.
def first_two(string: str) -> str:
    return string[0:2]

result = add_three(1, 2, 3)
print(result)

result = name_age("Ashley", 16)
print(result)

result = average_of_two(10, 20)
print(result)

result = largest_of_three(10, 20, 12)
print(result)

result = first_two("hamburger")
print(result)
