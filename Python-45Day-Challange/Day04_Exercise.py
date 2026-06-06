"""
Python for Mammals - Day 4 Exercise File
Topic: Strings

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
By the end of these exercises, you should be comfortable cleaning,
checking, formatting, and extracting useful information from text.
"""

print("=" * 70)
print("DAY 4 EXERCISES - STRINGS")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: Clean Introduction Text
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Name
2. Profession
3. City

The user may enter extra spaces.

TODO:
- Remove extra spaces using strip()
- Print name and city in title case
- Print profession in uppercase

Expected style:
Hello Aman!
Profession : DBA
City       : Delhi
"""

# Write your code below this line

Name=input("Please Enter Your Name with some spaces : ")
Profession=input("Please Enter Your Profession: ")
City=input("Please Enter Your City: ")

print("Hello ",Name.strip()+"!")
print("Profession : "+Profession)
print("City       : "+City)


# ---------------------------------------------------------------------
# EXERCISE 2: Backup Status Normalizer
# ---------------------------------------------------------------------

"""
Ask the user for backup status.

The user may enter:
success
 SUCCESS
Success
failed
 FAILED

TODO:
- Clean extra spaces
- Convert status to uppercase
- If status is SUCCESS, print "Backup completed successfully"
- If status is FAILED, print "Backup failed"
- Otherwise, print "Unknown backup status"
"""

# Write your code below this line
print("\n\n")
backup_status=input("Please Enter Your Backup Status with some extra Spaces : ")
if backup_status.strip().upper()=="SUCCESS":
    print("Backup completed successfully")
elif  backup_status.strip().upper()=="FAILED":    
    print("Backup failed")
else:
    print("Unknown backup status")
    
# ---------------------------------------------------------------------
# EXERCISE 3: File Extension Checker
# ---------------------------------------------------------------------

"""
Ask the user for a file name.

TODO:
- Clean extra spaces
- Check if the file ends with .log
- Check if the file ends with .csv
- Print a suitable message

Examples:
backup.log  -> Log file detected
report.csv  -> CSV report detected
notes.txt   -> Unsupported file type

Bonus:
Handle uppercase extensions like REPORT.CSV or ALERT.LOG.
"""

# Write your code below this line
print("\n\n")
file_name=input("Please Enter Your File Name with some extra spaces : ")
if file_name.strip().lower().endswith(".log") or file_name.strip().lower().endswith(".csv"):
    print("file Name you entered is ",file_name,",Which is valid file")
else:
    print("Not a valid file name entered")
    



# ---------------------------------------------------------------------
# EXERCISE 4: Server Naming Standard Checker
# ---------------------------------------------------------------------

"""
Ask the user for a server name.

Standard:
- Production server names should start with prod-
- Development server names should start with dev-
- Test server names should start with test-

TODO:
- Clean extra spaces
- Convert to lowercase
- Print the environment based on the prefix

Examples:
prod-db-01  -> Production server
dev-app-02  -> Development server
test-web-01 -> Test server
abc-01      -> Unknown naming standard
"""

# Write your code below this line
print("\n\n")
server_name=input("Please Enter Server Name:")
if server_name.strip().lower().startswith("prod-"):
    print("This is Prod Env")
elif server_name.strip().lower().startswith("dev-"):
    print("This is Dev Ent")
elif server_name.strip().lower().startswith("test-"):
    print("This is Test Env")





# ---------------------------------------------------------------------
# EXERCISE 5: Extract Environment from Server Name
# ---------------------------------------------------------------------

"""
Given this server name:
server_name = "prod-db-server-01"

TODO:
- Extract first 4 characters using slicing
- Extract last 2 characters using slicing
- Print both values

Expected output:
Environment Code : prod
Server Number    : 01
"""

server_name = "prod-db-server-01"

# Write your code below this line
print("\n\n")
print("Environment Code :",server_name[0:4])
print("Server Number    :",server_name[-2:])



# ---------------------------------------------------------------------
# EXERCISE 6: Alert Message Classifier
# ---------------------------------------------------------------------

"""
Ask the user for an alert message.

TODO:
- Clean extra spaces
- Convert it to uppercase
- If it contains ERROR or FAILED, print CRITICAL
- Else if it contains WARNING, print WARNING
- Else if it contains SUCCESS, print OK
- Otherwise, print UNKNOWN

Example:
"backup failed on server app-01" -> CRITICAL
"disk warning on server app-01"  -> WARNING
"backup success"                 -> OK
"job started"                    -> UNKNOWN
"""

# Write your code below this line
print("\n\n")
alert_message=input("Please enter Alert Message : ")
if "FAILED" in alert_message.strip().upper() or  "CRITICAL" in alert_message.strip().upper():
    print(alert_message.strip(),"->CRITICAL")
elif "WARNING" in alert_message.strip().upper():
    print(alert_message.strip(),"->WARNING")
elif "SUCCESS" in alert_message.strip().upper():
    print(alert_message.strip(),"->OK") 
else: 
    print(alert_message.strip(),"->UNKNOWN")
    

# ---------------------------------------------------------------------
# EXERCISE 7: Create a File-Friendly Name
# ---------------------------------------------------------------------

"""
Ask the user for a report title.

TODO:
- Clean extra spaces
- Convert to lowercase
- Replace spaces with underscores
- Add .txt at the end while printing

