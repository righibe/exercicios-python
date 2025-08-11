import re
termos_proibidos = ['fuder', 'cu', 'bosta', 'merda', 'caralho', 'puta', 'viado', 'desgraça']

chat = input('chat:').lower()

texto_limpo = re.sub(r'[^a-zA-Z]', '', chat)

if any(palavra in texto_limpo for palavra in termos_proibidos):
    print(' Parece que você está violando os termos de serviço.')
else:
    print(' Você está dentro das normas.')

