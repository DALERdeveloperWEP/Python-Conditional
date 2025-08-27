num1 = float(input('number1: '))
num2 = float(input('number2: '))
operation = input('operation: ')

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Nolga bo'lish mumkin emas")
    else:
        print(num1 / num2)
else:
    print(f"Noto'g'ri {operation} amal. Faqat +, -, *, / ishlatiladi.")