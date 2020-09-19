
import crypt
import os
sentencia='12345'
PASSWORD=crypt.crypt(sentencia,'salt')
print(PASSWORD)

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


if __name__=='__main__':
    needs_password()