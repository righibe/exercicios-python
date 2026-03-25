import os   

contacts = []



while True:
    print("1 - add contact")
    print("2 - list contacts")
    print("3 - delete contact")
    print("4 - search contact")
    print("5 - exit")
    print("----------------")

    opcao = input("Digite a opcao: ")

    if opcao == "1":
        name = input("Digite o nome do contato: ")

        exists = False
        for contact in contacts:
            if contact["name"] == name:
                exists = True
                break

        if exists:
            print("Contato ja existe, use outro nome")
            continue

        phone = input("Digite o telefone do contato: ")

        contacts.append({
            "name": name,
            "phone": phone
        })
        os.system("cls")
        print("Contato adicionado!")
   

    elif opcao == "2":
        for contact in contacts:
            print("----------------")
            print(f"{contact['name']}: {contact['phone']}")
            print("----------------")

    elif opcao == "3":

        search = input("Digite o nome do contato: ")

        found = False

        for contact in contacts:
            if contact['name'] == search:
                found = True
                if contact in contacts:
                    contacts.remove(contact)
                    os.system("cls")
                    print("Contato removido")
                    print("----------------")
                    break

        if not found:
            os.system("cls")
            print("Contato nao encontrado")

    elif opcao == "4":
        search = input("Digite o nome do contato: ")

        found = False

        for contact in contacts:
            if contact['name'] == search:
                found = True
                print(f"{contact['name']}: {contact['phone']}")
                
        if not found:
            os.system("cls")
            print("Contato nao encontrado")
        
    elif opcao == "5":
        os.system("cls")
        break

