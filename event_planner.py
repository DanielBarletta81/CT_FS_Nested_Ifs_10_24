# Task 1 Code Correction


# Buggy

""" attendees = input("Enter number of attendees: ") # attendees should be an integer
venue = "large hall" if attendees > 100 else "conference room"
print(venue) """

# Corrected

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task 2: Venue Selection

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if attendees > 125:
    if attendees > 175:
        print("The venue will require a projector and an audio system.")
    else:
        print("Depending on your audience, an audio system may be needed.")
elif venue == "large hall" and attendees < 125:
    print("You will need a projector, but an audio system is not required.")

elif venue == "conference room" and attendees > 50:
    print("Better speak up!")

else:
    print("You should be seen and heard easily in this " + venue)

#Task 3: Catering Choices

#Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

meal_choice = input("Would you like vegetarian food? ")

if meal_choice == 'yes':
    print('Try Veggie Delight Caterers. They have great vegetarian lunch specials. ')
else:
    print('The best overall option is Gourmet Meals Caterers.')