#file handling
#write()

a=open("divya.txt","w")
a.write("codegnan")
a.close()

a=open("mds.txt","w")
a.write("python")
a.close()

a=open("divya.txt","w")
a.write("PYTHON")
a.close()

#append()

a=open("divya.txt","a")
a.write("\tdata science")
a.close()

a=open("divya.txt","w")
a.write(input("data"))
a.close()

a=open("divya.txt","w")
b=input("data")
a.write(b)
a.close()

#read()

a=open("divya.txt")
#print(a.read())-#it will display entire content
#print(a.readline())-#it will display first line
#print(a.readlines())-#it will display in list with \n
#print(a.read(8))-#it will display no.of characters

#writelines()-#it makes every object side by side

a=open("ds.txt","w")
b=["divya","kavya","vaishnavi","girija","kumar"]
a.writelines("\n".join(b))
a.close()

a=open("ds.txt","w")
b=["divya","kavya","vaishnavi","girija","kumar"]
a.writeline(b)
a.close()

a=open("ds.txt")#you can also use .py also
print(a.read())

a=open("C:\\Users\\HP\\Downloads\\codegnan python\\map\\map1.py")
print(a.read())
