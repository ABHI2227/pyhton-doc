distance = 170

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"


print("AI recommends you the trsnsport of: ", transport)