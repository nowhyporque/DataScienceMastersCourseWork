
#Q1

meal = input("Enter a meal (breakfast, lunch, or dinner): ")

if meal == "breakfast":
    print("How about some bacon and eggs?")
elif meal == "lunch":
    print("maybe a burger!")
elif meal == "dinner":
    print("you have to get steak!")
else:
    print("Sorry, I only have suggestions for breakfast, lunch, or dinner.")



#Q2


hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly pay rate: "))

if hours > 20:
    overtime = hours - 20
    gross_pay = (20 * rate) + (overtime * rate * 1.5)
else:
    gross_pay = hours * rate

print("Gross pay: $", format(gross_pay, ".2f"))


#Q3


def times_ten(number):
    print(number * 10)

# Example call
times_ten(5)   # Output: 50


#Q4


def main():
    calories1 = float(input("How many calories are in the first food? "))
    calories2 = float(input("How many calories are in the second food? "))
    showCalories(calories1, calories2)

def showCalories(calories1, calories2):
    total = calories1 + calories2
    print("The total calories you ate today:", format(total, ".2f"))

main()


#Q5


total = 0

for i in range(1, 31):
    total += i / (31 - i)

print("Total:", total)


#Q6



def triangle_area(base, height):
    area = 0.5 * base * height
    print(area)

# Example
triangle_area(5, 4)   # Output: 10.0
