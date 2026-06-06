"""
Day 2 Homework Exercises
Topic: Comments, print(), arithmetic, variables, assignment, data types, and type()

How to use:
    1. Run this file once: python Day2_exercise.py
    2. Complete each TODO section.
    3. Do not use if-else, loops, functions, or lists yet.
    4. Keep your variable names meaningful.

Challenge rule:
    Use only Day 2 concepts unless a bonus task asks otherwise.
"""

print("=" * 60)
print("DAY 2 HOMEWORK: PYTHON BASICS")
print("=" * 60)
print()


# ============================================================
# EXERCISE 1: PERSONAL INTRO CARD
# ============================================================

print("Exercise 1: Personal Intro Card")

# TODO:
# Create variables for your name, city, favorite_food, hobby, and current_year.
# Print them in a clean intro-card style.
# Also print the type of at least two variables.


# Example output idea:
# Name: Riya
# City: Pune
# Favorite Food: Dosa
# Hobby: Sketching
# Current Year: 2026
# Type of name: <class 'str'>

# Write your code below this line:
name="Naresh"
city="Delhi"
favorite_food="Rice"
hobby="Football"
current_year=2026

print(f"Hello My Name is {name}, i live in {city} in Year {current_year}, My Fav Food is {favorite_food} and food is {hobby} ")
print()  # keep this blank line


# ============================================================
# EXERCISE 2: CAFE BILL CALCULATOR
# ============================================================

print("Exercise 2: Cafe Bill Calculator")

# TODO:
# Imagine you visited a cafe.
# Create variables for three items and their prices.
# Example: coffee_price, sandwich_price, brownie_price
# Create quantity variables for each item.
# Calculate:
#   1. subtotal
#   2. service_charge at 5% of subtotal
#   3. total_bill
# Print a readable bill.

# Hint:
# service_charge = subtotal * 0.05

# Write your code below this line:

coffee_price=120
sandwich_price=80
brownie_price=50

print (f"Your Subtotal is:",coffee_price+sandwich_price+brownie_price)
print (f"Service Charge on bill is :",0.05*(coffee_price+sandwich_price+brownie_price))
print (f"Total bill is :",(0.05*(coffee_price+sandwich_price+brownie_price))+((coffee_price+sandwich_price+brownie_price)))
print()


# ============================================================
# EXERCISE 3: MOVIE NIGHT SPLIT
# ============================================================

print("Exercise 3: Movie Night Split")

# TODO:
# You and your friends are planning a movie night.
# Create variables for:
#   movie_name
#   ticket_price
#   number_of_people
#   snacks_total
# Calculate:
#   tickets_total
#   grand_total
#   amount_per_person
# Print a simple summary.

# Expected learning:
# multiplication, addition, division, variables, print()

# Write your code below this line:
movie_name="Dhurandhar"
ticket_price=450
number_of_people=2
snacks_total=500
# Calculate:
#   tickets_total
#   grand_total
#   amount_per_person
# Print a simple summary.

print(f"tickets_total price for {movie_name} is: ", ticket_price*number_of_people)
print("including snack grand total is: ",(ticket_price*number_of_people)+snacks_total)
print("amount_per_person is: ",((ticket_price*number_of_people)+snacks_total)/2)
print()


# ============================================================
# EXERCISE 4: TIME CONVERTER
# ============================================================

print("Exercise 4: Time Converter")

# TODO:
# Create a variable total_minutes.
# Convert it into hours and remaining minutes.
# Example:
#   total_minutes = 135
#   hours = 135 // 60       # 2
#   minutes = 135 % 60      # 15
# Print the result as: 135 minutes = 2 hours and 15 minutes

# Try with 95, 135, and 250 minutes.

