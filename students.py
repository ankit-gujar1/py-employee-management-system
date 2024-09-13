import json

def list_all_students(students):
    print("\n")
    print("*" * 70)

    if(len(students)<=0):
        print('Empty')
    else:
        for index, student in enumerate(students, start=1):
            print(f"{index} Name: {student['name']}, Subject: {student['subject']}, Result: {student['result']} ")

    print("*" * 70)
    print("\n")

def add_students(students):
    name = input("Enter name: ")
    subject = input("Enter subject: ")
    result = input("Enter result: ")
    students.append({'name': name, 'subject': subject, 'result':result})
    save_data_helper(students)

def update_students(students):
    list_all_students(students)
    index=int(input('Enter the student number to update: '))
    if 1<=index<=len(students):
        name = input("Enter name: ")
        subject = input("Enter subject: ")
        result = input("Enter result: ")
        students[index-1]={'name': name, 'subject': subject, 'result':result}
        save_data_helper(students)
    else:
        print('Invalid input')

def delete_students(students):
    list_all_students(students)
    index=int(input('Enter the student number to delete: '))
    if 1<=index<=len(students):
        del students[index-1]
        save_data_helper(students)
    else:
        print('Invalid input')

def data_loader():
    try:
        with open('students.txt','r') as file:
            return json.load(file) #json.load will read students.txt and convert data into json format
    except FileNotFoundError:
        return []

def save_data_helper(students):
    with open('students.txt', 'w') as file:
        json.dump(students, file) #json.dump will convert data into json format and save in students.txt

def main():

    students=data_loader()

    while True:
        print("\nStudent Management System | Choose an option")
        print("1. List all students ")
        print("2. Add new students ")
        print("3. Update students details ")
        print("4. Delete students ")
        print("5. Exit the app ")

        choice=input('Enter your choice: ')

        match choice:
            case '1':
                list_all_students(students)
            case '2':
                add_students(students)
            case '3':
                update_students(students)
            case '4':
                delete_students(students)
            case '5':
                break
            case _:
                print('Invalid Input')


if __name__ ==  "__main__":
    main() 