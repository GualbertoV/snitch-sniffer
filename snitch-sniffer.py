#Main() project
def bconvertd(val,base):
    #initializing variables
    if base<2 or base>36:
        return 'ERROR: base must be betwen 2 and 36'
    alphanum=''
    letter='A'
    for i in range(10):
        alphanum += str(i)
    for i in range(26):
        alphanum += letter
        letter=chr(ord(letter)+1)
    
    dec=0
    exp=1
    val=str(val)
    i=len(val)-1
    
    while i >= 0:
        dec+=int(alphanum.index(val[i]))*(exp)
        exp*=base
        i-=1
            
    return dec