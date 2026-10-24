import os

def clear_screen():
    # Clears the terminal screen for Windows, Mac, or Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# Step 1: User creates their own password
print("--- SETUP MODE ---")
created_password = input("Create your new password: ")
clear_screen()  # Instantly hides the password they just made

# Step 2: User must enter the password they just created
print("--- LOCK SCREEN ---")
entered_password = input("Enter Password to unlock: ")

# Step 3: Check if it matches
if entered_password == created_password:
    clear_screen()  # Makes the password screen disappear
    
    # Step 4: Access granted to type anything
    print("Access Granted!")
    print("-" * 20)
    free_typing = input("Type anything you want here: \n")
    
else:
    print("Wrong password! Access Denied.")
