def fibonacci_series_list_generator(n):
    fibo_series = []
    a=-1
    b=1
    for i in range(0,n):
        c=a+b
        fibo_series.append(c)
        a=b
        b=c
        
    return fibo_series


fibonacci_series_list_generator(6)