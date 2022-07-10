import csv
import ast
import os
import configparser
import json
#['name', 'company', 'email','position','description']

config = configparser.ConfigParser()
config.read('cfig_file.ini')
#cp = ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
CLIENT_TABLE = config['FILE']['client_file']
print(CLIENT_TABLE)
PASSWORD = config['FILE']['password']
CLIENT_SCHEMA= list(config.get("HEADER","client_schema").split(','))
prueba=config.get("HEADER","client_schema")
print(prueba)
print(type(prueba))
clients=[]

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client) 
    else:
        print('El cliente se encuntra en la lista')
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
        print('El cliente no está en la lista')
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
    field = None
    while not field:
        field = input(message.format(field_name))
    return field

def _get_client_from_user():
    client={
        'name':_get_client_field('name').capitalize(),
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
                print('La contrasena no es correcta. Por favor, coloque la correcta')
                password=input('Ingrese contraseña: ')
        if password ==PASSWORD:
            return func()                   
    return wrapper

@password_required    
def needs_password():
    print('La contraseña es correcta')
def _print_welcome():
    print('WELCOME TO CLIENT REGISTRATION')
    print('*'*50)
    print("""What would you like to do?
             [C]reate client
             [L]ist client
             [U]pdate client
             [D]elete client
             [S]earch client""")

#Descerialization process with .csv
def _initialize_clients_form_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader=csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)
#Serialization
def _save_client_to_storage():
    global CLIENT_TABLE
    global CLIENT_SCHEMA
    with open(CLIENT_TABLE, 'a', encoding="utf-8") as f:
        write = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        write.writerows(clients)

if __name__=='__main__':  
    needs_password()
   # _initialize_clients_form_storage()
    _print_welcome()
    command=input().upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_id=int(_get_client_field('id'))
        updated_client=_get_client_from_user()
        update_client(client_id, updated_client)
    elif command=='D':
        client_id=int(_get_client_field('id'))
        delete_client(client_id)
    elif command=='S':
        client_name=_get_client_field('name').capitalize()
        found=search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
        
    _save_client_to_storage()
