import string

#App title
print("!! Welcome to Password Strength Checker !!")

#counter for score
score=0
has_upper=False
has_scar=False
has_num=False

#list to add suggestions
suggestions = []

#strings of special characters
special_char=string.punctuation

while True:
    password=input("Enter password: (minimum 8 characters): ")
    if len(password)<8:
        print("Password is too short! It must be at least 8 characters.\n")
    else:
        break

if len(password) >= 12:
    score += 2
elif len(password)>=8:
    score += 1
    suggestions.append("• Make your password at least 12 characters long")


#check if password contains any characters types, then switch it on
for i in password:
    if i.isupper():
        has_upper=True
    if i in special_char:
        has_scar=True
    if i.isdigit():
        has_num=True

#assigning scores based on character types or provide suggestion
if has_upper:
    score += 1
else:
    suggestions.append("• Include at least one uppercase letter (A-Z)")

if has_scar:
    score += 1
else:
    suggestions.append("• Include at least one special character (!@#$%)")

if has_num:
    score += 1
else:
    suggestions.append("• Include at least one number (0-9)")


#calculate and print scores
if score>=5:
    print("\nPassword strength is very strong")
elif score == 4:
    print("\nPassword strength is strong")
elif score == 3:
    print("\nPassword strength is Medium")
elif score == 2:
    print("\nPassword strength is weak")
else:
    print("\nPassword strength is  very weak")

#print out suggestions based on the password
if suggestions:
    print("\nSuggestions to improve your password:")
    for tip in suggestions:
        print(tip)