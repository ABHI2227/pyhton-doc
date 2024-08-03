#  problem: recommend a type of pet food based on the pet species and age 
# (eg: dog <2 year - puppy food , cat > 5 year - Senior cat food).

pet = "dog"
age = 1
if pet == "dog" and age < 2:
    print("puppy food")
elif pet == "cat" and age > 5:
    print("Senior cat food")
exit()