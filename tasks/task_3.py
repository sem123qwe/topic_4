first_number: str = input('Введите первое число: ')
second_number: str = input('Введите второе число: ')

result: bool = (bool(first_number > second_number))

print('Число', first_number, 'больше числа', second_number, 'это - ', result)
