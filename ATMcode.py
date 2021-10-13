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

#This class describes the structure used to hold transactionary data
class Transaction():

    def __init__(self, username, transaction_type, amount, currency, recipient):
        self.username = username
        self.transaction_type = transaction_type
        self.amount = amount
        self.currency = currency
        self.recipient = recipient

        # dd/mm/YY H:M:S formats date in preferable style
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_username(self):
        return self.username
    
    def get_transaction_type(self):
        return self.transaction_type
    
    def get_amount(self):
        return self.amount
    
    def get_currency(self):
        return self.currency
    
    def get_recipient(self):
        return self.recipient

    def get_timestamp(self):
        return self.timestamp

            

#This variable is set to false by default but changed to true when a user is validated for a session
is_logged_in = False

username = None

currency = None

transactions = []


#This function is called to verify user credentials and returns a boolean value 
 #depending on the validity of credentials entered
def user_is_valid(username, pin):
    if username in userDetails:
        if pin == userDetails[username]['pin']:
            return True

    return False

#This function collects user credentials and validates the session or recalls itself
def login():

    #The global keyword enables global variables to be modified at runtime
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

    amount = int(input(f"How much would you like to deposit into your {get_currency()} account?\n "))

    if (amount <= 0):
        print(f"You cannot deposit 0 {get_currency()}")
    else:
        balance = userDetails[username]['balance'][get_currency()]
        newBalance = balance + amount
        userDetails[username]['balance'][get_currency()] = newBalance
        print(f"An amount of {amount} {get_currency()} has been deposited into your account" +
        f"\nYour new balance is {get_balance(username, get_currency())} {get_currency()}")

        transaction = Transaction(username, "Deposit", amount, get_currency(), username)
        transactions.append(transaction)

        answer = input("\nWould you like to make another transaction? \n1.Yes\n")

        if(answer == '1'):
            welcome_user(username)

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

        transaction = Transaction(username, "Withdrawal", amount, get_currency(), username)
        transactions.append(transaction)

        answer = input("\nWould you like to make another transaction? \n1.Yes\n")

        if(answer == '1'):
            welcome_user(username)

#This function enables the transfer of money between user accounts
#It recalls itself when the recipient is not found
def transfer_money(username):
    user = input("\nWho would you like to transfer money to?\n")

    if user not in userDetails:
        print(f"{user} is not in our records")
        transfer_money(username)
    else:
        amount = int(input("\nHow much would you like to transfer?\n"))
        balance = userDetails[username]['balance'][get_currency()]
        if (balance - amount) < 0:
            print("You do not have enough funds to complete this transaction\n")
        else:
            balance = balance - amount
            userDetails[username]['balance'][get_currency()] = balance
            userDetails[user]['balance'][get_currency()] += amount
            print(f"You have successfully transferred {amount} {get_currency()} to {user}")
            print(f"Your new balance is {get_balance(username, get_currency())}")

            transaction = Transaction(username, "Transfer", amount, get_currency(), user)
            transactions.append(transaction)

            answer = input("\nWould you like to make another transaction? \n1.Yes\n")

            if(answer == '1'):
                welcome_user(username)

def get_balance(username, currency):
    return userDetails[username]['balance'][currency]
    
    
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
 
    print("What would you like to do today?\n")
    
    answer = input("1. Withdraw Money" + "\n2. Deposit"
                    "\n3. Transfer Money" + "\n4. Check Balance\n")
    if(answer == '1'):
        withdraw_money(username)
    elif(answer == '2'):
        deposit(username)
    elif(answer == '3'):
        transfer_money(username)
    else:
        check_balance()

def check_balance():
    print(f"You have {get_balance(username, get_currency())} {get_currency()} in your account")    
    
    answer = input("\nWould you like to make another transaction? \n1.Yes\n")

    if(answer == '1'):
        welcome_user(username)


#This function takes a list of transactions and prints details of each transaction
def generate_receipt(transactions): 
    
    choice = str(input("Do you want a receipt? yes or no(y/n): "))
    if choice == 'y':

        
# creating a variable to hold a card number. this is a random 12 digit number
        card_number = random.random()
        card_number = card_number*10000
        card_number = round(card_number)
        card_number = str(card_number)

        for transaction in transactions:
            print(" ********************************************")
            print(f" * Date and time          {transaction.get_timestamp()}")
            print(" * Card number:            xxxxxxxxxx"+card_number)
            print(" * Accountname:            "+ transaction.get_username())
            print(" * Transaction:            "+ transaction.get_transaction_type())
            print(" ****************************************")
            print(" *                                 ")
            print(f" * Amount:                 {transaction.get_amount()} {transaction.get_currency()} ")
            print(f" * Recipient:              {transaction.get_recipient()}")
            print(f" * Balance:                {get_balance(username, transaction.get_currency())} {transaction.get_currency()}")
            print(" ********************************************")
        
        print("THANKS FOR CHOOSING RESOLUTE BANK")
    elif choice == "n":
        print("THANKS FOR CHOOSING RESOLUTE BANK")
    else:
        print("WRONG INPUT")
        
        
#This is the begining of the application where a user is asked to enter their credentials
print( "Welcome to the Resolute Bank" + 
    "\nPlease enter your username and pin to log in")

while(is_logged_in == False):
    login()


welcome_user(username)        
    


generate_receipt(transactions)
is_logged_in = False

input("Enter any key to exit.")    
#   ### To prevent the executable from closing immediately after execution, unless user is done