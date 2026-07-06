Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={"name":"divya","course":"python","year":2026}
>>> print(a)
{'name': 'divya', 'course': 'python', 'year': 2026}
>>> len(a)
3
>>> a={"name":"sajad","city":"vja","name":"sajad"}
>>> a
{'name': 'sajad', 'city': 'vja'}
>>> a={"name":"sajad":,"city":"vja","name":"divya"}
SyntaxError: invalid syntax
>>> a={"name":"sajad","city":"vja","name":"divya"}
>>> print(a)
{'name': 'divya', 'city': 'vja'}
>>> a={"name1":"divya","city1":"vja","name2":"sajad","city2":"Hyd"}
>>> print(a)
{'name1': 'divya', 'city1': 'vja', 'name2': 'sajad', 'city2': 'Hyd'}
>>> a={"idnos":[10,20,30],"names":["trinadh","ishwarya","pani"],"marks":[100,200,300]}
>>> a
{'idnos': [10, 20, 30], 'names': ['trinadh', 'ishwarya', 'pani'], 'marks': [100, 200, 300]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['trinadh', 'ishwarya', 'pani'], 'marks': [100, 200, 300]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['trinadh', 'ishwarya', 'pani'], [100, 200, 300]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['trinadh', 'ishwarya', 'pani']), ('marks', [100, 200, 300])])
