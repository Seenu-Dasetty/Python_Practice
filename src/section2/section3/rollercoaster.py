# print("welcome to rollercoaster")
# height = int(input("what is your height in cms"))
# if height >= 120:
#     print("you can ride rollercoaster")
#
# else:
#     print("sorry you have to grow taller before you can ride.")


# #----
# number_to_check = int(input("what is the number you want to check? "))
# if number_to_check % 2 == 0:
#     print("even")
#
# else:
#     print("odd")


##----------------------------
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("underweight")


#-----------------
print("welcome to rollercoaster")
height = int(input("what is your height in cms "))
bill = 0
if height >= 120:
    print("you can ride rollercoaster")
    age = int(input("what is your age?"))
    if age <= 12:
        bill = 5
        print("your ticket price is $5.")
    elif age <= 18:
        bill = 7
        print("your ticket price is $7.")
    else:
        bill = 12
        print("your ticket price is $12.")
    want_photo = input("Do you want to have a photo take? type y for yes and n for no." )
    if want_photo == "y":
        bill += 3
    print(f"final bill is {bill}")

else:
    print("sorry you have to grow taller before you can ride.")

