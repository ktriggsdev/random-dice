import random

number_of_sides = int(input("Please choose how many sides of the dice you want (6, 10, 12, 15, 20, 24, 32, 50, 100, 120, 144): "))

if number_of_sides not in [6, 10, 12, 15, 20, 24, 32, 50, 100, 120, 144]:
    print("Invalid number of sides. Please enter a number between 6 and 144.")
    exit()

number_of_dice = int(input("How many dice do you want to roll? "))
if number_of_dice not in [1, 2, 3]:
    print("Invalid number of dice. Please enter a number between 1 and 3.")
    exit()


# Number of sides == 6
if number_of_dice == 1 and number_of_sides == 6:
    random_dice = random.randint(1, 6)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 6:
    random_dice = random.randint(1, 6) + random.randint(1, 6)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 6:
    random_dice = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    print(random_dice)
    
# number of sides == 10
elif number_of_dice == 1 and number_of_sides == 10:
    random_dice = random.randint(1, 10)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 10:
    random_dice = random.randint(1, 10) + random.randint(1, 10)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 10:
    random_dice = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
    print(random_dice)

# number of sides == 12
elif number_of_dice == 1 and number_of_sides == 12:
    random_dice = random.randint(1, 12)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 12:
    random_dice = random.randint(1, 12) + random.randint(1, 12)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 12:
    random_dice = random.randint(1, 12) + random.randint(1, 12) + random.randint(1, 12)
    print(random_dice)
 
# number of sides == 15   
elif number_of_dice == 1 and number_of_sides == 15:
    random_dice = random.randint(1, 15)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 15:
    random_dice = random.randint(1, 15) + random.randint(1, 15)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 15:
    random_dice = random.randint(1, 15) + random.randint(1, 15) + random.randint(1, 15)
    print(random_dice)

# number of sides = 20    
elif number_of_dice == 1 and number_of_sides == 20:
    random_dice = random.randint(1, 20)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 20:
    random_dice = random.randint(1, 20) + random.randint(1, 20)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 20:
    random_dice = random.randint(1, 20) + random.randint(1, 20) + random.randint(1, 20)
    print(random_dice)
    
# number of sides = 24    
elif number_of_dice == 1 and number_of_sides == 24:
    random_dice = random.randint(1, 24)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 24:
    random_dice = random.randint(1, 24) + random.randint(1, 24)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 24:
    random_dice = random.randint(1, 24) + random.randint(1, 24) + random.randint(1, 24)
    print(random_dice)
    
# number of sides = 32    
elif number_of_dice == 1 and number_of_sides == 32:
    random_dice = random.randint(1, 32)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 32:
    random_dice = random.randint(1, 32) + random.randint(1, 32)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 32:
    random_dice = random.randint(1, 32) + random.randint(1, 32) + random.randint(1, 32)
    print(random_dice)
    
    
# number of sides = 50    
elif number_of_dice == 1 and number_of_sides == 50:
    random_dice = random.randint(1, 50)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 50:
    random_dice = random.randint(1, 50) + random.randint(1, 50)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 50:
    random_dice = random.randint(1, 50) + random.randint(1, 50) + random.randint(1, 50)
    print(random_dice)
    
    
# number of sides = 100    
elif number_of_dice == 1 and number_of_sides == 100:
    random_dice = random.randint(1, 100)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 100:
    random_dice = random.randint(1, 100) + random.randint(1, 100)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 100:
    random_dice = random.randint(1, 100) + random.randint(1, 100) + random.randint(1, 100)
    print(random_dice)
    
    
# number of sides = 120    
elif number_of_dice == 1 and number_of_sides == 120:
    random_dice = random.randint(1, 120)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 120:
    random_dice = random.randint(1, 120) + random.randint(1, 120)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 120:
    random_dice = random.randint(1, 120) + random.randint(1, 120) + random.randint(1, 120)
    print(random_dice)
    
    
# number of sides = 144    
elif number_of_dice == 1 and number_of_sides == 144:
    random_dice = random.randint(1, 144)
    print(random_dice)
elif number_of_dice == 2 and number_of_sides == 144:
    random_dice = random.randint(1, 144) + random.randint(1, 144)
    print(random_dice)
elif number_of_dice == 3 and number_of_sides == 144:
    random_dice = random.randint(1, 144) + random.randint(1, 144) + random.randint(1, 144)
    print(random_dice)
    
else:
    print("ERROR: invalid number of dice or sides")