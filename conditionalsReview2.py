# #Create a Python script that assigns a grade to a student based on their exam score.
# Ask the user to input a score. Assume the score is out of 100.


# #functions allow me to wrap up code and reuse it 
# def scoreMe():
#     score = int(input("Enter your score: "))
#     print("You entered", score)
#     # Implement the logic to determine the grade based on the score:
#     # A score of 90 and above is an "A".
#     if score >= 90:
#         print("A")
#     # A score of 80 to 89 is a "B".
#     elif score >= 80 and score <90: 
#         print("B")
#     # A score of 70 to 79 is a "C".
#     elif score >= 70 and score < 80:
#         print("C")
#     # A score of 60 to 69 is a "D".
#     elif score >= 60 and score < 70:
#         print("D")
#     # A score below 60 is an "F".
#     elif score >= 50 and score < 60:
#         print("F")
#     # Ensure the score entered is within the valid range (0-100). If not, print an error message.
    
# #call the function
# scoreMe()
# scoreMe()
# scoreMe()

dietaryrestrictions = input("Do you have any dietary restrictions?")
if dietaryrestrictions == "yes":
    type = (input("What kind?"))
else:
    print("Thank you.")
if type == "Vegetarian":
    print("You can eat a salad.")
elif type == "gluten-free":
    print("You can eat gluten-free pasta")
elif type == "nut-free":
    print("You can eat a burger")
meal = input("What meal would you like? ")
print("The meal fits your preference")
payment = (input("Do you have a payment plan? "))
if payment == "yes":
    print("its been successfully paid.")
else:
    amount = int(input("Enter the amount of payment "))

outside = input("would you like to go outside? ")
outside = True
if outside:
    print("You can go eat at the picnic table.")
else:
    print("Stay inside")