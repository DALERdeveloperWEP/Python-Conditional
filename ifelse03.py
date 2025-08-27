import os

filename = input("Fayl nomini kiriting: ")

if os.path.exists(filename):
    print(f"Fayl '{filename}' mavjud.")
else:
    print(f"Fayl '{filename}' topilmadi.")
