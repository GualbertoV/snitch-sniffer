#Main() project
from string import ascii_uppercase, digits

def bconvertd(val,base):
    #initializing variables
    if base<2 or base>36:
        return 'ERROR: base must be betwen 2 and 36'
    alphanum=digits+ascii_uppercase
    
    dec=0
    exp=1
    val=str(val).upper()
    
    i=len(val)-1
    while i >= 0:
        dec+=int(alphanum.index(val[i]))*(exp)
        exp*=base
        i-=1
            
    return dec