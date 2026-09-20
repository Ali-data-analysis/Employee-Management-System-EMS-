# %% [markdown]
# Step 1 - Plan the Data Storage
# %%
employees = {
    101: {"name": "Satya","age": "27","department": "HR","salary": 50000},
    102: {"name": "Ali","age": "23","department": "dataScience","salary": 60000}
}
# %% [markdown]
# Add Employee
# %%
def add_employee():
    print("\n-----Add Employee-----")
# Validate Employee ID
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("employee already exists")
            else:
                break
        except ValueError:
            print("Please enter a valid ID")

# Get employee details
    name = input("Enter Employee Name: ").strip()
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            if age <= 0:
                print("Age must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid Age")

    department = input("Enter Department: ").strip()

    while True:
        try:
            salary = float(input("Enter Monthly Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid salary.")

# Store employee details
    employees[emp_id] = {
                         "name": name,
                                 "age": age,
                                  "department": department,
                                                "salary": salary

}
    print("\nEmployee added successfully!")


# %% [markdown]
# View All Employees
# %%
def view_employees():
    print("\n--- All Employees ---")

    if not employees:
        print("No employees available.")
        return

    # Table header
    print("-" * 80)
    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<10}"
        f"{'Department':<20}"
        f"{'Salary':<15}"
    )
    print("-" * 80)

    # Display employee details
    for emp_id, details in employees.items():
        print(
            f"{emp_id:<10}"
            f"{details['name']:<20}"
            f"{details['age']:<10}"
            f"{details['department']:<20}"
            f"{details['salary']:<15.2f}"
        )

    print("-" * 80)

# %%
# Step 5: Search Employee
def search_employee():
    print("\n--- Search Employee ---")

    try:
        emp_id = int(input("Enter Employee ID to search: "))

        if emp_id in employees:
            employee = employees[emp_id]

            print("\nEmployee Found!")
            print(f"Employee ID: {emp_id}")
            print(f"Name: {employee['name']}")
            print(f"Age: {employee['age']}")
            print(f"Department: {employee['department']}")
            print(f"Monthly Salary: {employee['salary']:.2f}")

        else:
            print("Employee not found.")

    except ValueError:
        print("Please enter a valid numeric Employee ID.")

# %%
# Step 2 & 6: Main Menu
def main_menu():
    while True:
        print("\n================================")
        print("   EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            print("\nThank you for using Employee Management System!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# Program Execution
if __name__ == "__main__":
    main_menu()
# %%
