from datetime import datetime
import random
import math


#This is the dictionary that holds user information
userDetails = {'kojo': 
                {'pin':'1234', 
                'balance' : {'GHS' : 35190,
                             'USD' : 5865}},
                'kofi': 
                {'pin':'1655', 
                'balance' : {'GHS' : 39000,
                             'USD' : 6500}},
                'kwabena': 
                {'pin':'0480', 
                'balance' : {'GHS' : 20814,
                             'USD' : 3469}},
                'matrevi': 
                {'pin':'1306', 
                'balance' : {'GHS' : 26856,
                             'USD' : 4476}},
               'justin':
               {'pin':'8743', 
                'balance' : {'GHS' : 35196,
                             'USD' : 5866}},
               'fernanda':
               {'pin':'5047',
                'balance' : {'GHS' : 790665,
                             'USD' : 7989}},
                'gifty':
                {'pin' : '6060',
                'balance' : {'GHS' : 34212,
                             'USD' : 5702}},
                'exorm':
                {'pin' : '4658',
                'balance': {'GHS' : 323154,
                            'USD' : 3859}},
                'sampson':
                {'pin' : '9390',
                'balance': {'GHS' : 26322,
                            'USD' : 4387}},
                'georgina':
                {'pin' : '7793',
                'balance': {'GHS' : 31974,
                            'USD' : 5329}},
               }

            

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

#This function is for depositing money into your account
def deposit(username):
    amount = int(input(f"How much would you like to deposit into your {get_currency()} account? "))
    balance = userDetails[username]['balance'][get_currency()]
    newBalance = balance + amount
    if (amount <= 0):
        print("You cannot deposit 0")
    else:
        userDetails[username]['balance'][get_currency()] = newBalance
        print(f"An amount of {amount} {get_currency()} has been deposited into your account" +
        f"\nYour new balance is {get_balance(username, get_currency())} {get_currency()}")

 #This function allows users to withdraw money from their accounts depending on their account balance
def withdraw_money(username):
  
  global amt 
  amount = int(input(f"How much in {get_currency()} would you like to withdraw?\n"))
  amt = amount
  balance = userDetails[username]['balance'][get_currency()]
   
  if(balance - amount < 0):
    print("Your account balance is not sufficient to complete this transaction")
    amt = "insufficient funds"
  else:
    userDetails[username]['balance'][get_curency()] = balance - amount
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
    
    
    
    
    
    ##### Gifty's code goes into the space left above. She's to add only the get_curency method.
    
    
def welcome_user(username):
    print(f"Hello {username}")

    set_currency()
    global ww
    global amt
    print("What would you like today?\n")
    
    answer = input("1.Withdraw Money" +
                    "\n2.Check Your Balance\n")
    if(answer == '1'):
        ww = "withdrawal"
        withdraw_money(username)
    else:
        ww = "Balance enquiry"
        print(f"You have {get_balance(username, get_currency())} {get_currency()} in your account")    
        amt = "-----"
        
        
#This is the begining of the application where a user is asked to enter their credentials
print( "Welcome to the Resolute Bank" + 
    "\nPlease enter your username and pin to log in")

while(is_logged_in == False):
    login()


welcome_user(username)        
    
def receipt(): # a function to print out a receipt when the withdrawal and balance functions are performed
    today = datetime.now() # variable to get date and time from local machine

# dd/mm/YY H:M:S formats date in preferable style
    d1 = today.strftime("%d/%m/%Y %H:%M:%S")

    # creating a variable to hold a card number. this is a random 12 digit number
    n = random.random()
    n = n*10000
    n = round(n)
    n = str(n)

    
    print(" ********************************************")
    print(" * Date and time           ",d1)
    print(" * Card number:            xxxxxxxxxx"+n)
    print(" * Transaction:               "+ ww)
    print(" ****************************************")
    print(" *                                 ")
    print(f" * Dispensed Amt:         {amt} {get_currency()} ")
    print(f" * Requested Amt:         {amt} {get_currency()}")
    print(f" * Balance                {get_balance(username, get_currency())} {get_currency()}")
    print(" ********************************************")
    print(" *****THANKS FOR CHOOSING RESOLUTE BANK*****")

receipt()    

input("Enter any key to exit.")    
#   ### To prevent the executable from closing immediately after execution, unless user is done

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
