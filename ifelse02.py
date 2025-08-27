password = input('password: ')
if len(password) >= 8 and (password.isalpha() == False and password.isdigit() == False):
    print("Parol qabul qilindi.")
else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")