# program to create mock passports, investigating strings and fxns further
# 22/01/23
surname = input("Enter your surname: ")
forenames = input("Enter your forename: ")
nationality = input("Enter your nationality: ")
birth_date = input("Enter your DOB: ")
expiration_date = "22/02/1942"
passport_number = "SP1002426"
initials = forenames[0] + "." + surname[0] + "."
print("_________________________________________________")
print("|/####\\\n| 0 . 0\n| \\__/\n|")
print("|Surname: " + surname.upper() + "    Forenames: " + forenames.upper())
print("|Nationality: " + nationality.upper() + " \n|Date of Birth: " + birth_date + "\n|Date of Expiration: " + expiration_date + "                   ")
print("|Passport Number: \"SP1002426\"                     ")
print("|P>IRL" + surname.upper() + ">>>>>>>>>>" + forenames.upper() + ">>>>>>>>>>>>>>>>>>>>>>|")
print("|" + passport_number + ">>>>>>" + birth_date + ">>>>>>>>>>>>>>>>>>>>>>>>|")
print("|_________________________________________________|")
print("Forename & Surname length: ")
print(len(forenames))
print(len(surname))
print("Initials: " + initials)
print(surname.upper().isupper())
# makes surname UPPER CASE and verifies
print(surname.index("ase") + 1)
# passes parameter "ase" & returns STARTING index + 1 (where it is in surname. Note 0 is starting point.)
print(forenames + " " + surname.replace("Casey", "Rutkowski"))
# changes surname and prints
