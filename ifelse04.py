money = int(input('balance: '))
balance = 5000

if money < 0 :
     print("Manfiy summa kiritib bo'lmaydi.")
else:
    if balance >= money:
        print(f"Pul yechildi. Qolgan balans: {balance - money} so'm")
    else:
        print("Mablag' yetarli emas. Sizning balansingiz: 5000 so'm")