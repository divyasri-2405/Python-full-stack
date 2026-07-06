Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"name":"divya","city":"vja"}
print(a)
{'name': 'divya', 'city': 'vja'}
a
{'name': 'divya', 'city': 'vja'}
type(a)
<class 'dict'>
b={"name":"sajad","email":"sajad1234@gmail.com","mobile no":9784278932}
print(b)
{'name': 'sajad', 'email': 'sajad1234@gmail.com', 'mobile no': 9784278932}
b.keys()
dict_keys(['name', 'email', 'mobile no'])
b.values()
dict_values(['sajad', 'sajad1234@gmail.com', 9784278932])
b.items()
dict_items([('name', 'sajad'), ('email', 'sajad1234@gmail.com'), ('mobile no', 9784278932)])
print(a)
{'name': 'divya', 'city': 'vja'}
a.update({"age":21})
a
{'name': 'divya', 'city': 'vja', 'age': 21}
a.update({"color":"pink"})
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink'}
b
{'name': 'sajad', 'email': 'sajad1234@gmail.com', 'mobile no': 9784278932}
a.update({"no":5,"gender":"female"})
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink', 'no': 5, 'gender': 'female'}
b
{'name': 'sajad', 'email': 'sajad1234@gmail.com', 'mobile no': 9784278932}
b.setdefault("gender":"male")
SyntaxError: invalid syntax
b.setdefault("gender","male")
'male'
b
{'name': 'sajad', 'email': 'sajad1234@gmail.com', 'mobile no': 9784278932, 'gender': 'male'}
b.setdefault("no",9,"color","black")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.setdefault("no",9,"color","black")
TypeError: setdefault expected at most 2 arguments, got 4
a.pop()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("email")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop("email")
KeyError: 'email'
a=
SyntaxError: invalid syntax
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink', 'no': 5, 'gender': 'female'}
a.pop("no")
5
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink', 'gender': 'female'}
a.popitem()
('gender', 'female')
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink'}
b.popitem()
('gender', 'male')
b
{'name': 'sajad', 'email': 'sajad1234@gmail.com', 'mobile no': 9784278932}
a.get("email")
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink'}
a.get("email")
a.get("name")
'divya'
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'color': 'pink'}
a.get('city')
'vja'
b
{'name': 'sajad', 'email': 'sajad1234@gmail.com', 'mobile no': 9784278932}
b[email]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b[email]
NameError: name 'email' is not defined. Did you mean: 'eval'? Or did you forget to import 'email'?
b["email"]
'sajad1234@gmail.com'
a={"hour":7,"min":4,"sec":90}
type(a)
<class 'dict'>
print(a)
{'hour': 7, 'min': 4, 'sec': 90}
a.clear()
a
{}
b={}
b.update("name":"divya"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
b.update("name":"divya")
SyntaxError: invalid syntax
b.update({"name":"divya"})
b
{'name': 'divya'}
a={"name":"divya","city":"vja","age":20}
print(a)
{'name': 'divya', 'city': 'vja', 'age': 20}
len(a)
3
a={"name":"divya","city":"vja","age":21,"name":"divya"}
a
{'name': 'divya', 'city': 'vja', 'age': 21}
a={"name":"divya","city":"vja","age":21,"name":"sajad"}
a
{'name': 'sajad', 'city': 'vja', 'age': 21}
a={"name":"divya","city":"vja","age":21,"name1":"sajad","city1":"kashmir","age1":29}
a
{'name': 'divya', 'city': 'vja', 'age': 21, 'name1': 'sajad', 'city1': 'kashmir', 'age1': 29}
a={"no":[1,2,3],"name":["advite","adraysh","varna"],"score":[100,200,300]}
a
{'no': [1, 2, 3], 'name': ['advite', 'adraysh', 'varna'], 'score': [100, 200, 300]}
a={"no":[1,2,3],"name":["advity","adraysh","varna"],"score":[100,200,300]}
a
{'no': [1, 2, 3], 'name': ['advity', 'adraysh', 'varna'], 'score': [100, 200, 300]}
a.keys()
dict_keys(['no', 'name', 'score'])
a.values()
dict_values([[1, 2, 3], ['advity', 'adraysh', 'varna'], [100, 200, 300]])
a.items()
dict_items([('no', [1, 2, 3]), ('name', ['advity', 'adraysh', 'varna']), ('score', [100, 200, 300])])
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> #[7,6,4,3,0,8,5,2,1]
>>> a[0:5]
[9, 1, 5, 2, 8]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b1=a[0:5]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> b1=a[0:5]
>>> b1
[9, 1, 5, 2, 8]
>>> b1.sort()
>>> b1
[1, 2, 5, 8, 9]
>>> b1.reverse()
>>> b1
[9, 8, 5, 2, 1]
>>> b2=a[6:10]
>>> b2
[6, 3, 7, 0]
>>> b2=a[5:10]
>>> b2
[4, 6, 3, 7, 0]
>>> b2.sort(0)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    b2.sort(0)
TypeError: sort() takes no positional arguments
>>> b2.sort()
>>> b2
[0, 3, 4, 6, 7]
>>> b2.reverse()
>>> b2
[7, 6, 4, 3, 0]
>>> b2+b1
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
