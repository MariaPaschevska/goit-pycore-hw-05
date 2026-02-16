from typing import Callable, Generator
import re

# Функція приймає рядок як аргумент і повертає генератор, що ітерує по всіх дійсних числах у тексті
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Використовує регулярний вираз для пошуку всіх  дійсних чисел у тексті
    pattern = r'\d+\.\d+|\d+'
    numbers = re.findall(pattern, text)
    for num in numbers:
        yield float(num)

# Використовує generator_numbers для обчислення загальної суми чисел у вхідному рядку та приймає його як аргумент при виклику
def sum_profit(text: str, func: Callable) -> float:
    # Використання вбудованої функції sum для обчислення суми всіх чисел, згенерованих generator_numbers
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
