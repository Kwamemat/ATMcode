#This is the dictionary that holds user information
userDetails = {'kojo': 
                {'pin':'0000', 
                'balance' : {'GHS' : 6000000,
                             'USD' : 1000000}}}

#This variable is set to false by default but changed to true when a user is validated for a session
is_logged_in = False

username = None

currency = None


#This function is called to verify user credentials and returns a boolean value 
#depending on the validity of credentials entered
def user_is_valid(username, pin):
    if username in userDetails:
        if pin == userDetails[username]['pin']:
            return True

    return False

#This function collects user credentials and validates the session or recalls itself
def login():

    #The global keyword enables global variables to be changed at runtime
    global username
    global is_logged_in

    username = input("Please type your username\n")
    pin = input("Please enter your pin\n")
    
    if(user_is_valid(username, pin)):
        is_logged_in = True

    else:
        print("Credentials not valid.\n" +
        'Please try again')
        login()

#This function allows users to withdraw money from their accounts depending on their account balance
def withdraw_money(username):

    amount = int(input(f"How much in {get_currency()} would you like to withdraw?\n"))

    balance = userDetails[username]['balance'][get_currency()]
    
    

    if(balance - amount < 0):
        print("Your account balance is not sufficient to complete this transaction")

    else:
        userDetails[username]['balance'][get_currency()] = balance - amount
        print(f"You have successfully withdrawn {amount} {get_currency()}" +
        f"\nYour remaining balance is {get_balance(username, get_currency())} {get_currency()}")

def get_balance(username, currency):

    return userDetails[username]['balance'][get_currency()]

def set_currency():
    account = input("Would you like to access your GHS or USD account?\n" +
    "1.GHS account \n2.USD account\n")

    global currency

    if(account == '1'):
        currency = 'GHS'
    elif(account == '2'): 
        currency = 'USD'
    else:
        set_currency()

def get_currency():
    return currency


def welcome_user(username):
    print(f"Hello {username}")

    set_currency()

    print("What would you like today?\n")
    
    answer = input("1.Withdraw Money" +
                    "\n2.Check Your Balance\n")
    if(answer == '1'):
        withdraw_money(username)
    else:
        print(f"You have {get_balance(username, get_currency())} {get_currency()} in your account")
    




#This is the begining of the application where a user is asked to enter their credentials
print("Welcome to the Resolute Bank" + 
    "\nPlease enter your username and pin to log in")

while(is_logged_in == False):
    login()


welcome_user(username)
input("Enter any key to exit.")         ### To prevent the executable from closing immediately after execution, unless user is done








    

    


            

