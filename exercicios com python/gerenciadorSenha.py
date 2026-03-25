passwords = {}

while True:
    print("\n""1 - add a password")
    print("2 - show services")
    print("3 - get password")
    print("4 - delete password")
    print("5 - change password")
    print("6 - quit")

    choice = input("\n enter your choice: ")

    if choice == '1':
        service = input("\n enter your service: ")
        password = input("\n enter your password: ")
        passwords[service] = password
        print("password added.")

    elif choice == '2':
        if not passwords:
            print("\n no services entered")
        else:
            for key, value in passwords.items():
                print(key)

    elif choice == '3':
        if not passwords:
            print("\n no services entered")
        else:
            for key, value in passwords.items():
                print(key + "  ->  " + value)

    elif choice == '4':
        if not passwords:
            print("\n no services entered")
        else:
            delete = input("\n enter the service to delete: ")
            for key, value in passwords.items():
                print("service: " + key + "passowrd: " + value)
            removed = passwords.pop(delete , None)

    elif choice == '5':
        if not passwords:
            print("\n no services entered")
        else:
            for key, value in passwords.items():
                print("service: " + key )
            service_choice = input("write the service you want to change the password for: ")
            if service_choice in passwords:
                    passwords_verification = input("enter your current password:")
                    if passwords_verification != value:
                        print("\n password verification failed")
                    else:
                        new_password = input("enter your new password:")
                        new_password_2_step = input("enter your new password:")
                        if new_password == new_password_2_step:
                            passwords[service_choice] = new_password
                        else:
                            print("passwords do not match")

    elif choice == '6':
        print("\n goodbye")
        break

    else:
        print("Invalid option")