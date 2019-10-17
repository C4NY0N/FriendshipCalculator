import random
name_1 = input("Who is the first person in the friendship? ")
name_2 = input("Who is the second person in the friendship? ")
percentage = random.randint(0, 101)

if percentage == 0:
    print("Your friendship is terrible, break up")
elif percentage > 0 and percentage < 26:
    print("Ehhhhh ya need some work.....a lot of work")
elif percentage > 25 and percentage < 51:
    print("Your friendship is decent, but it still needs work")
elif percentage > 50 and percentage < 76:
    print("...It's okay")
elif percentage > 75 and percentage < 91:
    print("Pretty good!")
else:
    print("Best friends!")




