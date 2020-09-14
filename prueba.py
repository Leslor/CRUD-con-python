uid=[1,2,3,4,5]
students=['Juan','Jose','Larsen','Ariel','Fedora']
uid_student={uid: student for uid, student in zip(uid ,students)}


print(uid_student)