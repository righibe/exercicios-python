dl = float(input('quantos dias de aluguel?'))
kml = float(input('quantos km rodados'))

tdl = dl * 60

tkml = kml * (15 / 1000)

tp = tkml + tdl

print(' o valor a pagar e {} sendo {} de dias do aluguel e {:.2f} da distacia que vc andou'.format(tp, tdl, tkml))
