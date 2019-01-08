#Program 6: Write a program which takes the number of rows and columns from the user and generate the values in form of list
r_n=int(input("input the number of rows"))
c_n=int(input("input the number of columns"))
m_list=[[0 for col in range(c_n)]for row in range(r_n)]
for row in range(r_n):
    for col in range(c_n):
        m_list[row][col]=row*col
        print(m_list)
