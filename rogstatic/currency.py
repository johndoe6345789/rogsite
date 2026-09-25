
def yen_dollar(num):
    '''
    (int)  -> float    
    Convert yen to dollar, format answer
    to give dollars and cents.
    >>> yen_dollar(6o)
    >>> 0.77
    '''
    num = num * 0.01276
    return "%0.2f"% num

def dollar_yen(num):
    '''
    (float)  -> int    
    Convert dollar to yen, format answer
    to give int.     
    >>> dollar_yen(6o)
    >>> 4703
    '''
    num = num * 78.39497
    return int(num)

def dollar_euro( num):
    '''
    (float)  -> float   
    Convert dollar to euro, format answer
    to give euro and cents.     
    >>> dollar_euro(6o)
    >>> 46.40
    '''
    num = num * 0.77340
    return "%0.2f"% num

def euro_dollar(num):
    '''
    (float)  -> float    
    Convert euro to dollar, format answer
    to give euro and cents.     
    >>> euro_dollar(6o)
    >>> 77.51
    '''
    num = num * 1.2918
    return "%0.2f"% num

def euro_yen(num):
    '''
    (float)  -> int    
    Convert euro to yen, format answer
    to give int.     
    >>> euro_yen(6o)
    >>> 6076
    '''
    num = num * 101.26
    return int( num )

def yen_euro(num):
    '''
    (float)  -> float    
    Convert yen to euro, format answer
    to give euros and cents.     
    >>> yen_euro(6o)
    >>> 0.59
    '''
    num = num * 0.00987
    return "%0.2f"% num 

def currency_to_convert(cash):
    while True:
        cash = input("Which to convert? euro, dollar, yen.")
        if cash not in ("euro","dollar" ,"yen"):
            print("Error, try again!")            
            continue
        return cash
    
def pile_of_cash(amount):
     while True:    
         amount = input("Amount to convert? ")
         if str.isalpha(amount) == True:
             print("Error, try again!")            
             continue
         return amount
     
def to_convert_to(exchange):
    while True:
        exchange = input("Currency required? euro, dollar, yen.")
        if exchange  not in ("euro","dollar" ,"yen"):
            print("Error, try again!")            
            continue
        return exchange
               

# while true, continue, to allow repeat conversions.

cash = 0
amount = 0
exchange = 0

while True:
        currency = currency_to_convert(cash)
        
        amount = pile_of_cash(amount)
       
        exchange = to_convert_to(exchange)
          
         
                
        
        amount = float(amount)
                        
        if currency == "euro" and exchange == "dollar":
            output = euro_dollar(amount)
        elif currency == "euro" and exchange == "yen":
            output = euro_yen(amount)
        elif currency == "dollar" and exchange == "euro":
            output = dollar_euro(amount)
        elif currency == "dollar" and exchange == "yen":
            output = dollar_yen(amount)
        elif currency == "yen" and exchange == "dollar":
            output = yen_dollar(amount)
        elif currency == "yen" and exchange == "euro":
            output = yen_euro(amount)
                        
                        
        print(output) 
                        
                    
                        
        y = input("You want to run again? (y/n) ")
                        
        if y == 'y':
            continue
        else:
            print ("OK, then we exit")
            exit()
            
        
        