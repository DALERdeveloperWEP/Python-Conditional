hour = int(input('hours: '))
if hour >= 5 and hour <= 11:
    print("Ertalab")
elif hour >= 12 and hour <= 17:
    print("Kunduzi")
elif hour >= 18 and hour <= 21:
    print( "Kechqurun")
elif (hour >= 22 and hour <= 23) or (hour >= 0 and hour <= 4):
    print( "Tun")
else:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")