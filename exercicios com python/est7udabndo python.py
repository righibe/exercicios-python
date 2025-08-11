nome = input('qual seu nome?')
idade = int(input('qual a sua idade?'))
qi = int(input('qual seu qi?'))
altura = input('qual sua altura?')
if qi >= 100 and int(altura) >= 1.60:
    print('Parabéns seu cargo é de administrador, {} que tem {} anos, {} de altura e {} de QI'.format(nome, idade, altura , qi))
    print(f'Parabéns seu cargo é de administrador, {nome} que tem {idade} anos, {altura} de altura e {qi} de QI')
else:
    print('''parabéns seu cargo é trabalhador CLT, {} que tem {} anos, {} de altura e {} de
     =============================================
     //////////gravando sua imagem////////////////
     =============================================
     QI'''.format(nome, idade, altura , qi))