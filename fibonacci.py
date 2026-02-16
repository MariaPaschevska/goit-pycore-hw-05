# Функція для обчислення чисел Фібоначчі з використанням кешування
def caching_fibonacci():
    cache = {}
    def fibonacci(n):
       if n <= 0:
           return 0
       elif n == 1:
           return 1
       elif n in cache:
           return cache[n]
       
       cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
       return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))