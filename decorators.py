
PASSWORD='12345'

def password_required(func):
    def wrapper():
        password=input('Ingrese contraseña: ')
        
        while not password or password !=PASSWORD:
            print('La contrasena no es correcta.')
            password=input('Ingrese contraseña: ')
        return password
        
        if password ==PASSWORD:
            return func()           

    return wrapper

@password_required    
def needs_password():
    print('La contraseña es correcta')


if __name__=='__main__':
    print(needs_password())

    