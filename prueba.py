uid=[1,2,3]
students=['Juan','Jose','Larsen']
uid_student={uid: student for uid, student in zip(uid ,students)}


print(uid_student)