def addition(n):
    return n + n**2

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))