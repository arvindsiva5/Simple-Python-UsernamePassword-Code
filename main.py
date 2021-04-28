# Declare main() procedure
def main():
    global key
    userCredentials()
    key = userInput()
    display()

# Declare userCredentials() procedure
def userCredentials():
    global realUsername, realPassword
    # Declare variable realUsername
    realUsername = "arvind"
    # Declare variable realPassword
    realPassword = "1234"

# Declare userInput() function
def userInput():
    global realUsername, realPassword, username, password
    print("U only have 3 attempts")
    for i in range(3):
        username = input(str("Enter your username: "))
        password = input(str("Enter your password: "))
        if username != realUsername and password != realPassword:
            print("Incorrect Username & Password")
        elif username == realUsername and password != realPassword:
            print("Incorrect Password")
        elif username != realUsername and password == realPassword:
            print("Incorrect Username")
        else:
            return True
    print("U failed the 3 attempts")
    return False

# Declare display() procedure
def display():
    global key
    # Output on screen
    if key == False:
        # Output for wrong user credentials
        print("Application Locked – Ring the Network Manager for Assistance")
    else:
        # Output for correct user credentials
        print("Vault is opened")

# call main procedure
main()
