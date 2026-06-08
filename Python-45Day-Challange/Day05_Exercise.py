"""
Python for Mammals - Day 5 Exercise File
Topic: String Practice for Logs, Alerts, Emails, and File Names

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
By the end of these exercises, you should be comfortable using strings
for practical operational text processing.
"""

print("=" * 70)
print("DAY 5 EXERCISES - STRING PRACTICE")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: Clean a Raw Alert
# ---------------------------------------------------------------------

"""
Ask the user for an alert message.

TODO:
- Remove extra spaces using strip()
- Convert the alert to uppercase
- Print the original alert using repr()
- Print the cleaned alert
- Print the uppercase alert

Example input:
   warning disk usage high on server-01
"""

# Write your code below this line
print("\n\n")
alert_message=input("Please Enter Alert Message: ")
alert_message.strip().upper()
print("You have entered :",repr(alert_message))
print("Cleaned Alert Messages is :",alert_message.strip())
print("Alert Messages in Upper Letter is :",alert_message.strip().upper())





# ---------------------------------------------------------------------
# EXERCISE 2: Basic Log Severity Checker
# ---------------------------------------------------------------------

"""
Ask the user for one log line.

TODO:
- Normalize the log line to uppercase
- If it contains ERROR or FAILED, print CRITICAL
- Else if it contains WARNING, print WARNING
- Else if it contains SUCCESS, print OK
- Otherwise, print UNKNOWN
"""

# Write your code below this line
print("\n\n")
log_line=input("Please Enter one log line : ")
if "ERROR" in log_line.strip().upper() or "FAILED" in log_line.strip().upper(): 
    print("CRITICAL")
elif "WARNING" in log_line.strip().upper():
    print("WARNING")
elif "SUCCESS" in log_line.strip().upper():
    print("OK")    
else:
    print("UNKNOWN")


# ---------------------------------------------------------------------
# EXERCISE 3: Timeout Detector
# ---------------------------------------------------------------------

"""
Ask the user for an alert text.

TODO:
- Clean extra spaces
- Normalize case
- If the text contains TIMEOUT, print "Timeout issue found"
- Otherwise, print "No timeout keyword found"

Bonus:
Also detect "TIMED OUT".
"""

# Write your code below this line
print("\n\n")
alert_text=input("Please Enter an alert text : ")
if "TIMEOUT" in alert_text.strip().upper(): 
    print("Timeout issue found") 
else:
    print("No timeout keyword found")



# ---------------------------------------------------------------------
# EXERCISE 4: Email Subject Cleaner
# ---------------------------------------------------------------------

"""
Given this email subject:
email_subject = "  Subject: CRITICAL - Backup failed on db-server-01  "

TODO:
- Remove extra spaces
- Remove the word "Subject:"
- Remove extra spaces again
- Print the clean subject

Expected style:
CRITICAL - Backup failed on db-server-01
"""


# Write your code below this line
print("\n\n")
email_subject = "  Subject: CRITICAL - Backup failed on db-server-01  "
strip_email_subject=email_subject.strip()
pos=strip_email_subject.find("CRITICAL")
email_subject_without_kw=strip_email_subject[pos:]
print(email_subject_without_kw.strip())



# ---------------------------------------------------------------------
# EXERCISE 5: Email Priority Classifier
# ---------------------------------------------------------------------

"""
Ask the user for an email subject.

TODO:
- Clean the subject
- Normalize it to uppercase for checking
- If it contains CRITICAL, FAILED, or ERROR, print High Priority
- Else if it contains WARNING, print Medium Priority
- Else print Normal Priority
"""

# Write your code below this line
print("\n\n")
subject=input("Please Enter Email Subject: ")
sub_up=subject.upper()
if "CRITICAL" in sub_up or "FAILED" in sub_up or "ERROR" in sub_up:
    print("High Priority")
elif "WARNING" in sub_up :
    print("WARNING")
else:
    print("Normal Priority")
  

# ---------------------------------------------------------------------
# EXERCISE 6: Extract Sender and Subject
# ---------------------------------------------------------------------

"""
Given this email-like line:
email_line = "From: monitoring@company.com | Subject: ORA-01555 on prod-db-01"

TODO:
- Split the line using "|"
- Extract sender from the first part
- Extract subject from the second part
- Remove labels "From:" and "Subject:"
- Print sender and subject neatly

Expected style:
Sender  : monitoring@company.com
Subject : ORA-01555 on prod-db-01
"""

email_line = "From: monitoring@company.com | Subject: ORA-01555 on prod-db-01"

# Write your code below this line
sp_email=email_line.split("|")
fr_sq=sp_email[0].find("monitoring")
print("Sender  : ",sp_email[0][fr_sq:])
su_sq=sp_email[1].find("ORA")
print("Subject : ",sp_email[1][su_sq:])



# ---------------------------------------------------------------------
# EXERCISE 7: File Type Checker
# ---------------------------------------------------------------------

"""
Ask the user for a file name.

TODO:
- Clean extra spaces
- Convert to lowercase for checking
- If it ends with .log, print Log file
- Else if it ends with .csv, print CSV file
- Else if it ends with .txt, print Text file
- Otherwise, print Unsupported file type

Test with:
backup.log
report.CSV
notes.txt
image.png
"""

# Write your code below this line
filename=input("Please Enter File Name:")
newfile=filename.strip().lower()
if newfile.endswith(".log"):
    print("Log file")
elif newfile.endswith(".csv"):
    print("CSV file")
elif newfile.endswith(".txt"):
    print("Text file")    
else:
    print("Unsupported file type")


# ---------------------------------------------------------------------
# EXERCISE 8: Safe Report File Name Builder
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Environment name
2. Report title
3. Date in YYYYMMDD format

