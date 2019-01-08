#4. Write a program which will collect your name, your father’s name, your roll number and your subjects (5 Subjects with name and numbers). At the end it will generate a result with your name, your father’s name, your details subjects, marks you have obtained with total marks with grade and percentage.  
my_name=input("enter your name")
my_father_name=input("enter your father name")
roll_no=input("enter your roll no")
sub_1=input("enter your subject name")
sub_2=input("enter your subject name")
sub_3=input("enter your subject name")
sub_4=input("enter your subject name")
sub_5=input("enter your subject name")
total_marks=int(input("enter total number"))
marks_1=int(input("enter your numbers"))
marks_2=int(input("enter your numbers"))
marks_3=int(input("enter your numbers"))           
marks_4=int(input("enter your numbers"))           
marks_5=int(input("enter your numbers"))
Obtain_marks=(marks_1+marks_2+marks_3+marks_4+marks_5)
percentage=(Obtain_marks/total_marks)*100
print("name of the student",my_name)
print("name of father",my_father_name)
print("numbers obtain in ",sub_1,"=",marks_1)
print("numbers obtain in ",sub_2,"=",marks_2)
print("numbers obtain in ",sub_3,"=",marks_3)
print("numbers obtain in ",sub_4,"=",marks_4)
print("numbers obtain in ",sub_5,"=",marks_5)
print("marks obtain out of total marks""=",Obtain_marks)
print("percentage of ",my_name,"",percentage)
if Obtain_marks<50:
    print( "grade F")
if Obtain_marks<100:
    print( "grade E")
if Obtain_marks<200:
    print( "grade D")
if Obtain_marks<300:
    print( "grade C")
if Obtain_marks<400:
    print( "grade B")
if Obtain_marks<500:
    print( "grade A")
    
