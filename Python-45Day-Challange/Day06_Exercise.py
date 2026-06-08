"""
Python for Mammals - Day 6 Exercise File
Topic: Operators & Calculations

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Fix errors patiently. Errors are part of learning.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be comfortable using operators
for practical calculations used in reports, monitoring, capacity checks,
backup validation, and daily operational summaries.
"""

print("=" * 70)
print("DAY 6 EXERCISES - OPERATORS & CALCULATIONS")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: Basic Disk Space Calculation
# ---------------------------------------------------------------------

"""
Given:
total_disk = 500
used_disk = 375

TODO:
- Calculate free disk space
- Print total disk
- Print used disk
- Print free disk

Expected style:
Total Disk : 500 GB
Used Disk  : 375 GB
Free Disk  : 125 GB
"""

total_disk = 500
used_disk = 375

# Write your code below this line
print("Total Disk : ",total_disk)
print("Used  Disk : ",used_disk)
print("Free  Disk : ",total_disk-used_disk)



# ---------------------------------------------------------------------
# EXERCISE 2: Disk Usage Percentage
# ---------------------------------------------------------------------

"""
Given:
used_disk = 375
total_disk = 500

TODO:
- Calculate disk usage percentage
- Round the percentage to 2 decimal places
- Print the result

Formula:
(used_disk / total_disk) * 100
"""

used_disk = 375
total_disk = 500

# Write your code below this line

print("Disk Usage Percentage :",(used_disk/total_disk)*100)



# ---------------------------------------------------------------------
# EXERCISE 3: Backup Duration Calculator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Backup start hour
2. Backup end hour

TODO:
- Convert both inputs to integers
- Calculate backup duration
- Print the duration

Example:
Start hour: 1
End hour  : 5
Output    : Backup duration is 4 hours
"""

# Write your code below this line
print("\n\n")
strt_hr=input("Please Enter Backup Start Hour :")
end_hr=input("Please Enter Backup End   Hour :")

print("Start hour: ",int(strt_hr))
print("End hour  :",int(end_hr))
print("Output    : Backup duration is ",(int(end_hr)-int(strt_hr)),"hours")


# ---------------------------------------------------------------------
# EXERCISE 4: Daily Check Summary
# ---------------------------------------------------------------------

"""
Given:
passed_checks = 42
failed_checks = 8

TODO:
- Calculate total checks
- Calculate pass percentage
- Calculate fail percentage
- Print all values neatly

Use round() for percentages.
"""

passed_checks = 42
failed_checks = 8
total_checks=passed_checks+failed_checks

# Write your code below this line
print("\n\n")

print("total checks :",total_checks)
print("pass percentage :",(passed_checks/total_checks)*100)
print("fail percentage :",(failed_checks/total_checks)*100)

# ---------------------------------------------------------------------
# EXERCISE 5: Assignment Operator Counter
# ---------------------------------------------------------------------

"""
Start with:
incident_count = 0

TODO:
- Add 1 incident using +=
- Add 3 more incidents using +=
- Resolve 2 incidents using -=
- Print the final incident count

This simulates a simple daily incident counter.
"""

incident_count = 0
print("\n\n")

# Write your code below this line
print("Current Incident Count= ",incident_count)
incident_count+=1

print("After +1 incident Count= ",incident_count)
incident_count+=3

print("After +3 incident Count= ",incident_count)
incident_count-=2

print(" After Substract final incident count:",incident_count)

# ---------------------------------------------------------------------
# EXERCISE 6: Backup Success and Failure Counter
# ---------------------------------------------------------------------

"""
Given three backup statuses:
backup_1 = "SUCCESS"
backup_2 = "FAILED"
backup_3 = "SUCCESS"

TODO:
- Create successful_backups = 0
- Create failed_backups = 0
- Use if/else for each backup status
- Increase the correct counter using +=
- Print both counters

Use only concepts learned so far.
"""
print("\n\n")

backup_1 = "SUCCESS"
backup_2 = "FAILED"
backup_3 = "SUCCESS"

# Write your code below this line
successful_backups = 0
failed_backups = 0
if backup_1=="SUCCESS":
    successful_backups+=1
else:
    failed_backups+=1
    
if backup_2=="SUCCESS":
    successful_backups+=1
else:
    failed_backups+=1

if backup_3=="SUCCESS":
    successful_backups+=1
else:
    failed_backups+=1    

print("successful_backups= ",successful_backups)
print("failed_backups= ",failed_backups)

# ---------------------------------------------------------------------
# EXERCISE 7: Threshold Checker
# ---------------------------------------------------------------------

"""
Ask the user for current disk usage percentage.

TODO:
- Convert input to float
- If usage is greater than or equal to 90, print CRITICAL
- Else if usage is greater than or equal to 80, print WARNING
- Else print OK

Test with:
75
84
92
"""

# Write your code below this line
print("\n\n")
usage=input("Please enter disk usage percentage= ")
f_usage=float(usage)
if f_usage >= 90:
    print("CRITICAL")
elif f_usage >= 80:    
    print("WARNING")
else:
    print("OK")



# ---------------------------------------------------------------------
# EXERCISE 8: SLA Delay Calculator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Allowed duration in minutes
2. Actual duration in minutes

TODO:
- Convert both to integers
- If actual duration is greater than allowed duration:
    - Calculate delay
    - Print SLA BREACHED
    - Print delay in minutes
- Otherwise, print Within SLA
"""

