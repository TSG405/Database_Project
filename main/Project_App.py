# CODED BY @ TSG,2020 ---------------------------------------------------------------------------------------//

import project
import sqlite3

MENU_PROMPT = """
Please choose any one of the given options below:

1) ADD A NEW STUDENT INTO DATABASE
2) DISPLAY CURRENT RECORDS OF 'STUDENTS' DATABASE
3) FIND A STUDENT BY NAME
4) GET THE TOPPER OF THE CURRENT DATABASE
5) CHECK FOR A STUDENT'S OPPORTUNITY
6) EXIT

"""

def menu():
    connection=project.connect()
    project.create_table(connection)

    while(user_input := input(MENU_PROMPT)) != "6" :
        if user_input == "1":
            name = input("ENTER THE STUDENT NAME : ")
            tenth_marks = int(input("ENTER THE STUDENTS' tenth MARKS (IN %) : "))
            twelveth_marks = int(input("ENTER THE STUDENT'S twelveth MARKS (IN %) : "))
            graduate_CGPA= input("ENTER THE STUDENT'S GRADUATE MARKS (IN CGPA GRADE SCHEME) : ")
            interest = input("ENTER STUDENT'S INTEREST FIELD (SCIENCE or COMMERCE or ARTS or PSYCHOLOGY) : ")

            project.add_student(connection,name,tenth_marks,twelveth_marks,graduate_CGPA,interest)

        elif user_input == "2":
            student = project.get_all_students(connection)
            for st in student:
                print(f"{st[1]} -- ({st[2]}) --  ({st[3]}) -- ({st[4]}) -- ({st[5]})")
                
        elif user_input == "3":
            name = input(" ENTER THE STUDENT NAME TO FIND : ")
            student = project.get_student_by_name(connection,name)
            for st in student:
                print(f"{st[1]} -- ({st[2]}) --  ({st[3]}) -- ({st[4]}) -- ({st[5]})")
            
        elif user_input == "4":
            topper = project.get_topper(connection)
            print(" THE TOPPER IS --- ->  ",topper)
            
        elif user_input == "5":
            name = input(" ENTER THE STUDENT NAME TO FIND HIS OR HER OPPORTUNITY: ")
            op =  project.opportunity(connection,name)
            if op[0] == "science" or op[0] == "SCIENCE" :
                print(" \n\n ** OPPORTUNITY IN THE FIELD OF 'ENGINEERING','RESEARCH','HONORS','MEDICAL','STATISTICS','TEACHING' ** \n\n")
            elif  op[0] == "commerce" or op[0] == "COMMERCE" :
                print(" ** \n\n ** OPPORTUNITY IN THE FIELD OF 'CA','SALES & MANAGEMENT','STATISTICS','BUSINESS ADMINISTRATION' ** \n\n")
            elif  op[0] == "arts" or op[0] == "ARTS":
                print(" \n\n ** OPPORTUNITY IN THE FIELD OF 'HONORS','ARCHEOLOGY','TEACHING','ARTISTRY','TEACHING' ** \n\n")
            elif op[0] == "psychology" or op[0] == "PSYCHOLOGY":
                print(" \n\n ** OPPORTUNITY IN THE FIELD OF 'HUMAN RESOURCE','ADMINISTRATION','MEDICAL','RESEARCH'.'TEACHING' ** \n\n")
        else:
            print(" \n\n INVALID INPUT , please TRY again!!  \n\n")

menu()
