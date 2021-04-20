#dictionary
dic={}
print(type(dic))
#key value paiers
#roll:1001
#name:arun
#age:25

#key:roll,name,age

#value:1001,arun,25

student={"roll":1001,"name":"arun","age:":25}
print(student)                          #1support heterogenious


student1={"roll":1001,"name":"arun","age":25,"cpp":25}
print(student1)                         #duplicate key not supported
                                        #duplicate value supported
                                        #insertion order preserved
print(student1["age"])    #fetch a value using corresponding key
print(student1["name"])
#roll:1001
#name:arun
#age:25
#cpp:25
for i in student1:
     print(i,",",student1[i])

#update a value:mutable, using corresponding key
student1["name"]="arjun"
print(student1)
student1["age"]=30
student1["cpp"]+=10
print(student1)
#delete a key and value
#del
del student1["cpp"]
print(student1)

#add new key and new value
#total 150
print("age" in student1)   #check a key in dictionary
student1["total"]=150
print(student1)

#collection #define #hetro #insertion #duplicate    #mutable
#list        []      yes      yes       yes             yes
#tuples      ()       yes      yes      yes              no
#set        set()     yes      no        no              yes
#dictionary   {}      yes      yes       value support   yes
