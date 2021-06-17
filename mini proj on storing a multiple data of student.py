students =[]
while(True):
    print("1. Add Record:")
    print("2. Update Record:")
    print("3. Delete Record:")
    print("4. Search Record:")
    print("5. Display Record:")
    print("0. Exit")
    choice = int(input("Enter the Choice:"))
    if choice==1:
        student={}
        student['id'] = input("Enter student ID:")
        student['name'] =input("Enter student Name:")
        student['course'] =input("Enter student Course:")
        student['fee'] = int(input("Enter student Fee:"))
        students.append(student)
    elif choice==2:
        id =input("Enter id to Update:")
        for student in students:
            if student['id']==id:
                student['name'] = (input("Enter student Name:"))
                student['course'] = (input("Enter student Course:"))
                student['fee'] = int(input("Enter student Fee:"))
                print("Record updated sucessfully")
            else:
                print("Record not updated")
    elif choice==3:
        id =input("Enter the id to delete:")
        for student in students:
            if student['id'] == id:
                students.remove(student)
                print("Id deleted sucessfully")
            else:
                print("Id not deleted")
    elif choice == 4:
        id =input("Enter the id to search:")
        for student in students:
            if student['id'] == id:
                print("Student Name:", student['name'])
                print("Student Course:", student['course'])
                print("Student Fee:", student['fee'])
            else:
                print("No Id detected")
    elif choice == 5:
        id = (input("Enter the id to display:"))
        for student in students:
            if student['id'] == id:
                print("Student Id:", student['id'])
                print("Student Name:", student['name'])
                print("Student Course:", student['course'])
                print("Student Fee:", student['fee'])
            else:
                print("Record not Found")
            
    else:
        exit(0)
