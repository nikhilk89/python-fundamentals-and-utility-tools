import random
import string

#title
print("!! Welcome to Password Generator !!")

#asking element inputs from user for password
while True:
    try:
        pwd_len=int(input("Enter password length (minimum 8): "))
        if pwd_len <8:
            print("Password length must be atleast 8 characters!")
            continue
        break
    except ValueError: # if error during input
        print("Invalid input! Please enter numbers only.")


#function to solve incorrect user input
def YESorNO(input_param):
    while True:
        user_input=input(input_param).strip().lower()
        if user_input in ["y", "n"]:
            return user_input
        else:
            print("Invalid choice! Please enter 'y' for Yes or 'n' for No.\n")

#use function to take input
pwd_upcase=YESorNO("include uppercase? (y/n): ")
pwd_num=YESorNO("include numbers? (y/n): ")
pwd_sp_char=YESorNO("include special characters? (y/n): ")


#pool of characters to include all strings
char_pool=string.ascii_lowercase
pwd_pool=[] #list to contain password elements

#add all the elements to the pool if it is yes
#guarantee 1 of each element, adds to char pool
if pwd_upcase=="y":
    pwd_pool.append(random.choice(string.ascii_uppercase))
    char_pool += string.ascii_uppercase
if pwd_num=="y":
    pwd_pool.append(random.choice(string.digits))
    char_pool += string.digits
if pwd_sp_char=="y":
    pwd_pool.append(random.choice(string.punctuation))
    char_pool += string.punctuation

# counter for pwd length
pwd_len_count=pwd_len-len(pwd_pool)

# for remaining length of elements in pool, pick random elements  from char pool
for i in range(pwd_len_count):
    pwd_pool.append(random.choice(char_pool))

# Shuffle the pool so order changes!
random.shuffle(pwd_pool)

#create final password
final_pwd="".join(pwd_pool)
print(f"Your password is: {final_pwd}")



