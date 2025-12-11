employees = {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}

def add_employee():
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    print("Employee added successfully!\n")


def view_emp():
    for emp_id, data in employees.items():
        print(f"ID: {emp_id}, Name: {data['name']}, Age: {data['age']}, Dept: {data['department']}, Salary: {data['salary']}")
    print()


def search_emp():
    emp_id = int(input("Enter employee ID to search: "))

    if emp_id in employees:
        data = employees[emp_id]
        print("Employee found!")
        print(f"Name: {data['name']}, Age: {data['age']}, Dept: {data['department']}, Salary: {data['salary']}\n")
    else:
        print("Employee does NOT exist!\n")


def exit_program():
    print("Thank you!")
    exit()


operations = {
    1: add_employee,
    2: view_emp,
    3: search_emp,
    4: exit_program
}


def main_menu():
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter a number 1-4: "))

    match choice:
        case 1:
            add_employee()
        case 2:
            view_emp()
        case 3:
            search_emp()
        case 4:
            exit_program()
        case _:
            print("Invalid choice!")


main_menu()
