passward = "Secure3p@ss"

if len(passward) < 6:
    strength = "weak"
elif len(passward) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Passward Strength is : ", strength)