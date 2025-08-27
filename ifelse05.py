email = input('email: ')
if ('@' in email) and ('.com' in email or '.uz' in email or '.org' in email or '.net' in email ):
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")