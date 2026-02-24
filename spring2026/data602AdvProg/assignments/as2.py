#Q1

numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])

#Q2

sales = []

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    amount = float(input(f"Enter sales for {day}: "))
    sales.append(amount)


total_sales = 0
for amount in sales:
    total_sales += amount


print(f"\nTotal sales for the week: ${total_sales:.2f}")


#Q3

places = ["Tokyo", "Brazil", "Iceland", "Canada", "Greece"]

print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

#Q4

rooms = {
    "CS101": "Room 3004",
    "CS102": "Room 4501",
    "CS103": "Room 6755",
    "NT110": "Room 1244",
    "CM241": "Room 1411"
}

instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

meeting_times = {
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m."
}

course = input("Enter a course number: ").upper()

if course in rooms:
    print("Room Number:", rooms[course])
    print("Instructor:", instructors[course])
    print("Meeting Time:", meeting_times[course])
else:
    print("Course not found.")


#Q5

contacts = {
    "Kevin": "kevin@email.com",
    "Maria": "maria@email.com",
    "James": "james@email.com"
}

while True:
    print("\n1. Look up email")
    print("2. Add new contact")
    print("3. Change email")
    print("4. Delete contact")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter the name: ")
        if name in contacts:
            print("Email:", contacts[name])
        else:
            print("Name not found.")

    elif choice == "2":
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        contacts[name] = email
        print("Contact added.")

    elif choice == "3":
        name = input("Enter the name: ")
        if name in contacts:
            email = input("Enter the new email: ")
            contacts[name] = email
            print("Email updated.")
        else:
            print("Name not found.")

    elif choice == "4":
        name = input("Enter the name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Name not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
