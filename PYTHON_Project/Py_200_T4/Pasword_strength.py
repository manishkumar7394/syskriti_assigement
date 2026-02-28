'''TaskPY200_T4: Write program to check password strength rules Input a string s (assume lowercase/uppercase/digits may appear)
Now check: if the string contains full fills all these and print final output: valid (STRONG) or Invalid password (WEAK) 
1. length >= 8 2. has at least 1 digit 3. has at least 1 uppercase 4. has at least 1 lowercase Print “STRONG” else “WEAK”'''


# Password Strength Checker

password = input("Enter your password: ")          #User enters a password and it is stored in the variable password.

# Rule checks
length_ok = len(password) >= 8              #len(password) counts the number of characters.It checks if length is at least 8
has_digit = False
has_upper = False
has_lower = False                       #We assume initially that password does NOT contain digit, uppercase, or lowercase.

for char in password:                   #We check every character one by one.	
    if char.isdigit():                  # checks if character is a number
        has_digit = True
    if char.isupper():              # checks if character is uppercase
        has_upper = True
    if char.islower():              #checks if character is lowercase
        has_lower = True
                                #If found, we change the corresponding variable to True.

# Final decision
if length_ok and has_digit and has_upper and has_lower:
    print("STRONG")
else:
    print("WEAK")           #If ALL conditions are true → print STRONG Otherwise → print WEAK

    
''' FOR EXAMPLE
    Input:
Hello123

Output:
STRONG ✅

Input:
hello

Output:
WEAK ❌ (no uppercase, no digit, length < 8)'''