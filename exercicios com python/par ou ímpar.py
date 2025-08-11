n = int(input('digite um número de quilometros da viagem'))
if n <= 200:
    valor1 = n * 0.50
    print(f'a viagem vai ser {valor1}')
else:
    valor2 = n * 0.45
    print(f'a viagem vai ser {valor2:.0f} reais')