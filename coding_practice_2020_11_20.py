# 1. Favourite Colour
colour = input("What's your favourite colour? ")
print(f"Cool! My favourite colour is {colour} too!")
print()

# 2. Packs of Cans
cans_per_pack = int(input("How many cans are there in one pack? "))
packs = int(input("How many packs are there? "))
print("There are", cans_per_pack * packs, "cans in total.")
print()

# 3. Volume of a Rectangular Prism
length = float(input("What is the length of the rectangular prism in cm? "))
width = float(input("What is the width in cm? "))
height = float(input("What is the height in cm? "))
print("The volume of the rectangular prism is", length * width * height, "cm cubed.")
print()

# 4. Google Meet
reply = input("Hey, do you just join the Google Meet and mute the teacher? ")
if reply == "yes":
    print("That's probably not a good idea.")
if reply == "no":
    print("Ok. Good.")
