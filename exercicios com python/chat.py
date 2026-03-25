import os

mensagens = [] 

nome = input("Digite seu nome: ")

while True:
    
    os.system("cls")

    if len(mensagens) > 0:
        for mensagem in mensagens:
            print(f"{mensagem['nome']}: {mensagem['mensagem']}")

    print("---------------------------------------------------")
    
    mensagem = input("Digite sua mensagem (ou 'sair' para sair): ")
    
    if mensagem.lower() == "sair":
        break
    
    mensagens.append({
        "nome": nome,
        "mensagem": mensagem
        })
    