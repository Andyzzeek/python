rychlost = 60

if rychlost > 50 and rychlost < 90:
    print("Mimo obec")
elif rychlost <= 50:
    print("OBEC")
elif rychlost > 90 and rychlost < 130:
    print("DALNICE")
else:
    print("POZOR, JEDES MOC RYCHLE")