number: int = int(input('Введите положительное трехзначное число: '))  

hundreds: float =  number // 100 
tens: float = number // 10 % 10  
units: float = number % 10  

sum_digits: int = hundreds + tens + units 

product_digits: int = hundreds * tens * units 

print('Сумма цифр:', sum_digits)  
print('Произведение цифр:', product_digits)  
