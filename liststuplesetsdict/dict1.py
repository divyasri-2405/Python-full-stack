Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"divya","city":"vja"}
print(a)
{'name': 'divya', 'city': 'vja'}
type(a)
<class 'dict'>
b={1,2,3,4,"name"}
print(b)
{1, 2, 3, 4, 'name'}
type(b)
<class 'set'>
c={"name":"sajad","city":"kashmir"}
c
{'name': 'sajad', 'city': 'kashmir'}
print(c)
{'name': 'sajad', 'city': 'kashmir'}
a={"name":"divya","email":"divya123@gmail.com","mobile no":"78953404389"}
print(a)
{'name': 'divya', 'email': 'divya123@gmail.com', 'mobile no': '78953404389'}
a.keys()
dict_keys(['name', 'email', 'mobile no'])
a.dict_keys()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.dict_keys()
AttributeError: 'dict' object has no attribute 'dict_keys'
a.values()
dict_values(['divya', 'divya123@gmail.com', '78953404389'])
a.items()
dict_items([('name', 'divya'), ('email', 'divya123@gmail.com'), ('mobile no', '78953404389')])
a={"course":"python","institute":"codegnan"}
print(a)
{'course': 'python', 'institute': 'codegnan'}
a.update({"year":"2020"})
a
{'course': 'python', 'institute': 'codegnan', 'year': '2020'}
a.update({"name":"divya","month":7})
a
{'course': 'python', 'institute': 'codegnan', 'year': '2020', 'name': 'divya', 'month': 7}
b={"name":"divya","email":"divya123@gmail.com","mobile no":78953404389}
b
{'name': 'divya', 'email': 'divya123@gmail.com', 'mobile no': 78953404389}
print(b)
{'name': 'divya', 'email': 'divya123@gmail.com', 'mobile no': 78953404389}
print(a)
{'course': 'python', 'institute': 'codegnan', 'year': '2020', 'name': 'divya', 'month': 7}
a={"year":2026,"month":"july"}
>>> print(a)
{'year': 2026, 'month': 'july'}
>>> a.setdefault("date",5)
5
>>> print(a)
{'year': 2026, 'month': 'july', 'date': 5}
>>> a={"time":12,"date":7,"min":8,"sec":12}
>>> print(a)
{'time': 12, 'date': 7, 'min': 8, 'sec': 12}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("time")
12
>>> a
{'date': 7, 'min': 8, 'sec': 12}
>>> a.popitem()
('sec', 12)
>>> print(a)
{'date': 7, 'min': 8}
>>> a.popitem()
('min', 8)
>>> print(a)
{'date': 7}
>>> a={"college":"pvpsit","branch":"it"}
>>> a.get("college")
'pvpsit'
>>> a["branch"]
'it'
>>> a.get("branch")
'it'
>>> a["college"]
'pvpsit'
>>> a={"hour":9,"min":6,"sec"5}
SyntaxError: ':' expected after dictionary key
>>> a={"hour"9,"min":7,"sec";5}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a={"hour":9,"min":6,"sec":5}
>>> print(a)
{'hour': 9, 'min': 6, 'sec': 5}
>>> type(a)
<class 'dict'>
>>> a.clear()
>>> a
{}
b={}
b.update({"name":"divya"})
print(b)
{'name': 'divya'}

.
