def print_values(*args, **kwargs):  # *args valores posicionais (tupla), **kwargs valores nomeados (dict)
    print(args)
    print(kwargs)


def create_contact(*args):
    print("Enter the informations to register a contact!")
    info = {}
    for arg in args:
        info[arg] = input(f'Enter {arg}')

    return info


# def create_contact2():
#    name = input("Type the name: ")
#    email = input("Enter your email: ")
#    phone = input("Informe your phone number (xx) xxxxx-xxxx:\n")
#    return {
#        'name': name,
#        'email': email,
#        'phone': phone
#    }


def save_file(**kwargs):
    file = open('contatos.csv', 'a')  # w sobescreve // a continua a escrita
    file.write(','.join(kwargs.values()))
    file.flush()
    file.close()
    return "file update with success"


if __name__ == '__main__':
    # print_values('teste1', 'teste2', parameter='teste3')
    # name, email, phone = create_contact()
    informations = create_contact("name: ", "email: ")
    save_file(**informations)
