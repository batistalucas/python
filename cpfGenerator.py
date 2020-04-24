from random import randint
cpf = str(randint(100000000, 999999999))

j = 10
mul = []

for i in cpf:
    i = int(i)
    mul.extend([i * j])
    j -= 1
penultimoDigito = 11 - (sum(mul) % 11)
if penultimoDigito > 9:
    penultimoDigito = 0

j = 11
mul = []
cpf += str(penultimoDigito)

for i in cpf:
    i = int(i)
    mul.extend([j * i])
    j -= 1
sum(mul)
ultimoDigito = 11 - (sum(mul) % 11)
if ultimoDigito > 9:
    ultimoDigito = 0
cpf += str(ultimoDigito)

print(f"CPF gerado: {cpf}.")
