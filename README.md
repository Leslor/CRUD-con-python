# :woman_technologist: CRUD Console
## Description
------------
CRUD is an acronym that comes from the world of computer programming and refers to the four functions that are considered necessary to implement a persistent storage application: create, read, update and delete.

### General
- How to create a CRUD programm with Python
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a CSV file
- How to manage datetime
- What is an UUID

### Tecnologies and libreries
------------

- Python3 (version 3.8.5)
- UUID modul
- configparser module 
- unittest module
- so module
- csv module
- Use of pycodestyle (version 2.8.*)


## More Info
------------
### Execution

```
$ ./console.py
WELCOME TO CLIENT REGISTRATION
**************************************************
What would you like to do?
             [C]reate client
			 [L]ist client
			 [U]pdate client
			 [D]elete client
			 [S]earch client


$
```
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Compilation & Output
----
The code will be executed this way:

``` $ ./console ```

- Any output must be printed on stdout

```
group_luis_leslie@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
	    print(obj)

		print("-- Create a new object --")
		my_model = BaseModel()
		my_model.name = "My_First_Model"
		my_model.my_number = 89
		my_model.save()
		print(my_model)
group_luis_leslie@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
group_luis_leslie@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
--
-- Create a new object --
	[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
group_luis_leslie@ubuntu:~/AirBnB$ cat file.json ; echo ""
		-- Create a new object --
		[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
group_luis_leslie@ubuntu:
		{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}

```



## Attributes by Class
---
All classes that inherit from `BaseModel`

1. Class User

	Public class attributes:
	- `email`: string - empty string
	- `password`: string - empty string
	- `first_name`: string - empty string
	- `last_name`: string - empty string
2. Class State

	Public class attributes:
	- `name`: string - empty string

3. Class Amenity

	Public class attributes:
	- `name`: string - empty string

4. Class Place

	Public class attributes:
	- `city_id`: string - empty string: it will be the City.id
	- `user_id`: string - empty string: it will be the User.id
	- `name`: string - empty string
	- `description`: string - empty string
	- `number_rooms`: integer - 0
	- `number_bathrooms`: integer - 0
	- `max_guest`: integer - 0
	- `price_by_night`: integer - 0
	- `latitude`: float - 0.0
	- `longitude`: float - 0.0
	- `amenity_ids`: list of string - empty list: it will be the list of Amenity.id later

5. Class Review

	Public class attributes:
	- `place_id`: string - empty string: it will be the Place.id
	- `user_id`: string - empty string: it will be the User.id
	- `text`: string - empty string

## Opcodes from Console
---
| Opcode | Description                    |
| ------------- | ------------------------------ |
| `quite`   | Quit command to exit the program     |
| `create`      | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id|
| `show`   | Show string representation of an instance based on the class name and id.  |
| `destroy`      | Deletes an instance based on the class name and id.|
| `all`   | Prints all string representation of all instances based or not on the classnam. |
| `update`      | Update an instance based on the class name and id by adding or updating attribute (save the change into the JSON file. |

## Examples to use the console.py
---
In this section the operation of the console will be shown
```
(hbnb)create User
db53f522-7d37-4f62-adb5-520ec7dbfaf4

(hbnb)create Place
5c7521b5-702c-4a4e-b67c-b7361dfb3cb0

(hbnb)create Place
b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9

(hbnb)create Place
[Place] (b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9) {'id': 'b8f45bdb-cf34-4ca7-a186-35bb9e7ddbe9', 'created_at': datetime.datetime(2022, 7, 1, 10, 23, 15, 8285), 'updated_at': datetime.datetime(2022, 7, 1, 10, 23, 15, 8293)}
[Place] (7c115662-fefa-417f-8183-2e146548a83f) {'id': '7c115662-fefa-417f-8183-2e146548a83f', 'created_at': datetime.datetime(2022, 7, 1, 10, 23, 17, 27311), 'updated_at': datetime.datetime(2022, 7, 1, 10, 23, 17, 27351)}
```
## Examples to use the console.py by class name
---

In this section, the operation of the console will be shown by calling each method with the respective class.

## How to use:
- Retrieve all instances of a class by using: `<class name>.all()`
- Retrieve the number of instances of a class: `<class name>.count()`
- Retrieve an instance based on its ID: `<class name>.show(<id>)`
- Destroy an instance based on his ID: `<class name>.destroy(<id>)`
- Update an instance based on his ID: `<class name>.update(<id>, <attribute name>, <attribute value>)`

```
(hbnb)create Place
e5954ba0-388a-40e4-809c-1e5a372a1c77

(hbnb)Place.update("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6", "amenity_ids", ["pool", "sauna", "karaoke", "bar"])

(hbnb)Place.show("efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6")
[Place] (efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6) {'id': 'efe34d81-1c2f-4cda-bb4a-786ab9a4c6a6', 'created_at': datetime.datetime(2022, 7, 1, 10, 34, 46, 406010), 'updated_at': datetime.datetime(2022, 7, 1, 10, 45, 50, 119480), 'name': 'Luis', 'max_guest': 5, 'latitude': 4.0, 'longitude': '-', 'amenity_ids': ['pool', 'sauna', 'karaoke', 'bar']}

```







## Author
---
- Leslie Paz - [Leslor](https://github.com/Leslor)
