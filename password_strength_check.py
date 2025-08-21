# problem_18 Password Strength Checker

password = input("Enter password: ")

if password == "":
    pass  
else:
    has_digit = has_upper = has_lower = has_special = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif not ch.isalnum():  
            has_special = True

    if has_digit and has_upper and has_lower and has_special:
        print("Strong Password")
    else:
        print("Weak Password")
