while True:
    def fun1(n1):
        if n1%5==0 and n1%2==0:
            return 'FizzBuzz'
        elif n1%2==0:
            return 'Fizz'
        elif n1%5==0:
            return 'Buzz'
        else:
            return n1
    print(fun1(int(input("Qual o número: "))))