print("Welcome to the Student Data Organizer!")

student_records = []    # Master list

while True:
    print("\n Select an option : ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    ch = input("Select an option (1-6): ")
    
    match ch:
        
        case "1":       # Add Student
            
            print("\nEnter Student Details : ")
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            sub = input("Enter Subjects (comma-separated): ")
            
            # separating subjects
            sub_set = set()
            splited_sub = sub.split(",")        #separating from ,(comma)
            
            for i in splited_sub:
                if i:
                    sub_set.add(i)     #adding subjects in the set
            
            id_dob_tuple = (student_id, dob)     # student ID and dob as tuple
            
            # Storing everything in a dictionary
            student_dict = {
                "id_dob" : id_dob_tuple,
                "name" : name,
                "age" : age,
                "grade" : grade,
                "subjects" : sub_set
            }
            
            student_records.append(student_dict)        # Adding to the master list
            print("Student record added successfully!")

            
        case "2":       # Display All Students
            
            if len(student_records) == 0:
                print("\nNo student records found.")
            else:
                print("\n" + "=" * 110)
                print(f"{'Student ID':<12} {'Name':<20} {'Age':<6} {'Grade':<8} {'DOB':<12} {'Subjects'}")
                print("=" * 110)
                
                for student in student_records:
                    
                    s_id, s_dob = student["id_dob"]     # Unpack the tuple
                    
                    # Turn set back into a displayable string
                    subjects_list = list(student["subjects"])
                    subjects_str = ", ".join(sorted(subjects_list))
                    
                    print(f"{s_id:<12} {student['name']:<20} {student['age']:<6} {student['grade']:<8} {s_dob:<12} {subjects_str}")
                print("=" * 110)

                
        case "3":       # Update Student Information
            
            if len(student_records) == 0:
                print("\nNo student records found.")
            else:
                search_id = input("\nEnter the Student ID to update: ")
                found = False
                
                for student in student_records:
                    
                    s_id, _ = student["id_dob"]     # Unpack the tuple
                    
                    if s_id == search_id:
                        found = True
                        print(f"\nRecord found for {student['name']} : ")
                        print("1. Update Age")
                        print("2. Update Subjects")
                        update_ch = input("Choose an option to update (1 or 2): ")
                        
                        match update_ch:
                            case "1":
                                new_age = input("Enter new age: ")
                                student["age"] = new_age
                                print("Age updated successfully!")
                            case "2":
                                new_subjects_input = input("Enter new subjects (comma-separated): ")
                                
                                new_subjects_set = set()
                                raw_subs = new_subjects_input.split(",")
                                
                                for sub in raw_subs:
                                    if sub:
                                        new_subjects_set.add(sub)
                                        
                                student["subjects"] = new_subjects_set
                                print("Subjects updated successfully!")
                            case _:
                                print("Invalid choice. No changes made.")
                        break
                        
                if not found:
                    print("Student ID not found.")
                
    
        case "4":       # Delete Student
            
            if len(student_records) == 0:
                print("\nNo student records found.")
            else:
                search_id = input("\nEnter the Student ID to delete: ")
                found_index = -1
                
                for i in range(len(student_records)):       #finding student
                    s_id, _ = student_records[i]["id_dob"]
                    if s_id == search_id:
                        found_index = i
                        break
                        
                if found_index != -1:
                    
                    del student_records[found_index]        # Deleting using the 'del' keyword
                    print(f"Student record with ID {search_id} deleted successfully.")
                else:
                    print("Student ID not found.")
                
      
        case "5":       # Display Subjects Offered
            
            if len(student_records) == 0:
                print("\nNo student records found.")
            else:
                all_unique_subjects = set()
                
                # Combine sets from all individual students
                for student in student_records:
                    for sub in student["subjects"]:
                        all_unique_subjects.add(sub)
                        
                if len(all_unique_subjects) == 0:
                    print("\nNo subjects recorded yet.")
                else:
                    print("\n--- All Offered Subjects ---")
                    print(", ".join(list(all_unique_subjects)))

       
        case "6":       # Exit
            
            print("\nThank you for using the Student Data Organizer. Goodbye!")
            break
            
      
        case _:
            print("Invalid selection. Choose from 1 to 6.")

