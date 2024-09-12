import json

def list_all_employees(emps):
    print("\n")
    print("*" * 70)

    if(len(emps)<=0):
        print('Empty')
    else:
        for index, emp in enumerate(emps, start=1):
            print(f"{index} Name: {emp['name']}, Department: {emp['department']}, Salary: {emp['salary']} ")

    print("*" * 70)
    print("\n")

def add_employees(emps):
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    emps.append({'name': name, 'department': department, 'salary':salary})
    save_data_helper(emps)

def update_employees(emps):
    list_all_employees(emps)
    index=int(input('Enter the employee number to update: '))
    if 1<=index<=len(emps):
        name = input("Enter name: ")
        department = input("Enter department: ")
        salary = input("Enter salary: ")
        emps[index-1]={'name': name, 'department': department, 'salary':salary}
        save_data_helper(emps)
    else:
        print('Invalid input')

def delete_employees(emps):
    list_all_employees(emps)
    index=int(input('Enter the employee number to delete: '))
    if 1<=index<=len(emps):
        del emps[index-1]
        save_data_helper(emps)
    else:
        print('Invalid input')

def data_loader():
    try:
        with open('employees.txt','r') as file:
            return json.load(file) #json.load will read employees.txt and convert data into json format
    except FileNotFoundError:
        return []

def save_data_helper(emps):
    with open('employees.txt', 'w') as file:
        json.dump(emps, file) #json.dump will convert data into json format and save in employees.txt

def main():

    emps=data_loader()

    while True:
        print("\nEmployee Management System | Choose an option")
        print("1. List all employees ")
        print("2. Add new employee ")
        print("3. Update employee details ")
        print("4. Delete employee ")
        print("5. Exit the app ")

        choice=input('Enter your choice: ')

        match choice:
            case '1':
                list_all_employees(emps)
            case '2':
                add_employees(emps)
            case '3':
                update_employees(emps)
            case '4':
                delete_employees(emps)
            case '5':
                break
            case _:
                print('Invalid Input')


if __name__ ==  "__main__":
    main() 