TODO:
- Clean all inputs
- Convert environment to lowercase
- Convert report title to lowercase
- Replace spaces in report title with underscores
- Create a file name in this format:
  environment_report_title_date.txt

Example:
Environment : PROD
Report title: Daily Alert Summary
Date        : 20260605
Output      : prod_daily_alert_summary_20260605.txt
"""

# Write your code below this line
print("\n\n")
env_name=input("Please Enter Enviorment Name :") 
l_env_name=env_name.strip()
rep_title=input("Please Enter Report title :")
l_rep_title=rep_title.lower()
new_rep_file=l_rep_title.replace(" ","_")
date=input("Please enter date in YYYYMMDD format: ")

print("Environment : ",l_env_name)
print("Report title: ",rep_title)
print("Date        : ",date)
print("Output      : ",new_rep_file+"_"+date+".txt")


# ---------------------------------------------------------------------
# EXERCISE 9: Backup File Name Parser
# ---------------------------------------------------------------------

"""
Given this file name:
file_name = "backup_prod_db01_20260605.log"

TODO:
- Remove .log from the file name
- Split the remaining text using "_"
- Extract:
  backup type
  environment
  server
  date
- Print all values neatly

Expected style:
Type        : backup
Environment : prod
Server      : db01
Date        : 20260605
"""

file_name = "backup_prod_db01_20260605.log"
print("\n\n")
# Write your code below this line
pos=file_name.find(".log")
new_file=file_name[:pos]
new_file_splt=new_file.split("_")
print("Type        : ",new_file_splt[0])
print("Environment : ",new_file_splt[1])
print("Server      : ",new_file_splt[2])
print("Date        : ",new_file_splt[3])


# ---------------------------------------------------------------------
# EXERCISE 10: ORA Pattern Detector
# ---------------------------------------------------------------------

"""
Ask the user for one log line.

TODO:
- Clean the line
- Convert it to uppercase for searching
- Check if it contains "ORA-"
- If yes, print "Oracle error found"
- Otherwise, print "No Oracle error found"

Test with:
ORA-00060 deadlock detected
backup completed successfully
job failed with ora-01555 snapshot too old
"""

# Write your code below this line
print("\n\n")
log_line=input("Please enter one log line: ")
if "ORA-" in log_line.upper():
    print("Oracle error found")
else:
    print("No Oracle error found")



# ---------------------------------------------------------------------
# EXERCISE 11: Extract ORA Code
# ---------------------------------------------------------------------

"""
Ask the user for one log line.

TODO:
- Find the position of "ORA-"
- If found, extract 9 characters starting from ORA-
- Print the ORA code
- If not found, print "No ORA code found"

Example:
Input : Job failed with ORA-01555 snapshot too old
Output: ORA-01555

Hint:
Use find() and slicing.
"""

# Write your code below this line
print("\n\n")
log_line=input("Please enter one log line: ")
pos=log_line.find("ORA-")
if pos==9:
    print(log_line[pos:9])
else:
    print("No ORA code found")




# ---------------------------------------------------------------------
# EXERCISE 12: Extract ORA Message
# ---------------------------------------------------------------------

"""
Ask the user for one log line.

TODO:
- Find the position of "ORA-"
- Extract ORA code using slicing
- Extract the text after the ORA code as the ORA message
- Print both values

Example:
Input:
Job failed with ORA-00060 deadlock detected while updating records

Expected style:
ORA Code    : ORA-00060
ORA Message : deadlock detected while updating records
"""

# Write your code below this line
print("\n\n")
log_line=input("Please enter one log line: ")
pos=log_line.find("ORA-")
print(log_line[pos:pos+9])
print(log_line[pos+9:])



# ---------------------------------------------------------------------
# EXERCISE 13: ORA Severity Mapper
# ---------------------------------------------------------------------

"""
Ask the user for an ORA code.

TODO:
- Clean and uppercase the ORA code
- If code is ORA-00060, print CRITICAL and "Possible deadlock"
- Else if code is ORA-01555, print WARNING and "Possible undo/snapshot issue"
- Else if code is ORA-00600, print CRITICAL and "Internal error"
- Otherwise, print UNKNOWN and "Check runbook/documentation"
"""

# Write your code below this line

print("\n\n")
u_ora_code=input("Please enter an ORA code: ")
if u_ora_code=="ORA-00060":
    print('CRITICAL and "Possible deadlock"')
elif  u_ora_code=="ORA-01555":    
    print('WARNING and "Possible undo/snapshot issue"')
elif  u_ora_code=="ORA-00600":    
    print('CRITICAL and "Internal error""')

# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - ORA Error Extractor
# ---------------------------------------------------------------------

"""
Build a mini ORA Error Extractor.

Ask the user for one log line or alert message.

TODO:
- Clean the input
- Normalize it for searching
- Find ORA-
- If ORA- is found:
  - Extract ORA code
  - Extract ORA message
  - Decide severity using these rules:
    ORA-00060 -> CRITICAL
    ORA-01555 -> WARNING
    ORA-00600 -> CRITICAL
    Any other ORA -> UNKNOWN
  - Print a clean report
- If ORA- is not found:
  - Print a clean report saying no ORA error was found

Expected output style:
========================================
ORA Error Extractor Report
========================================
Input Line  : Job failed with ORA-00060 deadlock detected
ORA Found   : Yes
ORA Code    : ORA-00060
ORA Message : deadlock detected
Severity    : CRITICAL
Hint        : Possible deadlock
========================================

Important:
Use only the concepts learned so far:
- input()
- variables
- strings
- strip()
- upper()
- replace()
- find()
- slicing
- if / elif / else
- print()
"""

# Write your mini project code below this line





print("\nExercise file loaded successfully. Complete the tasks one by one.")
