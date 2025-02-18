rychly = True 
chytry = True
pomaly = True
hloupy = False

values = [rychly, chytry, pomaly, hloupy]

print("Values:", values)  # Debug print to check the values

if False in values:
    print(False)
else:
    print(True)

