def is_prime(n):
    flag = False
    if n > 1:
        for i in range(2,n):
            if (n%i)==0:
                flag = True
                break
    if flag:
        return False
    else:
        return True



is_prime(7)