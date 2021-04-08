# GUI Implementation using TKinter, Python3, SQLite3
import sqlite3
from tkinter import *

root=Tk()
root.geometry('720x220')
root.title('STUDENT DATABASE GUI')


def submit():
    x=id_no.get()
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    for row in cur.fetchall():
        if row[0]==x:
            name.set(row[1])
            id_no.set(row[0])
            tenth_marks.set(row[2])
            twelveth_marks.set(row[3])
            graduate_CGPA.set(row[4])
            interest.set(row[5])
    conn.commit()
    
def res2():
    name1.set(' ')
    id_no1.set(' ')
    tenth_marks1.set(' ')
    twelveth_marks1.set(' ')
    graduate_CGPA1.set(' ')
    t.set('SCIENCE')
    
def add():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    i = id_no1.get()
    n = name1.get()
    t1 = tenth_marks1.get()
    t2 = twelveth_marks1.get() 
    g = graduate_CGPA1.get()
    i1 = t.get()
    INSERT_STUDENT = "INSERT INTO students (id_no,name,tenth_marks,twelveth_marks,graduate_CGPA,interest)VALUES(?,?,?,?,?,?);"
    cur.execute(INSERT_STUDENT,(i,n,t1,t2,g,i1))
    conn.commit()
    res2()
    
def res():
    name.set(' ')
    id_no.set(' ')
    tenth_marks.set(' ')
    twelveth_marks.set(' ')
    graduate_CGPA.set(' ')
    interest.set(' ')
    res2()

    
choices = {'SCIENCE','ARTS','COMMERCE','PSYCHOLOGY'}

name=StringVar()
id_no=IntVar()
tenth_marks=IntVar()
twelveth_marks=IntVar()
graduate_CGPA=IntVar()
interest=StringVar()

name1=StringVar()
id_no1=IntVar()
tenth_marks1=IntVar()
twelveth_marks1=IntVar()
graduate_CGPA1=IntVar()
t = StringVar(root)
t.set('SCIENCE')


Label(root,text="Enter  STUDENT ID  ").grid(row=1,column=1)
Label(root,text='STUDENT DETAILS',bg='Light Blue').grid(row=2,column=2)
Label(root,text='Name  ').grid(row=3,column=0)
Label(root,text='SSC Percentage (%) ').grid(row=4,column=0)
Label(root,text='HSC Percentage (%) ').grid(row=5,column=0)
Label(root,text='Graduation SGPA  ').grid(row=6,column=0)
Label(root,text='Interest  ').grid(row=7,column=0)

Label(root,text='ADD INFORMATION',bg='Light Blue').grid(row=2,column=8)
Label(root,text="Add Student ID ").grid(row=3,column=7)
Label(root,text="Add Student's Name ").grid(row=4,column=7)
Label(root,text='Add SSC Percentage (%) ').grid(row=5,column=7)
Label(root,text='Add HSC Percentage (%) ').grid(row=6,column=7)
Label(root,text='Add Graduation SGPA ').grid(row=7,column=7)
Label(root,text="Add Student's Interest ").grid(row=8,column=7)


Entry(root,textvariable=id_no).grid(row=1,column=2)
Entry(root,textvariable=name).grid(row=3,column=1)
Entry(root,textvariable=tenth_marks).grid(row=4,column=1)
Entry(root,textvariable=twelveth_marks).grid(row=5,column=1)
Entry(root,textvariable=graduate_CGPA).grid(row=6,column=1)
Entry(root,textvariable=interest).grid(row=7,column=1)

Entry(root,textvariable=id_no1).grid(row=3,column=8)
Entry(root,textvariable=name1).grid(row=4,column=8)
Entry(root,textvariable=tenth_marks1).grid(row=5,column=8)
Entry(root,textvariable=twelveth_marks1).grid(row=6,column=8)
Entry(root,textvariable=graduate_CGPA1).grid(row=7,column=8)
OptionMenu(root,t,*choices).grid(row=8, column=8)


Button(root,text='     SUBMIT     ',command=submit).grid(row=1,column=4)
Button(root,text='         RESET         ',command=res).grid(row=9,column=2)
Button(root,text='   ADD   ',command=add).grid(row=9,column=8)
root.mainloop()


@CODED BY TSG405, 2021
