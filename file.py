
f=open("file1.txt",'w')
f.write("Learning python is easy.\n")
#f.write("welcome to python.\n")
print("success")
f=open("file1.txt","r")
data=f.read()
words=data.split()
print("number of words in text file:",len(words))
#f=open("file1.txt","r")
#data=f.read()
number_of_characters = len(data)
print("number of characters in textfile:",number_of_characters)
fname=input("enter fil name:")
num_lines=0
with open(fname,'r')as f:
    for line in f:
        num_lines += 1
        print("number of lines:")
        print(num_lines)
f.close()
 
