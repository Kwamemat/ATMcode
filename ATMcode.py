#This is the dictionary that holds user information
userDetails = {'kojo': 
                {'pin':'1234', 
                'balance' : {'GHS' : 6000000,
                             'USD' : 1000000}},
                'kofi': 
                {'pin':'1655', 
                'balance' : {'GHS' : 1350000,
                             'USD' : 9056000}},
                'kwabena': 
                {'pin':'0480', 
                'balance' : {'GHS' : 9876700,
                             'USD' : 1986600}},
                'matrevi': 
                {'pin':'1306', 
                'balance' : {'GHS' : 8797800,
                             'USD' : 5630000}},
               'justin':
               {'pin':'8743', 
                'balance' : {'GHS' : 3423000,
                             'USD' : 1096600}}
               }

#This variable is set to false by default but changed to true when a user is validated for a session
is_logged_in = False

username = None

currency = None



