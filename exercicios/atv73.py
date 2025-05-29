brasileirao = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceará SC', 'Bahia',
               'Fluminense', 'Corinthians', 'Atlético-MG', 'Botafogo', 'São Paulo',
               'Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional', 'EC Vitória',
               'Grêmio', 'Juventude', 'Santos', 'Sport Recife')
print('-='*20)
print(f'Lista dos times do Brasileirão: {brasileirao}')

print('-='*20)
print(f'Os 5 primeiros times são {brasileirao[:5]}')

print('-='*20)
print(f'Os ultimos 4 são {brasileirao[-4:]}')

print('-='*20)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')

print('-='*20)
print(f'O time {brasileirao[8]} está na {brasileirao.index("Atlético-MG")+1}ª posição.')