# Write your code below this line
print("\n\n")
allow_min=input("Please Enter Allowed duration in minutes :")
actul_min=input("Please Enter Actual duration in minutes  :")
i_allow_min=int(allow_min)
i_actul_min=int(actul_min)

if i_actul_min > i_allow_min:
    print("SLA BREACHED ",i_actul_min-i_allow_min,"Min")
    
else: 
    print("Within SLA")



# ---------------------------------------------------------------------
# EXERCISE 9: Floor Division and Remainder
# ---------------------------------------------------------------------

"""
Given:
total_tasks = 23
engineers = 4

TODO:
- Calculate complete tasks per engineer using //
- Calculate remaining tasks using %
- Print both values

Expected idea:
Each engineer gets 5 complete tasks.
3 tasks remain.
"""

total_tasks = 23
engineers = 4

# Write your code below this line
print("\n\n")
print("complete tasks per engineer using= ",total_tasks//engineers)
print("remaining tasks using %= ",total_tasks%engineers)




# ---------------------------------------------------------------------
# EXERCISE 10: Operator Precedence Practice
# ---------------------------------------------------------------------

"""
Given:
a = 10
b = 5
c = 2

TODO:
- Calculate result_1 = a + b * c
- Calculate result_2 = (a + b) * c
- Print both results
- Observe the difference

This exercise teaches why brackets matter.
"""

a = 10
b = 5
c = 2

# Write your code below this line
print("\n\n")
print("Output of 'a + b * c' =",a + b * c)
print("Output of '(a + b) * c' =",(a + b) * c)


# ---------------------------------------------------------------------
# EXERCISE 11: Capacity Status Calculator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Resource name
2. Used value
3. Total value

TODO:
- Convert used and total values to float
- Calculate free value
- Calculate usage percentage
- Round usage percentage to 2 decimals
- Print a clean capacity report

Expected style:
Resource      : Disk /data
Used          : 780
Total         : 1000
Free          : 220
Usage Percent : 78.0 %
"""

# Write your code below this line
print("\n\n")

Resource_name=input("Please enter Resource: ")
Used_value=input("Please enter Used Value: ")
Total_value=input("Please enter Total Value: ")

Used_value=int(Used_value)
Total_value=int(Total_value)

print("Resource      : ",Resource_name)
print("Used          : ",Used_value)
print("Total         : ",Total_value)
print("Free          : ",(Total_value-Used_value))
print("Usage Percent : ",((Used_value)/Total_value)*100,"%")




# ---------------------------------------------------------------------
# EXERCISE 12: Capacity Status With Severity
# ---------------------------------------------------------------------

"""
Extend Exercise 11.

TODO:
- If usage percentage is >= 90, print CRITICAL
- Else if usage percentage is >= 80, print WARNING
- Else print OK

Test with:
Used 750, Total 1000 -> OK
Used 850, Total 1000 -> WARNING
Used 940, Total 1000 -> CRITICAL
"""

# Write your code below this line
print("\n\n")

if ((Used_value)/Total_value)*100 >=90:
    print("CRITICAL")
elif ((Used_value)/Total_value)*100 >=80:
    print("WARNING")
else:
    print("OK")

# ---------------------------------------------------------------------
# EXERCISE 13: Report Count Calculator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Number of successful reports
2. Number of failed reports
3. Number of pending reports

TODO:
- Calculate total reports
- Calculate success percentage
- Calculate failure percentage
- Print a report summary

Use round() for percentages.
"""

# Write your code below this line
print("\n\n")
successful=input("Number of successful reports= ")
failed=input("Number of failed reports= ")
pending=input("Number of pending reports= ")

i_successful=int(successful)
i_failed=int(failed)
i_pending=int(pending)
i_total=i_successful+i_failed+i_pending


print("total reports",i_total)
print("success percentage",((i_successful/i_total)*100))
print("failure percentage",((i_failed/i_total)*100))

# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Operational Calculator
# ---------------------------------------------------------------------

"""
Build a mini Operational Calculator.

Ask the user for:
1. Resource name
2. Used value
3. Total value
4. Warning threshold
5. Critical threshold

TODO:
- Clean the resource name
- Convert numeric inputs to float
- Calculate free value
- Calculate usage percentage
- Compare usage percentage with thresholds
- Print a clean report

Expected output style:
========================================
Operational Calculator Report
========================================
Resource       : Disk /backup
Used           : 450.0
Total          : 500.0
Free           : 50.0
Usage Percent  : 90.0 %
Status         : CRITICAL
========================================

Important:
Use only the concepts learned so far:
- input()
- variables
- strings
- strip()
- int()
- float()
- arithmetic operators
- assignment operators
- comparison operators
- if / elif / else
- print()
"""

print("\n\n")
# Write your mini project code below this line
print("="*80)
print("Operational Calculator Report")
print("="*80)
print("Resource       : Disk ",Resource_name)
print("Used           : ",Used_value)
print("Total          : ",Total_value)
print("Free           : ",(Total_value-Used_value))
print("Usage Percent  : ",((Used_value)/Total_value)*100,"%")
if ((Used_value)/Total_value)*100 >=90:
    print("Status         : CRITICAL")
elif ((Used_value)/Total_value)*100 >=80:
    print("Status         : WARNING")
else:
    print("Status         : OK")





print("\nExercise file loaded successfully. Complete the tasks one by one.")
