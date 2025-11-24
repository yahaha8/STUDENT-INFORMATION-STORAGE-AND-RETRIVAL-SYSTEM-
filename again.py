
import details

print("1: if you want to check student info")
print("2: if you want add new student info")
print("3: exit")
ch=int(input("enter your choice:"))


if ch==1:
    
    name=input("enter name:")
    for i in details.students:
       if i["name"].lower()==name.lower():
        print(i)
       else:
        print("student not found")
        break
       

elif ch==2:

   myfile=open("storeddata.txt","a+")
   d1={}
   ans="y"
   while ans=="y":
       n1=input("enter the the name of student:")
       br=input("enter the branch of student:")
       regn=input("enter the regno:")
       cit=input("enter the address: ")
       d1["name"]=n1
       d1["branch"]=br
       d1["regno"]=regn
       d1["city"]=cit

       ans=input("do you want to continue adding information?(y/n)")  
       myfile.write(str(d1)+"\n") 
 
   myfile.close()


elif ch==3:
   print("exiting the program")

else:
   print("please enter the specified numbers only")
