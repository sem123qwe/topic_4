a: int = int(input('Введите число a: '))
b: int = int(input('Введите число b: '))

# c = a
# a = b
# b = c

a, b = b, a  # x, y = 10, 20

print('Значения после перестановки:')
print('a =', a, '\nb =', b)
