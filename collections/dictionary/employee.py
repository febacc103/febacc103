#employee

#id,name,desingnation ,salary
#1.employee name
#check company
#add company:luminar
#update salary
#print key value pairs

employee={"i_d":1001,"name":"feba","designation":"teacher","salary":50000,}
print(employee)
print("company" in employee)
employee["company"]="luminar"
employee["salary"]+=15000
for i in employee:
    print(i ,"=",employee[i])
