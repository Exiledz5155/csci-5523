print("Aitan Morbidly Obese Singh")

def add_numbers(a: int, b: int) -> int:
    return a + b

# Intentional type error the "10" should error due to mypy
result = add_numbers(5, "10")  # MyPy should complain about this line
print(result)