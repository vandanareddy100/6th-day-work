f=open("mytext.txt",'w')

dic={}

print(dic)
print("My To Do App")
print("============")
print("selection operation:")
print("1.add task")
print("2.view all task")
print("0. exit")
choice=input("enter choice(1/2/0):")

if choice == '1':
    n=input("enter task name")
    dic.update({n : 1})
    print(dic)
    print("task added")
    print(dic)
   
elif choice == '2':
    n= input("enter task name")
    dic.update({n:2})
    print(dic)
    print(".......")
    print("to shop")
    dic.update({n:2})
    print(dic)
    
elif choice == '0':
    print("bye")
else:
    print("invalid choice")
f.write(dic)

f.close()
