m = float(input('sm: '))
kg = float(input('kg: '))
result = kg / (m ** 2)

if m <= 0 or kg <= 0 or m < 0.5 or m > 3.0 or kg < 1 or kg > 500:
    print(
        """Xatolik:\n
        - Vazn va bo'y musbat bo'lishi kerak\n
        - Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak\n
        - Vazn 1-500 kg oralig'ida bo'lishi kerak"""
    )
else:
    print('BMI:',round(result,2))
    if result < 18.5: 
        print('Tasnif:',"Kam vazn")
    elif result < 25:
        print('Tasnif:',"Normal vazn")
    elif result < 30:
        print( 'Tasnif:',"Ortiqcha vazn")
    elif result > 30:
        print('Tasnif:',"Semizlik")