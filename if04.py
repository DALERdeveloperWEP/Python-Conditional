num = int(input('age: '))
money = 100
if num >=0 and num <=6:
    print(f"Yakuniy narx: {money-(money * 0.50)} so'm (50% chegirma qo'llanildi)")
if num>=7 and num<=17:
    print(f"Yakuniy narx: {money-(money * 0.20)} so'm (20% chegirma qo'llanildi)")
if num > 60 :
    print(f"Yakuniy narx: {money-(money * 0.30)} so'm (30% chegirma qo'llanildi)")