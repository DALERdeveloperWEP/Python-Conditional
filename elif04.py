km = int(input('km: '))

if km < 0:
    print("Masofa manfiy bo'la olmaydi!")
elif km <= 1:
    print("Piyoda yuring")
elif km <= 5:
    print("Velosiped yoki elektr skuter")
elif km <= 50:
    print("Avtobus yoki mashina")
else:
    print("Poyezd yoki samolyot")