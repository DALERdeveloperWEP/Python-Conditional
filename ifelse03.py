import os

file_name = input("Fayl nomini kiriting: ")

if os.path.exists(file_name):
    print(f"Fayl '{file_name}' mavjud.")
else:
    print(f"Fayl '{file_name}' topilmadi.")