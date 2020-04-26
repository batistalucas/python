for i in range(0,100):
    from random import randint
    n1, resp = randint(-100,100), ''

    resp += 'Fizz' if n1%3==0 else ''
    resp += 'Buzz' if n1%5==0 else ''

    print (n1,resp)