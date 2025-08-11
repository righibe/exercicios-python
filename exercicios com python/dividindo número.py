n = int(input('Me diga um número de 4 dígitos: '))

u = n % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10

print(f'''Esse número tem {u} unidades 
{d} dezenas  
{c} centenas 
{m} milhar''')
