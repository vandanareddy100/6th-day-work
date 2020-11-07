import csv
"""
with open("emp.csv","w",newline='') as f:
     w=csv.writer(f) # returns csv writer object 
     w.writerow(["ENO","ENAME","ESAL"]) 
     n=int(input("Enter Number of Employees:")) 
     for i in range(n): 
         eno=input("Enter Employee No:") 
         ename=input("Enter Employee Name:") 
         esal=input("Enter Employee Salary:") 
         w.writerow([eno,ename,esal]) 
print("Total Employees data written to csv file successfully")
"""

### DISPLAY EMPLOYEES WHOSE SALARY IS EMPTY###
with open("emp.csv",'r',newline='') as f:
    w=csv.reader(f)
    data = list(w)
    print(data[0])
    for i in data[1:]:
        if i[2] == '':
            for x in i[2]:
                print(x,end=',' )
            print(i)

####DISPLAY EMPLOYEES WHOSE SALARY IS GREATER THAN 3500###

with open("emp.csv",'r',newline='') as f:
    w=csv.reader(f)
    data = list(w)
    print(data[0])
    for i in data[1:]:
        if i[2] != '':
            if int(i[2])>3500:
                for x in i:
                    print(x,end=',', sep='\n' )
                #print(i)

###DISPLAY EMPLYOESS WHOSE NAME START WITH "A"#####


with open("emp.csv",'r',newline='') as f:
    w=csv.reader(f)
    data = list(w)
    print(data[0])
    for line in data:
        if line[1].startswith("A"):
            print(line)



#####DISPLAY EMPLOYEES WHOSE ID OR NAME OR SALARY IS EMPTY####

with open("emp.csv",'r',newline='') as f:
    w=csv.reader(f)
    data = list(w)
    print(data[0])
    for line in data:
        if line[0] == '' or line[1] == '' or line[2] == '' :
            print(line)
            
            
####DISPLAY EMPLOYESS WHOS ID OR NAME OR SALARY IS NOT EMPTY###
with open("emp.csv",'r',newline='') as f:
    w=csv.reader(f)
    data = list(w)
    #print(data[0])
    for line in data:
        #if line[0:] != '':
        if line[0] != '' and line[1] != '' and line[2] != '' :
            print(line)