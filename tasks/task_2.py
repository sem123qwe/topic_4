a: int = int(input('Введите число a: ')) 
b: int = int(input('Введите число b: '))   

if a >= 0 and b >= 0:
    c = a
    a = b
    b = c

print("Значения после перестановки:")
print('a =', a, '\nb =', b)    
