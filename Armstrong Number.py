ef is_armstrong(n):
    order = len(str(n))
    add = 0
    temp = n
    while temp>0:
        d = temp%10
        add +=d**order
        temp //=10;
    if n == add:
        return True
    else:
        return False

        
is_armstrong(371) 