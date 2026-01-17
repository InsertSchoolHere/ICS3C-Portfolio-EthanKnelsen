age = int(input("Enter your age: "))


parental_permission = input("Do you have parental permission? (yes/no): ")


if age >= 18 or parental_permission == "yes":  
    print("You can watch the movie")
else:
    print("You cannot watch the movie")
