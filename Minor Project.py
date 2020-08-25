#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import time
import pandas as pd
import random
import hashlib

def institution_module():
    li=[]
    
    filename="F:/Minor2/hash.txt"
    data = np.loadtxt(filename,dtype=str)
    previous_hash=data[len(data)-1]
    s=previous_hash
    
    print("Enter the data that you want to enter to the chain: ")
    print("Enter the new records")
    institution_name=input("Enter the name of the institution which is issuing the record: ")
    li.append(institution_name)
    s=s+','+institution_name
    print(s)
    enrl=int(input("Enter the enrollment number of the candidate: "))
    enr=str(enrl)
    print(enr)
    print(type(enr))
    li.append(enr)
    s=s+','
    s=s+enr
    name=input("Enter the name of the candidate: ")
    li.append(name)
    s=s+','+name
    father_name=input("Enter the father's name of the candidate: ")
    li.append(father_name)
    s=s+','+father_name
    dob=input("Enter the Date of Birth of the Candidate: ")
    li.append(dob)
    s=s+','+dob
    course_details=input("Enter the course Details for which the certificate is being issued: ")
    li.append(course_details)
    s=s+','+course_details
    course_grade=input("Enter the CGPA or the Grade Point achieved in this course by the candidate: ")
    li.append(course_grade)
    s=s+','+course_grade
    passing_details=input("Enter the passing details of this particular course: ")
    li.append(passing_details)
    s=s+','+passing_details
    print(s)
    
    result = hashlib.sha256(s.encode())
    print("The hexadecimal equivalent of SHA256 for the given data block is : ")
    has=result.hexdigest()
    print(has)
    
    s=s+','+has
    print("The data to be written to the file after including the hash of the current block:")
    print(s)
    
    file1=open("F:\\Minor2\\hash.txt","a")
    file1.write(has+"\n")
    file1.close()
    file2=open("F:\\Minor2\\users.txt","a")
    file2.write(s+"\n")
    file2.close()
    
def institution_key_generator():
    k=""
    k=k+','
    for i in range(random.randint(1,100)):
        num=random.random()
        a=str(num)
        k=k+a
        k=k+','
    result=hashlib.sha1(k.encode())
    key=result.hexdigest()
    return key
def recruiter_module():
    var=institution_key_generator()
    if var==None:
        print("Sorry, You can not access our database.")
    else:
        elapsed_time=0.0
        start=time.time()
        f = open("F:/Minor2/users.txt", "r")
        flag=0;
        while(elapsed_time<0.0012 or flag==0):
            print(f.read())
            end=time.time()
            elapsed_time=end-start
            flag=1
        print("The access time has elapsed.")
        f.close()

def candidate_module():
    n=int(input("Enter your Enrollment No: "))
    no=str(n)
    filename="F:/Minor2/users2.txt"
    data = np.loadtxt(filename,delimiter=',',dtype=str)
    print(len(data))
    print(data)
    for i in range(len(data)):
        if data[i][2]==no:
            print("Your Institutions Name: ", data[i][0])
            print("Your Enrollment No: ",data[i][1])
            print("Your Name: ",data[i][3])
            print("Your DOB: ",data[i][4])
            print("Name of your course: ",data[i][5])
            print("Your Grade: ",data[i][6])
            print("Other details and Remarks About Your Course: ",data[i][7])

print("Welcome to Blockchain Based Academic and Professional Record System")
import numpy as np
import pandas as pd
import time
filename="F:/Minor2/user.txt"
data = np.loadtxt(filename,dtype=str)
print("The data in the user file is as follows:")
print(data)
print("The number of the users authorised to use the system right now and their details are as follows:")
print(data.shape)
print(len(data))

print("Enter your choice from the options given below:")
print("1. Enter new records")
print("2. Access the records")
choice=int(input("Enter your choice: "))
usr=input("Enter your username: ")
pswd=input("Enter your password: ")
flag=0
if choice==1:
    for i in range(len(data)):
        if data[i][0]=="institution" and data[i][1]==usr and data[i][2]==pswd:
            flag=1
            temp=i
            break
if choice==2:
    for i in range(len(data)):
        if data[i][0]!="institution" and data[i][1]==usr and data[i][2]==pswd:
            flag=1
            temp=i
            break
if flag==1:
    if data[temp][0]=="institution":
        print("Institution User accepted.")
        institution_module()
    elif data[temp][0]=="recruiter":
        print("Recruiter User accepted.")
        recruiter_module()
    elif data[temp][0]=="candidate":
        print("Candidate User accepted.")
        candidate_module()
elif flag==0:
    print('''The User does not exist. Do you want to create a new user?(Y/N)''')
    ch=input('''Enter your choice:(Y/N)''')
    if ch=="Y":
        print("For the new user, enter from the following choices:")
        print("1.Institution")
        print("2.Recruiter")
        print("3.Candidate")
        user_type=int(input("Enter the type of the new user that you want to enter:"))
        us=""
        if user_type==1:
            us="institution"
        elif user_type==1:
            us="recruiter"
        elif user_type==3:
            us="candidate"
        user_name=input("Enter the user name of the user: ")
        user_pswd=input("Enter the password for the user: ")
        wr=us+","+user_name+","+user_pswd
        file1=open("F:\\Minor2\\user.txt","a")
        file1.write("\n"+wr)
        file1.close()


# In[ ]:




