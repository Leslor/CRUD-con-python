import sys

clients=['pablo','ricardo']


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name) 
    else:
        print('Client alredy is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx, client))


def update_client(client_name, update_name):
    global clients
    if client_name in clients:
        index=clients.index(client_name)
        clients[index]=update_name
    else:
        print('Client not in client\'s list')

def delete_client(cliente_name):
    global clients
    if client_name in clients:
        clients.remove(cliente_name)
    else:
        print('Client not in client\'s list')

def search_client(client_name):
    for client in clients:
        if client!=client_name:
            continue
        else: 
            return True

def _get_client_name():
    client_name=None
    while not client_name:
        client_name=input('What is the client name? ')
        if client_name=="exit":
            client_name=None
            break
        
    if not client_name:
            sys.exit() 
    
    return client_name
       

def _print_welcome():
    print('WELCOME TO #### VENTAS')
    print('*'*50)
    print("""What would you like to do?
             [C]reate client
             [R]emove client
             [U] client
             [D]elete client""")

    
if __name__=='__main__':
    _print_welcome()

    command=input().upper()
    
    
    if command=='C':
        client_name=_get_client_name()
        create_client(client_name)
        list_clients()

    elif command=='L':
        list_clients()
    
    elif command=='U':
        client_name=_get_client_name()
        update_client=input('What is the new client name?')
        update_client(client_name, update_client)
        list_clients()

    elif command=='D':
        client_name=_get_client_name()
        delete_client(client_name)
        list_clients()

    elif command=='S':
        client_name=_get_client_name()
        found=search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')


    
    
  