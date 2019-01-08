#!/usr/bin/env python
# coding: utf-8

# In[2]:


#programming exercise Q3
diff=eval(input("enter diff"))
firstterm=eval(input("enter the first term"))
nth=eval(input("enter the nth term"))
def seqnum(nth,diff,firstterm):
    an=firstterm+(nth-1)*diff
    return an
print(seqnum(nth,diff,firstterm))
while True:
    q=input("do you want to continue?")
    if q=="yes":
        nth2=eval(input("enter the nth2 term"))
        print(seqnum(nth2,diff,firstterm))
    else:
         break


# In[2]:


#programming exercise Q4
def checkpalidrome(pharase):
    if pharase==pharase[::-1]:
        print("is in palidrome")
    else:
        print("not in palidrome ")
        


# In[3]:


checkpalidrome('mom')


# In[4]:


checkpalidrome('car')


# In[2]:


#programming exercise Q5
name=input("enter name")
father_name=input("enter father  name")
science=int(input("enter the number in science"))
english=int(input("enter the number in english"))
islamiat=int(input("enter the number in islamiat"))
computer=int(input("enter the number in computer"))
total_marks=400
obtain_marks=science+english+islamiat+computer
percentage=(obtain_marks/total_marks)*100
def percentage():
    percentage=(obtain_marks/total_marks)*100
    return percentage
def grade():
    if percentage > 80:
        print("A one grade")
    elif percentage > 70:
        print("A grade")
    elif percentage > 60:
        print("B grade")
    elif percentage > 50:
        print("C grade")
def marksheet():
    print("my name",name)
    print("my father name",father_name)
    print("my marks in science",science)
    print("my marks in english",english)
    print("my marks in islamiat",islamiat)
    print("my marks in computer",computer)
    print("my total marks",obtain_marks)
    print("my percentage",percentage)
    print("my grade",grade)
    


# In[3]:


percentage()


# In[4]:


marksheet()


# In[7]:


#programming exercise Q6
def firstlawofmotion(vi,a,t):
    vf=vi+a*t
    return vf
def secondlawofmotion(vi,a,t):
    s=(vi*t)+(1/2)*a*t**2
    return s
def thirdlawofmotion(vf,vi,s):
    a=(vf**2-vi**2)/2*s
    return a


# In[9]:


firstlawofmotion(2,3,4)


# In[10]:


secondlawofmotion(1,2,3)


# In[11]:


thirdlawofmotion(4,5,6)


# In[ ]:


#programmingexercise Q7
g=9.8
import math
def timeofflight(Vo,theta):
    theta=(theta*math.pi)/180
    t=2*Vo*math.sin(theta)/g
    print("the time of flight",t,"sec")
def maxheight(V,theta):
    theta=(theta*math.pi)/180
    H=(V*math.sin(theta)**2/2*g)
    print("maximum height reached",H,"m")
    