Example:
Input : Daily Backup Report
Output: daily_backup_report.txt
"""

# Write your code below this line
print("\n\n")
report_title=input("Please Enter Report Title: ")
print("Output : ",report_title.strip().lower().replace(" ","_")+".txt")


# ---------------------------------------------------------------------
# EXERCISE 8: Split a Simple Monitoring Line
# ---------------------------------------------------------------------

"""
Given this monitoring line:
line = "app-server-01 CPU 86 WARNING"

TODO:
- Split the line using split()
- Print server name
- Print metric name
- Print metric value
- Print status

Expected output:
Server : app-server-01
Metric : CPU
Value  : 86
Status : WARNING
"""

line = "app-server-01 CPU 86 WARNING"

# Write your code below this line
print("\n\n")
print("Server : ",line.split()[0])
print("Metric : ",line.split()[1])
print("Value  : ",line.split()[2])
print("Status : ",line.split()[3])



# ---------------------------------------------------------------------
# EXERCISE 9: Split a CSV-like Report Row
# ---------------------------------------------------------------------

"""
Given this CSV-like row:
row = "db-server-01,DISK,92,CRITICAL"

TODO:
- Split the row using comma as separator
- Store each part in a separate variable
- Print a clean report using f-strings

Expected style:
Server : db-server-01
Metric : DISK
Value  : 92%
Status : CRITICAL
"""

row = "db-server-01,DISK,92,CRITICAL"

print("\n\n")
# Write your code below this line
print("Server : ",row.split(",")[0])
print("Metric : ",row.split(",")[1])
print("Value  : ",row.split(",")[2]+"%")
print("Status : ",row.split(",")[3])




# ---------------------------------------------------------------------
# EXERCISE 10: Log Line Keyword Search
# ---------------------------------------------------------------------

"""
Ask the user for a log line.

TODO:
- Normalize the line to uppercase
- Check whether the log contains any of these words:
  ERROR
  ORA-
  FAILED
  TIMEOUT
  WARNING

Print a useful message based on what you find.

Example:
Input : ORA-00060 deadlock detected
Output: Oracle error found in log line

Input : connection timeout for app
Output: Timeout issue found
"""

# Write your code below this line
print("\n\n")
logline=input("Please Enter Log Line: ")
if "ERROR" in logline.upper() or "ORA-" in logline.upper() or "FAILED" in logline.upper() or "WARNING" in logline.upper() :
    print("Output: Oracle error found in log line")
elif "TIMEOUT" in logline.upper():
    print("Output: Timeout issue found")


# ---------------------------------------------------------------------
# EXERCISE 11: Username Validator
# ---------------------------------------------------------------------

"""
Ask the user for a username.

TODO:
- Remove extra spaces
- Check length using len()
- If username length is 0, print "Username cannot be empty"
- If username length is less than 5, print "Username too short"
- Otherwise, print "Username accepted"

Bonus:
Convert username to lowercase before printing final accepted username.
"""

# Write your code below this line
print("\n\n")
Name=input("Please Enter Username with space: ")
if len(Name.strip())==0:
    print("Username cannot be empty")
elif len(Name.strip())<5: 
    print("Username too short")
else:
    print("Username accepted")



# ---------------------------------------------------------------------
# EXERCISE 12: Mini Project - Daily Text Cleanup Assistant
# ---------------------------------------------------------------------

"""
Create a small text cleanup assistant.

Ask the user for:
1. Server name
2. Backup status
3. Log line
4. Report file name

TODO:
- Clean all inputs using strip()
- Normalize backup status using upper()
- Normalize log line for searching using upper()
- Check if report file name ends with .csv or .log
- Print a clean operational summary

Decision rules:
- If log line contains ERROR, FAILED, ORA-, or TIMEOUT, final status should be CRITICAL
- If log line contains WARNING, final status should be WARNING
- If backup status is FAILED, final status should be CRITICAL
- If backup status is SUCCESS and file name is valid, final status should be OK
- Otherwise, final status should be UNKNOWN

Expected output style:
========================================
Daily Text Cleanup Summary
========================================
Server Name   : app-server-01
Backup Status : SUCCESS
File Name     : daily_report.csv
File Type     : Valid report/log file
Final Status  : OK
Reason        : Backup success and file name looks valid
========================================

Important:
Focus on string cleaning and searching first.
Formatting can be improved after the logic works.
"""

# Write your mini project code below this line
print("\n\n")
Server_name=input("Please Enter Server Name : ").strip()
Backup_status=input("Please Enter Backup status : ").strip().upper()
Log_line=input("Please Enter Log line : ").strip().upper()
Report_file_name=input("Please Enter Report file name : ").strip()

print("="*50)
print("Daily Text Cleanup Summary")
print("="*50)
print("Server Name   :",Server_name)
print("Backup Status : ",Backup_status)

if Report_file_name.endswith(".log") or Report_file_name.endswith(".csv"):
 print("File Name     : ",Report_file_name)
 print("File Type     : Valid report/log file")
else:
 print("File Name     : ",Report_file_name)
 print("File Type     : Not Valid report/log file")    
 
if Backup_status=="FAILED":
 print("Final Status  : CRITICAL")
elif Backup_status=="SUCCESS":
 print("Final Status  : OK")
    
if  Backup_status=="SUCCESS" and (Report_file_name.endswith(".log") or Report_file_name.endswith(".csv")):
    print("Reason        : Backup success and file name looks valid")
else:
    print("Reason        : Backup Or file name Is Not Valid")
    
print("="*50)



print("\nExercise file loaded successfully. Complete the tasks one by one.")
