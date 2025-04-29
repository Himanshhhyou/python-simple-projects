# Print the heading of the program
print("----- Student Management System -----")

# List to store all student records
students = []

# Infinite loop to keep the program running until user exits
while True:
    # Display menu options
    print("\n1. Add Student Data")
    print("2. Show Student Data")
    print("3. Update Student Data")
    print("4. Delete Student Data")
    print("5. Exit")

    # Take user input for choice
    choice = input("Enter choice (1-5): ")

    # Validate if the input is a number
    if not choice.isdigit():
        print("Please enter a valid number!")
        continue  # Restart the loop

    choice = int(choice)  # Convert choice to integer

    # Option 1: Add a new student
    if choice == 1:
        sName = input("Enter student name: ")
        sAge = input("Enter student age: ")
        sCourse = input("Enter student course: ")
        
        # Create a dictionary for student
        student = {
            "name": sName,
            "age": sAge,
            "course": sCourse
        }
        # Add student to the list
        students.append(student)
        print("Student added successfully!")

    # Option 2: Show details of a student
    elif choice == 2:
        n = input("Enter the name of student to display: ")
        
        for student in students:
            if student["name"].lower() == n.lower():
                # Display student details
                print("\n--- Student Found ---")
                print("Name: ", student["name"])
                print("Age: ", student["age"])
                print("Course: ", student["course"])
                break  # Exit the loop once found
        
        else:
            print("Student not found.")

    # Option 3: Update existing student data
    elif choice == 3:
        n = input("Enter the name of student to update: ")
        
        for student in students:
            if student["name"].lower() == n.lower():
                print("Enter new data (leave blank to keep old value):")
                
                # Take new inputs, if left blank keep old
                new_name = input(f"New name (current: {student['name']}): ")
                new_age = input(f"New age (current: {student['age']}): ")
                new_course = input(f"New course (current: {student['course']}): ")

                if new_name:
                    student["name"] = new_name
                if new_age:
                    student["age"] = new_age
                if new_course:
                    student["course"] = new_course
                
                print("Student data updated successfully!")
                break
        
        else:
            print("Student not found.")

    # Option 4: Delete a student record
    elif choice == 4:
        n = input("Enter the name of student to delete: ")
        
        for student in students:
            if student["name"].lower() == n.lower():
                students.remove(student)  # Remove the student
                print("Student deleted successfully!")
                found = True
                break
        
        else:
            print("Student not found.")

    # Option 5: Exit the program
    elif choice == 5:
        print("Exiting program... Goodbye!")
        break  # Exit the infinite loop and program

    # If invalid option entered
    else:
        print("Invalid choice. Please select between 1 to 5.")
