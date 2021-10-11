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
               {'pin':'5047'},
                'balance' : {'GHS' : 790665,
                             'USD' : 7989}},
                'gifty':
                'balance' : {'GHS' : 34212,
                             'USD' : 5702}},
                'exorm':
                'balance': {'GHS' : 323154,
                            'USD' : 3859}},
                'sampson':
                'balance': {'GHS' : 26322,
                            'USD' : 4387}},
                'georgina':
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
