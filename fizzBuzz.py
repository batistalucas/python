import re

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

n1, resp = input('Insira um número inteiro: '), ''

if is_int(n1):
    n1=int(n1)
    resp += 'Fizz' if n1 % 3 == 0 else ''
    resp += 'Buzz' if n1 % 5 == 0 else ''
    print(n1, resp)
else:
    print('Caracter inválido.')
