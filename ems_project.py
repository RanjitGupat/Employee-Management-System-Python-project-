# Employee Management System (EMS)

# Step 1: Initial Employee Data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Rina', 'age': 32, 'department': 'IT', 'salary': 70000},
    103: {'name': 'Amit', 'age': 29, 'department': 'Finance', 'salary': 60000}
}

# Step 2: Menu System
def main_menu():
    while True:
        print("\n==== Employee Management System ====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 3: Add Employee Function
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Try a different one.")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print(f"Employee {name} added successfully!")

    except ValueError:
        print("Invalid input. Please enter correct data types.")

# Step 4: View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 50)
    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t\t{details['salary']}")

# Step 5: Search Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print(f"\nEmployee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Please enter a valid numeric Employee ID.")

# Entry Point
if __name__ == "__main__":
    main_menu()
