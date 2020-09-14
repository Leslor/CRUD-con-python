uid=[1,2,3,4,5]
students=['Juan','Jose','Larsen','Ariel','Fedora']
uid[0]=0
uid_student={uid: student for uid, student in zip(uid ,students)}


#Comentario para probar reset HEAD

print(uid_student,"Nuevo")