# Write your code below this line:
total_minutes=95
print(f"{total_minutes} minutes converted to hour is:", total_minutes//60 ,"Hrs and ", total_minutes%60 ,"Sec")

total_minutes=135
print(f"{total_minutes} minutes converted to hour is:", total_minutes//60 ,"Hrs and ", total_minutes%60 ,"Sec")

total_minutes=250
print(f"{total_minutes} minutes converted to hour is:", total_minutes//60 ,"Hrs and ", total_minutes%60 ,"Sec")

print()


# ============================================================
# EXERCISE 5: TYPE DETECTIVE
# ============================================================

print("Exercise 5: Type Detective")

# TODO:
# Create one variable each for:
#   string
#   integer
#   float
#   boolean
#   None
# Print value and type for each variable.

# Bonus thought:
# What is the difference between 100 and "100"?

# Write your code below this line:
tring="Python"
nteger=3
loat=3.18
oolean=True
one=None

print(f"I have installed {tring}","which is type ",type(tring))
print(f"Those major Version is {nteger} which is ",type(nteger))
print(f"And Full Version is {loat} which is ",type(loat))
print(f"Are you interested {oolean} which is ",type(oolean))
print(f"Do you have any Project {one} which is ",type(one))

print()


# ============================================================
# EXERCISE 6: FIX THE BROKEN CODE
# ============================================================

print("Exercise 6: Fix The Broken Code")

# TODO:
# The code below has mistakes. Do not delete the idea, fix it.
# Uncomment the lines, correct them, and make the final bill print properly.

item = "Wireless Mouse"
price = "799"
quantity = 2
total = int(price) * quantity
print(f"Total price for {quantity} {item} is ",total)

# Expected final meaning:
# Total price for 2 Wireless Mouse is 1598

# Write fixed code below this line:


print()


# ============================================================
# EXERCISE 7: MINI PROJECT - SIMPLE FITNESS SNAPSHOT
# ============================================================

print("Exercise 7: Mini Project - Simple Fitness Snapshot")

# TODO:
# Create variables for:
#   person_name
#   steps_walked_today
#   average_step_length_meter
#   water_glasses
#
# Calculate:
#   distance_meter = steps_walked_today * average_step_length_meter
#   distance_km = distance_meter / 1000
#
# Print a neat daily snapshot.
# Also print type of distance_km.

# Example output idea:
# Daily Fitness Snapshot
# Name: Meera
# Steps: 8500
# Distance Walked: 5.95 km
# Water Glasses: 8
# Type of distance_km: <class 'float'>

# Write your code below this line:
person_name="Hamza"
steps_walked_today=1200
average_step_length_meter=3
water_glasses=20

distance_meter = steps_walked_today * average_step_length_meter
distance_km = distance_meter / 1000

#Print a neat daily snapshot.
print("Daily Fitness Snapshot")
print(f"Name: ",person_name)
print(f"Steps: ",steps_walked_today)
print(f"Distance Walked: {distance_km} km")
print(f"Water Glasses: ",water_glasses)
print(f"Type of distance_km: ", type(distance_km))

#Also print type of distance_km.


print()


# ============================================================
# BONUS CHALLENGE: RECEIPT DESIGN
# ============================================================

print("Bonus Challenge: Receipt Design")

# TODO:
# Create a beautiful text receipt using print(), variables, and arithmetic.
# Use symbols like -, =, *, and spacing to make it readable.
# You can choose any theme: bookstore, gaming cafe, tea stall, art supplies, etc.

# Conditions:
#   - Minimum 5 variables
#   - At least 3 arithmetic operations
#   - At least 3 type() checks
#   - At least 1 useful comment explaining your logic

# Write your code below this line:
print("=" * 60)
print("Gaming Cafe Bill ")
print("=" * 60)

name="Rahman"
V3="Kanpur"
Game="Counter Strike"
TimeSpendHr=2
PerHrCharge=10

print("Hello", name," you Name type is ",type(name))
print("You have played:",Game)
print("You have spend total:",TimeSpendHr,"Hr","which is ",type(TimeSpendHr))
print()  # prints a blank line


print()
print("Homework file completed. Run, fix, improve, and share your output screenshot!")
