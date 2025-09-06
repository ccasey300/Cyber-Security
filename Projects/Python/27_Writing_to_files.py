# program to append to files
# 27/01/23
employee_file = open("Employees.txt", "a")  # "w" overrides everything in file...
employee_file.write("\nDylan - Caretaker")  # adds Dylan at the end of our file...
'''for employee in employee_file.readlines():
    print(employee) '''
''' employee_file = open("NewEmployees.txt", "w") 
employee_file.write("\nKelly - Customer Service") '''  # writes a new file with title "NewEmployees"
employee_file = open("index.html", "w")
employee_file.write("<p>Some HTML Code<p>")  # creates a html file and writes to it
employee_file.close()
