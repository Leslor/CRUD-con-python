import csv
import os


CLIENT_SCHEMA=['name', 'company', 'email','position','description']
CLIENT_TABLE='.clients.csv.'
clients=[]
PASSWORD='12345'

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client) 
    else:
        print('Client alredy is in the client\'s list')


def list_clients():
    print('uid|name|company|email|position|description')
    print('*'*50)

    for idx, client in enumerate(clients):
        print('{uid}|{name}|{company}|{email}|{position}|{description}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],
            description=client['description']))


def update_client(client_id, update_client):
    global clients
    if len(clients) -1>=client_id:
        clients[client_id]=update_client
    else:
        print('Client not in client\'s list')


def delete_client(cliente_id):
    global clients
    for idx, client in enumerate(clients):
        if idx==client_id :
            del clients[idx]
            break

def search_client(client_name):
    for client in clients:
        if client['name']!=client_name:
            continue
        else: 
            return True

def _get_client_field(field_name, message='What is the client {}?'):
    field=None

    while not field:
        field=input(message.format(field_name))
    return field


def _get_client_from_user():
    client={
        'name':_get_client_field('name'),
        'company':_get_client_field('company'),
        'email':_get_client_field('email'),
        'position':_get_client_field('position'),
        'description':_get_client_field('description')
                }    
    return client

def password_required(func):
    def wrapper():
        password=input('Ingrese contraseña: ')
        
        while not password or password !=PASSWORD:
                print('La contrasena no es correcta.')
                password=input('Ingrese contraseña: ')
        
        if password ==PASSWORD:
            return func()                   

    return wrapper


@password_required    
def needs_password():
    print('La contraseña es correcta')


def _print_welcome():
    print('WELCOME TO #### VENTAS')
    print('*'*50)
    print("""What would you like to do?
             [C]reate client
             [L]ist client
             [U] client
             [D]elete client
             [S]earch client""")


def _initialize_clients_form_storage():
    #context manayer para abrir el archivo
    with open(CLIENT_TABLE, mode='r') as f:
        reader=csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_client_to_storage():
    tmp_table_name='{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        write=csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        write.writerows(clients)
       
    os.remove(CLIENT_TABLE)
        
    os.rename(tmp_table_name, CLIENT_TABLE)

    
if __name__=='__main__':

    _initialize_clients_form_storage()
   
    needs_password()

    _print_welcome()

    command=input().upper()
    
    if command=='C':
        client=_get_client_from_user()        
        create_client(client)
      
    elif command=='L':
        list_clients()
    
    elif command=='U':
        client_id=int(_get_client_field('id'))
        updated_client=_get_client_from_user()
        update_client(client_id, updated_client)

    elif command=='D':
        client_id=int(_get_client_field('id'))
        delete_client(client_id)
     
    elif command=='S':
        client_name=_get_client_field('name')
        found=search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')


    _save_client_to_storage()
    
  